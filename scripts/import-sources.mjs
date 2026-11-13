// One-time, reproducible import. Reads local clones; never writes to source repositories.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { execFileSync } from 'node:child_process';
import YAML from 'yaml';
const root = process.argv[2];
if (!root) throw Error('Usage: node scripts/import-sources.mjs /path/to/clones');
const subjects = ['analisis-matematico-i', 'bbdd-aplicadas', 'diseno-de-software'];
const titles = ['Análisis Matemático I', 'Bases de Datos Aplicadas', 'Diseño de Software'];
const walk = (dir) => fs.readdirSync(dir, { withFileTypes: true }).flatMap(e => e.name.startsWith('.') ? [] : e.isDirectory() ? walk(path.join(dir, e.name)) : [path.join(dir, e.name)]);
const hash = s => crypto.createHash('sha256').update(s).digest('hex');
const save = (p, data) => { fs.mkdirSync(path.dirname(p), { recursive: true }); fs.writeFileSync(p, data); };
const matrix = [{ source: 'index.md', old: '/', canonical: '/', kind: 'page' }];
const provenance = [];
const pages = [];
const assets = [];
for (const [i, subject] of subjects.entries()) {
  const dir = path.join(root, subject);
  const config = YAML.parse(fs.readFileSync(path.join(dir, '_config.yml'), 'utf8'));
  const excluded = new Set(['AGENTS.md','CLAUDE.md','CODEX.md','README.md',...(config.exclude || [])]);
  const files = walk(dir).filter(p => !path.relative(dir,p).split('/').some(s => s.startsWith('_') || excluded.has(s)));
  const docs = files.filter(p => p.endsWith('.md')).map(p => {
    const text = fs.readFileSync(p, 'utf8');
    const match = text.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n/);
    if (!match) return null;
    const data = YAML.parse(match[1]);
    const rel = path.relative(dir, p);
    const old = '/' + subject + (data.permalink || '/' + rel.replace(/\.md$/, '.html'));
    const canonical = old.replace(/(?:index)?\.html$/, '').replace(/\/$/, '') + '/';
    return { p, rel, text, body: text.slice(match[0].length), data, old, canonical };
  }).filter(Boolean);
  const urlMap = new Map();
  for (const d of docs) {
    for (const key of [d.old, d.canonical, '/'+subject+'/'+d.rel, '/'+subject+'/'+d.rel.replace(/\.md$/, '.html')]) urlMap.set(key, d.canonical);
    matrix.push({ source: subject+'/'+d.rel, old: d.old, canonical: d.canonical, kind: 'page' });
  }
  function url(value, doc) {
    if (!value || value.startsWith('#') || /^(?:mailto:|data:|tel:)/.test(value)) return value;
    let u;
    try { u = new URL(value, 'https://unlam-informatica.github.io/'+subject+'/'+doc.rel); } catch { return value; }
    if (u.origin !== 'https://unlam-informatica.github.io') return value;
    let pathname = decodeURI(u.pathname);
    if (/^\/unidad-/.test(pathname)) pathname = '/'+subject+pathname;
    let destination = urlMap.get(pathname);
    if (!destination) {
      const candidates = docs.filter(d => d.canonical.split('/').at(-2) === pathname.replace(/\/$/,'').split('/').at(-1) && d.canonical.split('/')[2] === pathname.split('/')[2]);
      if (candidates.length === 1) destination = candidates[0].canonical;
    }
    return (destination || pathname) + u.search + u.hash;
  }
  for (const d of docs) {
    let body = d.body;
    body = body.replace(/\{\{\s*['"]([^'"]+)['"]\s*\|\s*(?:relative_url|absolute_url)\s*\}\}/g, (_, v) => '/'+subject+v);
    body = body.replace(/\{%\s*(?:raw|endraw)\s*%\}/g, '');
    // Rewrite destinations, not prose, math or fenced code examples.
    const blocks = body.split(/(^```[^\n]*\n[\s\S]*?^```[^\n]*$)/gm);
    body = blocks.map((block, n) => {
      if (n % 2) {
        // Timeline's colon separates events; use an equivalent hour notation in labels.
        if (block.startsWith('```mermaid') && block.includes('\ntimeline\n')) return block.replace(/(\d{2}):(\d{2})/g, '$1h$2');
        return block;
      }
      block = block.replace(/(!?\[[^\]\n]*\]\()([^\s)]+)([^\n]*?\))/g, (_, a, v, b) => a+url(v,d)+b);
      block = block.replace(/((?:href|src)=["'])([^"']+)(["'])/g, (_, a, v, b) => a+url(v,d)+b);
      block = block.replace(/^(\s*\[[^\]]+\]:\s*)(\S+)/gm, (_, a, v) => a+url(v,d));
      const callouts = { note:['note','Nota'], important:['caution','Importante'], warning:['danger','Atención'], enunciado:['note','Enunciado'], resolucion:['tip','Resolución'] };
      block = block.replace(/^\{: \.(\w+)\s*\}\s*\n((?:>[^\n]*(?:\n|$))+)/gm, (all, name, quote) => {
        if (!callouts[name]) return all;
        const [type,title] = callouts[name];
        return `:::${type}[${title}]\n${quote.replace(/^> ?/gm, '').trimEnd()}\n:::\n`;
      });
      return block.replace(/\{:\s*[^}]+\}/g, '');
    }).join('');
    // MathJax accepted same-line display delimiters; remark-math requires separate lines.
    body = body.replace(/\$\$([\s\S]*?)\$\$/g, (_, math) => '\n\n$$\n'+math.trim()+'\n$$\n\n');
    body = body.replaceAll('$\\$20$', '$\\text{\\char36}20$');
    if (subject === 'bbdd-aplicadas' && d.rel === 'unidad-2/teoria/unidad-2.md') body = body.replace('**El problema sin aislamiento**', '<a id="el-problema-sin-aislamiento"></a>\n\n**El problema sin aislamiento**');
    // The first academic H1 becomes Starlight's page title; retain its wording.
    let title = d.data.title;
    body = body.replace(/^# ([^\n]+)\n/m, (_, t) => { title = t; return ''; });
    const front = { title, slug: d.canonical.slice(1,-1), sidebar: { order: d.data.nav_order ?? 100 } };
    if (d.rel === 'index.md') front.sidebar.label = titles[i];
    const output = 'src/content/docs/'+subject+'/'+d.rel;
    save(output, '---\n'+YAML.stringify(front)+'---\n'+body);
    pages.push({ source: subject+'/'+d.rel, output, originalSha256: hash(d.text), migratedSha256: hash(fs.readFileSync(output)), canonical: d.canonical });
    if (d.old.endsWith('.html') && !d.old.endsWith('/index.html')) {
      save('public'+d.old, `<!doctype html><html lang="es"><meta charset="utf-8"><title>Página trasladada</title><link rel="canonical" href="https://unlam-informatica.github.io${d.canonical}"><meta http-equiv="refresh" content="0;url=${d.canonical}"><script>location.replace(${JSON.stringify(d.canonical)}+location.search+location.hash)</script><a href="${d.canonical}">Continuar al apunte</a></html>`);
    }
  }
  for (const p of files.filter(p => !p.endsWith('.md') && !/\.(?:scss|yml|html|js)$/.test(p) && !['Gemfile','Gemfile.lock'].includes(path.basename(p)))) {
    const rel = path.relative(dir,p);
    const output = 'public/'+subject+'/'+rel;
    save(output, fs.readFileSync(p));
    assets.push({ source: subject+'/'+rel, output, sha256: hash(fs.readFileSync(p)) });
    matrix.push({ source: subject+'/'+rel, old: '/'+subject+'/'+rel, canonical: '/'+subject+'/'+rel, kind:'asset' });
  }
  provenance.push({ repository: 'unlam-informatica/'+subject, commit: execFileSync('git',['-C',dir,'rev-parse','HEAD'], {encoding:'utf8'}).trim(), pages: docs.length });
}
save('migration/sources.json', JSON.stringify({ repositories: provenance, pages, assets },null,2)+'\n');
save('migration/compatibility.json', JSON.stringify(matrix,null,2)+'\n');
save('migration/compatibility.md', '# Matriz de compatibilidad\n\nLas rutas sin barra final se sirven mediante la normalización de directorios de GitHub Pages. Las rutas `.html` tienen redirección estática conservando query y fragmento.\n\n| Ruta anterior | Ruta unificada | Tipo |\n|---|---|---|\n'+matrix.map(r => `| \`${r.old}\` | \`${r.canonical}\` | ${r.kind} |`).join('\n')+'\n');
console.log(provenance);
