import { test, expect } from '@playwright/test';

const page_ = '/algebra-ii/unidad-1/teoria/subespacios/';

test('las barras laterales se ocultan con botones y atajos, y el estado se recuerda', async ({ page, isMobile }) => {
  test.skip(isMobile, 'En móvil el menú es un panel desplegable y no hay barras laterales fijas.');
  await page.setViewportSize({ width: 1440, height: 900 });
  await page.goto(page_);
  const left = page.locator('[data-slot="layout"] .aside');
  const toc = page.locator('[data-slot="docs"] > .toc');
  const leftButton = page.locator('[data-sidebar-toggle="left"]');
  const rightButton = page.locator('[data-sidebar-toggle="right"]');
  await expect(left).toBeVisible();
  await expect(toc).toBeVisible();
  const widthBefore = await page.locator('.sl-markdown-content').evaluate(e => e.getBoundingClientRect().left);

  await leftButton.click();
  await expect(left).toBeHidden();
  await expect(leftButton).toHaveAttribute('aria-pressed', 'true');
  await expect(leftButton).toHaveAttribute('title', /^Mostrar el menú/);
  expect(await page.locator('.sl-markdown-content').evaluate(e => e.getBoundingClientRect().left)).not.toBe(widthBefore);

  await page.keyboard.press('ControlOrMeta+Period');
  await expect(left).toBeVisible();
  await expect(leftButton).toHaveAttribute('aria-pressed', 'false');

  await page.keyboard.press('ControlOrMeta+Shift+Period');
  await expect(toc).toBeHidden();
  await expect(rightButton).toHaveAttribute('aria-pressed', 'true');

  // El estado se conserva al navegar a otra página y al recargar.
  await page.keyboard.press('ControlOrMeta+Period');
  await page.locator('a[rel="next"]').click();
  await expect(left).toBeHidden();
  await expect(page.locator('[data-slot="docs"] > .toc')).toBeHidden();
  await page.reload();
  await expect(page.locator('[data-slot="layout"] .aside')).toBeHidden();
  await rightButton.click();
  await leftButton.click();
  await expect(page.locator('[data-slot="layout"] .aside')).toBeVisible();
  await expect(page.locator('[data-slot="docs"] > .toc')).toBeVisible();
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1)).toBeTruthy();
});

test('en pantallas angostas los botones no aparecen y el atajo no cambia nada', async ({ page }) => {
  await page.setViewportSize({ width: 800, height: 900 });
  await page.goto(page_);
  await expect(page.locator('[data-sidebar-toggle="left"]')).toBeHidden();
  await page.keyboard.press('ControlOrMeta+Period');
  expect(await page.evaluate(() => document.documentElement.dataset.sidebarLeft)).toBeUndefined();
});

test('el índice muestra las fórmulas de los títulos renderizadas', async ({ page, isMobile }) => {
  test.skip(isMobile, 'El índice lateral solo se muestra en pantallas anchas.');
  await page.setViewportSize({ width: 1440, height: 900 });
  await page.goto(page_);
  const toc = page.locator('starlight-toc');
  const item = toc.locator('a[href^="#ejemplo-4"]');
  await expect(item.locator('.katex')).toBeVisible();
  // La parte visual de KaTeX muestra la fórmula, no su código (la anotación LaTeX es solo para accesibilidad).
  await expect(item.locator('.katex-html')).toHaveText(/^P\s*2\S*\[R\]$/);
  await expect(item.locator('.katex-error')).toHaveCount(0);
  await expect(toc).not.toContainText('⟦');
  // El título conserva su fórmula y la copia oculta no se ve.
  const heading = page.locator('h3[id^="ejemplo-4"]');
  await expect(heading.locator('.katex')).toBeVisible();
  await expect(heading.locator('.heading-math-source')).toBeHidden();
  // El resaltado de la sección actual sigue funcionando.
  await item.click();
  await expect(item).toHaveAttribute('aria-current', 'true');
});
