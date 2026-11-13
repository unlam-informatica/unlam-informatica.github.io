import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import lucode from 'lucode-starlight';
import { unified } from '@astrojs/markdown-remark';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import mathCompat from './scripts/remark-math-compat.mjs';
import mermaidBlocks from './scripts/remark-mermaid.mjs';
export default defineConfig({
  site: 'https://unlam-informatica.github.io',
  trailingSlash: 'always',
  markdown: { processor: unified({ remarkPlugins: [remarkMath, mathCompat, mermaidBlocks], rehypePlugins: [[rehypeKatex, { strict: false }]] }) },
  integrations: [starlight({
    title: 'Apuntes UNLaM',
    plugins: [lucode({
      navLinks: [
        { label: 'Inicio', link: '/' },
        { label: 'Análisis I', link: '/analisis-matematico-i/' },
        { label: 'BBDD', link: '/bbdd-aplicadas/' },
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
    components: { Footer: './src/components/Footer.astro' },
    sidebar: [
      { label: 'Inicio', link: '/' },
      { label: '1er año · Análisis Matemático I', items: [{ autogenerate: { directory: 'analisis-matematico-i', collapsed: true } }], collapsed: true },
      { label: '2do año · BBDD Aplicadas', items: [{ autogenerate: { directory: 'bbdd-aplicadas', collapsed: true } }], collapsed: true },
      { label: '3er año · Diseño de Software', items: [{ autogenerate: { directory: 'diseno-de-software', collapsed: true } }], collapsed: true },
    ],
  })],
});
