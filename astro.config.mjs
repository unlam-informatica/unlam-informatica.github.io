import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import lucode from 'lucode-starlight';
import { unified } from '@astrojs/markdown-remark';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import mathCompat from './scripts/remark-math-compat.mjs';
import mermaidBlocks from './scripts/remark-mermaid.mjs';
import navigationIntegration from './scripts/navigation-integration.mjs';
import { sidebar } from './src/config/sidebar.mjs';
export default defineConfig({
  site: 'https://unlam-informatica.github.io',
  trailingSlash: 'always',
  redirects: Object.fromEntries(Array.from({ length: 6 }, (_, index) => {
    const unit = `/bbdd-aplicadas/unidad-${index + 1}/`;
    return [unit, unit + 'teoria/'];
  })),
  markdown: { processor: unified({ remarkPlugins: [remarkMath, mathCompat, mermaidBlocks], rehypePlugins: [[rehypeKatex, { strict: false }]] }) },
  integrations: [starlight({
    title: 'Apuntes UNLaM',
    // The navigation integration indexes with Pagefind's keepIndexUrl option.
    pagefind: false,
    plugins: [lucode({
      navLinks: [
        { label: 'Inicio', link: '/' },
        { label: 'Análisis Matemático I', link: '/analisis-matematico-i/' },
        { label: 'BBDD Aplicadas', link: '/bbdd-aplicadas/' },
        { label: 'Diseño', link: '/diseno-de-software/' },
      ],
      footerText: 'Sitio personal de apuntes. No es un sitio oficial de la Universidad Nacional de La Matanza (UNLaM).',
      // The Footer wrapper composes Lucode's footer with the notice and local Mermaid loader.
      warnOverrides: false,
    })],
    defaultLocale: 'root', locales: { root: { label: 'Español', lang: 'es' } },
    favicon: '/assets/favicon/favicon.ico',
    social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/unlam-informatica/unlam-informatica.github.io' }],
    customCss: ['katex/dist/katex.min.css', './src/styles/custom.css'],
    components: { Footer: './src/components/Footer.astro', Search: 'lucode-starlight/components/overrides/Search.astro' },
    sidebar,
  }), navigationIntegration()],
});
