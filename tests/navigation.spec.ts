import { test, expect } from '@playwright/test';

test('portada por año y navegación contextual', async ({ page, isMobile }, testInfo) => {
  await page.goto('/');
  await page.screenshot({ path: testInfo.outputPath('portada.png'), fullPage: true, animations: 'disabled' });
  await testInfo.attach('Portada Lucode', { path: testInfo.outputPath('portada.png'), contentType: 'image/png' });
  for (const name of ['1er año','2do año','3er año']) await expect(page.getByRole('heading', { name, exact: true })).toBeVisible();
  await expect(page.getByText('Este sitio no es oficial', { exact: false })).toBeVisible();
  await page.locator('.sl-markdown-content a[href="/analisis-matematico-i/index.html"]').first().click();
  await expect(page).toHaveURL(/analisis-matematico-i\/index\.html$/);
  await page.locator('.sl-markdown-content a[href="/analisis-matematico-i/unidad-1/index.html"]').first().click();
  await expect(page).toHaveURL(/unidad-1\/index\.html$/);
  if (isMobile) {
    await page.getByRole('button', { name: 'Toggle Menu', exact: true }).click();
    await expect(page.locator('#drawer')).toBeVisible();
    await page.locator('#drawer a[href="/bbdd-aplicadas/index.html"]').first().click();
    await expect(page).toHaveURL(/bbdd-aplicadas\/index\.html$/);
  }
});

test('fórmulas, diagramas y desborde móvil', async ({ page }) => {
  for (const route of ['/', '/analisis-matematico-i/unidad-1/practica/ejercicio-1/', '/bbdd-aplicadas/unidad-1/teoria/conceptos-basicos/', '/diseno-de-software/unidad-3/teoria/']) {
    await page.goto(route);
    if (route.includes('ejercicio-1')) await expect(page.locator('.katex').first()).toBeVisible();
    if (route.includes('diseno-de-software')) await expect(page.locator('.mermaid svg').first()).toBeVisible({ timeout: 30000 });
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1)).toBeTruthy();
  }
});

test('búsqueda global', async ({ page }) => {
  for (const [term, subject] of [['derivada', 'analisis-matematico-i'], ['transacciones', 'bbdd-aplicadas'], ['patrones', 'diseno-de-software']]) {
    await page.goto('/');
    await page.getByRole('button', { name: 'Buscar', exact: true }).click();
    const input = page.locator('.pagefind-ui__search-input');
    await input.fill(term);
    await expect(page.locator('.pagefind-ui__result').first()).toBeVisible();
    await expect(page.locator('.pagefind-ui__result-link').first()).toHaveAttribute('href', new RegExp(subject));
    await expect(page.locator('.pagefind-ui__result-link').first()).toHaveAttribute('href', /\/index\.html(?:#.*)?$/);
    await page.locator('.pagefind-ui__result-link').first().click();
    await expect(page.locator('h1').first()).not.toHaveText('404');
    await expect(page.locator('meta[name="generator"][content^="Starlight"]')).toHaveCount(1);
  }
});

test('redirecciones conservan fragmentos y consultas', async ({ page }) => {
  await page.goto('/diseno-de-software/diagramas.html?origen=legacy#uml');
  await expect(page).toHaveURL('/diseno-de-software/diagramas/index.html?origen=legacy#uml');
});

test('todos los diagramas Mermaid se renderizan', async ({ page }) => {
  test.setTimeout(180000);
  const { readFileSync, readdirSync } = await import('node:fs');
  const { join } = await import('node:path');
  const walk = (dir: string): string[] => readdirSync(dir, { withFileTypes: true }).flatMap(e => e.isDirectory() ? walk(join(dir,e.name)) : [join(dir,e.name)]);
  const errors: string[] = [];
  page.on('pageerror', error => errors.push(error.message));
  page.on('console', msg => { if (msg.type() === 'error') console.log(page.url(), msg.text()); });
  for (const file of walk('dist').filter(f => f.endsWith('.html'))) {
    const count = (readFileSync(file,'utf8').match(/class="mermaid"/g) || []).length;
    if (!count) continue;
    await page.goto('/'+file.slice(5).replace(/index\.html$/, ''));
    // Mermaid renders sequentially; 31 diagrams can exceed 30s on shared CI runners.
    const renderTimeout = Math.max(30000, count * 3000);
    await expect(page.locator('.mermaid[data-processed="true"] svg'), file).toHaveCount(count, { timeout: renderTimeout });
    await expect.soft(page.getByText('Syntax error in text', { exact: false }), file).toHaveCount(0, { timeout: 500 });
  }
  expect(errors).toEqual([]);
});

test('Lucode conserva el aviso y permite alternar tema claro y oscuro', async ({ page }, testInfo) => {
  await page.goto('/analisis-matematico-i/unidad-1/practica/ejercicio-1/');
  await expect(page.locator('.disclaimer')).toBeVisible();
  await expect(page.locator('[data-slot="docs"]')).toBeVisible();
  const before = await page.locator('html').getAttribute('data-theme');
  await page.locator('starlight-theme-lucode-select button').click();
  await expect(page.locator('html')).toHaveAttribute('data-theme', before === 'dark' ? 'light' : 'dark');
  await page.reload();
  await expect(page.locator('html')).toHaveAttribute('data-theme', before === 'dark' ? 'light' : 'dark');
  await expect(page.locator('.katex').first()).toBeVisible();
  await page.screenshot({ path: testInfo.outputPath('apunte-tema-alternativo.png'), animations: 'disabled' });
  await testInfo.attach('Apunte Lucode', { path: testInfo.outputPath('apunte-tema-alternativo.png'), contentType: 'image/png' });
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1)).toBeTruthy();
});
