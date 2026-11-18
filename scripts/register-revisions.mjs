// Registers deliberate academic revisions of migrated pages in migration/revisions.json.
// sources.json is never modified: each revision chains the previous hash (from) to the current one (to).
// Usage: node scripts/register-revisions.mjs --prefix src/content/docs/<materia>/ --stage E3 \
//          --reason "Motivo" [--plan ruta/al/plan.md] [--dry-run]
import fs from 'node:fs';
import { createHash } from 'node:crypto';

const args = process.argv.slice(2);
const option = name => { const i = args.indexOf(name); return i >= 0 ? args[i + 1] : undefined; };
const prefix = option('--prefix');
const stage = option('--stage');
const reason = option('--reason');
const plan = option('--plan');
const dryRun = args.includes('--dry-run');
// A single subject per run: src/content/docs/<materia>/ (never the whole docs tree).
if (!prefix || !/^src\/content\/docs\/[^/]+\/$/.test(prefix) || !stage || !reason) {
  console.error('Uso: --prefix src/content/docs/<materia>/ --stage <etapa> --reason "<motivo>" [--plan <archivo>] [--dry-run]');
  process.exit(2);
}

const sources = JSON.parse(fs.readFileSync('migration/sources.json', 'utf8'));
const ledgerPath = 'migration/revisions.json';
const ledger = JSON.parse(fs.readFileSync(ledgerPath, 'utf8'));
const head = new Map();
for (const page of sources.pages) for (const output of [page, ...(page.additionalOutputs || [])]) head.set(output.output, output.migratedSha256);
for (const r of ledger.revisions) {
  if (head.get(r.output) !== r.from) { console.error(`Cadena rota en ${r.output}: revisá ${ledgerPath}`); process.exit(1); }
  head.set(r.output, r.to);
}

const date = new Date().toISOString().slice(0, 10);
const added = [];
for (const [output, expected] of head) {
  if (!output.startsWith(prefix) || !fs.existsSync(output)) continue;
  const current = createHash('sha256').update(fs.readFileSync(output)).digest('hex');
  if (current === expected) continue;
  added.push({ output, from: expected, to: current, date, stage, reason, ...(plan ? { plan } : {}) });
}
if (!dryRun && added.length) {
  ledger.revisions.push(...added);
  fs.writeFileSync(ledgerPath, JSON.stringify(ledger, null, 2) + '\n');
}
console.log(JSON.stringify({ prefix, stage, registered: added.length, dryRun, outputs: added.map(r => r.output) }, null, 2));
