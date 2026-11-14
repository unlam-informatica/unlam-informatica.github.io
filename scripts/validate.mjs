import fs from 'node:fs';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { load } from 'cheerio';
import YAML from 'yaml';
import { navigationPath } from './navigation.mjs';
const walk = dir => fs.readdirSync(dir, {withFileTypes:true}).flatMap(e => e.isDirectory() ? walk(path.join(dir,e.name)) : [path.join(dir,e.name)]);
const files = walk('dist');
const errors = [];
const pages = new Map();
const route = p => '/'+path.relative('dist',p).replace(/index\.html$/, '');
for (const p of files.filter(p => p.endsWith('.html'))) pages.set(route(p), {p,$:load(fs.readFileSync(p,'utf8'))});
const sourceRoutes = new Set();
for (const p of walk('src/content/docs').filter(p => /\.mdx?$/.test(p))) {
 const text = fs.readFileSync(p,'utf8');
 const fm = YAML.parse(text.match(/^---\n([\s\S]*?)\n---/)[1]);
 const r = '/'+(fm.slug ? fm.slug+'/' : '');
 if (sourceRoutes.has(r)) errors.push(`Duplicate route ${r}`);
 sourceRoutes.add(r);
 if (!pages.has(r)) errors.push(`Missing rendered page ${r}`);
 if (/^\{:\s/m.test(text)) errors.push(`Unconverted Kramdown in ${p}`);
}
function target(url) {
 const p = decodeURIComponent(url.pathname);
 const exact = 'dist'+p;
 if (fs.existsSync(exact) && fs.statSync(exact).isFile()) return exact;
 if (fs.existsSync(path.join(exact,'index.html'))) return path.join(exact,'index.html');
 return null;
}
let checked = 0;
const graph = new Map();
for (const [r, {$}] of pages) {
 graph.set(r, new Set());
 for (const el of $('a[href],img[src],script[src],link[href],source[src]').toArray()) {
  const value = $(el).attr('href') ?? $(el).attr('src');
  let u; try { u = new URL(value, 'https://unlam-informatica.github.io'+r); } catch {continue;}
  if (u.origin !== 'https://unlam-informatica.github.io') continue;
  // Astro's generated 404 canonical is metadata, not a navigable content route.
  if (r === '/404.html' && $(el).attr('rel') === 'canonical') continue;
  checked++;
  const file = target(u);
  if (!file) { errors.push(`${r} -> ${value}`); continue; }
  if ($(el).is('a') && file.endsWith('index.html')) {
   const destination = route(file);
   graph.get(r).add(destination);
   if (!value.startsWith('#') && !value.startsWith('?') && u.pathname !== navigationPath(destination)) errors.push(`Directory navigation ${r} -> ${value}`);
  }
  if (u.hash && file.endsWith('.html')) {
   const other = pages.get(route(file));
   const id = decodeURIComponent(u.hash.slice(1));
   if (other && !other.$('[id]').toArray().some(e=>other.$(e).attr('id')===id)) errors.push(`Missing anchor ${r} -> ${value}`);
  }
 }
 if ($('.katex-error').length) errors.push(`Math rendering errors ${r}: ${$('.katex-error').text()}`);
}
// A page existing on disk is insufficient: every academic page must be reachable
// from the homepage through links actually rendered in the portal.
const reachable = new Set(['/']);
for (const current of reachable) for (const next of graph.get(current) || []) reachable.add(next);
for (const r of sourceRoutes) if (!reachable.has(r)) errors.push(`Unreachable from homepage ${r}`);
const matrix = JSON.parse(fs.readFileSync('migration/compatibility.json'));
for (const entry of matrix) {
 if (!target(new URL(entry.old, 'https://unlam-informatica.github.io'))) errors.push(`Missing legacy path ${entry.old}`);
 if (!target(new URL(entry.canonical, 'https://unlam-informatica.github.io'))) errors.push(`Missing canonical ${entry.canonical}`);
 if (entry.kind === 'page') {
  if (entry.navigation !== navigationPath(entry.canonical)) errors.push(`Unexpected navigation path ${entry.canonical}`);
  const file = target(new URL(entry.navigation, 'https://unlam-informatica.github.io'));
  if (!file) errors.push(`Missing navigation file ${entry.navigation}`);
  const legacy = pages.get(entry.old);
  if (legacy && legacy.$('meta[http-equiv="refresh"]').length) {
   const refresh = legacy.$('meta[http-equiv="refresh"]').attr('content');
   if (refresh !== '0;url=' + entry.navigation) errors.push(`Unsafe legacy redirect ${entry.old}`);
   if (!legacy.$('script').text().includes('location.search+location.hash')) errors.push(`Legacy redirect loses query/fragment ${entry.old}`);
  }
 }
}
const provenance = JSON.parse(fs.readFileSync('migration/sources.json'));
for (const page of provenance.pages) {
 for (const output of [page, ...(page.additionalOutputs || [])]) {
  if (!fs.existsSync(output.output) || createHash('sha256').update(fs.readFileSync(output.output)).digest('hex') !== output.migratedSha256) errors.push(`Migrated page hash mismatch ${output.output}`);
 }
}
for (const a of provenance.assets) {
 if (createHash('sha256').update(fs.readFileSync(a.output)).digest('hex') !== a.sha256 || createHash('sha256').update(fs.readFileSync('dist/'+a.output.slice(7))).digest('hex') !== a.sha256) errors.push(`Asset changed ${a.output}`);
}
const report = { pages: sourceRoutes.size, reachableFromHomepage: [...sourceRoutes].filter(r => reachable.has(r)).length, renderedHtml: pages.size, internalLinksAndResources: checked, compatibilityEntries: matrix.length, assets: provenance.assets.length, errors: [...new Set(errors)] };
fs.writeFileSync('migration/validation.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(report,null,2));
if (errors.length) process.exitCode = 1;
