// Protocolo de comprobación de los comandos de GeoGebra citados en los apuntes de AM I.
//
// Abre GeoGebra Clásico (distribución oficial, https://www.geogebra.org/apps/deployggb.js) en Chromium con la
// interfaz en español y escribe cada comando de `casos.json` en la barra de entrada, como lo haría un estudiante:
// el texto se pega en el campo «Entrada…» y se confirma con Enter. Luego lee los objetos nuevos con la API del
// applet y compara con el resultado esperado.
//
// No se usa `evalCommand` de la API porque solo acepta los nombres internos en inglés (Root, Derivative…): no
// comprobaría la sintaxis en español que usan los apuntes.
//
// Requisitos: dependencias del repositorio instaladas (Playwright con Chromium) y acceso a geogebra.org.
// Uso, desde la raíz del repositorio:
//   node academic-sources/analisis-matematico-i/geogebra/ejecutar.mjs
// Resultado: geogebra/resultado.json (detalle) y un resumen por consola. Termina con código 1 si algún caso falla.
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const dir = path.dirname(fileURLToPath(import.meta.url));
const casos = JSON.parse(fs.readFileSync(path.join(dir, 'casos.json'), 'utf8'));
const TOL = 1e-3;

function cumple(espera, nuevos) {
  if (espera.nada) return nuevos.length === 0;
  if (!nuevos.length) return false;
  const v = nuevos[0];
  if (espera.tipo && v.type !== espera.tipo) return false;
  if (espera.valor && v.val !== espera.valor) return false;
  if (espera.contiene && !nuevos.some((n) => (n.val || '').includes(espera.contiene))) return false;
  if (espera.valor_texto && !(v.val || '').endsWith('= ' + espera.valor_texto)) return false;
  if (espera.numero !== undefined && !(v.num !== null && Math.abs(v.num - espera.numero) < TOL)) return false;
  if (espera.punto && !(Math.abs(v.x - espera.punto[0]) < TOL && Math.abs(v.y - espera.punto[1]) < TOL)) return false;
  if (espera.puntos) {
    const pts = nuevos.filter((n) => n.type === 'point');
    if (pts.length !== espera.puntos.length) return false;
    for (const [px, py] of espera.puntos) {
      if (!pts.some((n) => Math.abs(n.x - px) < TOL && Math.abs(n.y - py) < TOL)) return false;
    }
  }
  return true;
}

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1100, height: 750 } });
await page.goto('file://' + path.join(dir, 'applet.html'));
await page.waitForFunction(() => window.ready === true, null, { timeout: 120000 });
await page.waitForTimeout(8000); // carga diferida del CAS (Límite, Derivada, Taylor)

const resultados = [];
for (const caso of casos) {
  const antes = await page.evaluate(() => window.api.getAllObjectNames());
  await page.locator('.avInputItem').last().click();
  await page.waitForTimeout(300);
  await page.evaluate((txt) => {
    const dt = new DataTransfer();
    dt.setData('text/plain', txt);
    document.activeElement.dispatchEvent(new ClipboardEvent('paste', { clipboardData: dt, bubbles: true, cancelable: true }));
  }, caso.cmd);
  await page.waitForTimeout(300);
  await page.keyboard.press('Enter');
  await page.waitForTimeout(2500);
  const nuevos = await page.evaluate((antes) => {
    const api = window.api;
    const g = (fn) => { try { return fn(); } catch { return null; } };
    return api.getAllObjectNames().filter((n) => !antes.includes(n)).map((l) => {
      const type = g(() => api.getObjectType(l));
      return {
        l, type, val: g(() => api.getValueString(l, false)),
        num: type === 'numeric' ? g(() => api.getValue(l)) : null,
        x: type === 'point' ? g(() => api.getXcoord(l)) : null,
        y: type === 'point' ? g(() => api.getYcoord(l)) : null,
      };
    });
  }, antes);
  await page.keyboard.press('Escape');
  resultados.push({ ...caso, obtenido: nuevos, ok: cumple(caso.espera, nuevos) });
}
const version = await page.evaluate(() => window.api.getVersion());
await browser.close();

const fecha = new Date().toISOString().slice(0, 10);
fs.writeFileSync(path.join(dir, 'resultado.json'), JSON.stringify({ fecha, version, resultados }, null, 1) + '\n');
const fallas = resultados.filter((r) => !r.ok);
console.log(`GeoGebra ${version}: ${resultados.length - fallas.length}/${resultados.length} casos como se esperaba`);
for (const r of fallas) console.log('FALLA', r.cmd, '→', JSON.stringify(r.obtenido.map((n) => n.val)));
process.exit(fallas.length ? 1 : 0);
