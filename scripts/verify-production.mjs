// Read-only check of the deployed portal against the migration compatibility matrix.
import fs from 'node:fs';
import { createHash } from 'node:crypto';
import { load } from 'cheerio';
const origin = new URL(process.argv[2] || 'https://unlam-informatica.github.io').origin;
const matrix = JSON.parse(fs.readFileSync('migration/compatibility.json', 'utf8'));
const sources = JSON.parse(fs.readFileSync('migration/sources.json', 'utf8'));
const hashes = new Map(sources.assets.map(a => ['/' + a.output.slice(7), a.sha256]));
const checks = new Map();
for (const entry of matrix) {
  checks.set(entry.old, { ...entry, url: entry.old, canonicalPage: entry.old === entry.canonical && entry.kind === 'page' });
}
for (const entry of matrix.filter(e => e.kind === 'page')) checks.set(entry.canonical, { ...entry, url: entry.canonical, canonicalPage: true });
checks.set('/pagefind/pagefind.js', { url: '/pagefind/pagefind.js', kind: 'search' });
const queue = [...checks.values()];
const errors = [];
let checked = 0;
await Promise.all(Array.from({ length: 4 }, async () => {
  while (queue.length) {
    const entry = queue.shift();
    try {
      const response = await fetch(origin + entry.url, { signal: AbortSignal.timeout(30000) });
      if (!response.ok) throw Error(`HTTP ${response.status}`);
      if (entry.kind === 'search' && !response.headers.get('content-type')?.includes('javascript')) throw Error('El módulo de búsqueda no es JavaScript');
      if (entry.kind === 'asset') {
        const hash = createHash('sha256').update(Buffer.from(await response.arrayBuffer())).digest('hex');
        if (hash !== hashes.get(entry.url)) throw Error('SHA-256 distinto al recurso original');
      } else if (entry.kind === 'page') {
        const $ = load(await response.text());
        const canonical = $('link[rel="canonical"]').attr('href');
        if (!canonical || new URL(canonical).pathname !== entry.canonical) throw Error('Canonical inesperado: ' + canonical);
        if (entry.canonicalPage && !$('meta[name="generator"]').toArray().some(e => $(e).attr('content')?.startsWith('Starlight '))) throw Error('La ruta todavía no sirve Starlight');
      }
    } catch (error) {
      errors.push({ url: entry.url, error: error.message });
    }
    checked++;
  }
}));
console.log(JSON.stringify({ origin, checked, errors }, null, 2));
if (errors.length) process.exitCode = 1;
