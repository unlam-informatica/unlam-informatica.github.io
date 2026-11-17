import { toHtml } from 'hast-util-to-html';
import { SKIP, visit } from 'unist-util-visit';

// KaTeX deja tres copias de cada fórmula (MathML, anotación LaTeX y HTML visual) y Astro
// arma el texto de los títulos —el del índice y el del ancla— concatenándolas.
// Este plugin corre después de rehype-katex y antes de que Astro recolecte los títulos:
// - reemplaza cada fórmula de un título por un nodo `raw`, que el recolector ignora y
//   `rehype-raw` vuelve a convertir en el mismo HTML (el título se ve igual);
// - agrega una copia oculta del LaTeX entre ⟦ ⟧, que es lo único que recolecta Astro.
// El índice (src/components/TableOfContents.astro) renderiza esos ⟦ ⟧ con KaTeX.
export const MATH_OPEN = '⟦';
export const MATH_CLOSE = '⟧';

const classes = node => [].concat(node.properties?.className ?? []);
const isHeading = node => node.type === 'element' && /^h[1-6]$/.test(node.tagName);

function latexOf(katexNode) {
  let tex = null;
  visit(katexNode, 'element', node => {
    if (node.tagName === 'annotation' && node.properties?.encoding === 'application/x-tex') {
      tex = node.children.map(child => child.value ?? '').join('');
      return false;
    }
  });
  return tex;
}

export default function headingMath() {
  return (tree, file) => {
    // MDX no usa nodos `raw`; ninguna página MDX tiene fórmulas en los títulos.
    if (file.history[0]?.endsWith('.mdx')) return;
    visit(tree, 'element', heading => {
      if (!isHeading(heading)) return;
      visit(heading, 'element', (node, index, parent) => {
        if (!classes(node).includes('katex') || !parent || index === undefined) return;
        const tex = latexOf(node);
        if (tex === null) return SKIP;
        parent.children.splice(index, 1,
          // Sin saltos de línea: el recolector solo ignora un `raw` de una sola línea.
          { type: 'raw', value: toHtml(node).replace(/\n/g, ' ') },
          {
            type: 'element',
            tagName: 'span',
            properties: { hidden: true, dataPagefindIgnore: '', className: ['heading-math-source'] },
            children: [{ type: 'text', value: `${MATH_OPEN}${tex.replace(/\s+/g, ' ').trim()}${MATH_CLOSE}` }],
          });
        return [SKIP, index + 2];
      });
      return SKIP;
    });
  };
}
