import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
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
    title: 'Apuntes de Informática — UNLaM',
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
