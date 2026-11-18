// Texto de búsqueda para las fórmulas KaTeX.
//
// KaTeX deja tres copias de cada fórmula (MathML, anotación LaTeX y HTML visual), y
// Pagefind arma los extractos concatenándolas: «a=0a=0a=0», «\begin{pmatrix}…».
// Antes de indexar, cada fórmula se reemplaza por una sola versión lineal en texto
// plano, derivada del MathML: «A₀=CDC⁻¹», «(a+1)/2», «(0 1; 1 0)», «a≠0».
// Solo se toca la copia que recibe el indexador; el HTML publicado no cambia.

const SUPERSCRIPT = Object.fromEntries([...'0123456789+-−=()nitT'].map((c, i) => [c, '⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁻⁼⁽⁾ⁿⁱᵗᵀ'[i]]));
const SUBSCRIPT = Object.fromEntries([...'0123456789+-−=()aeijknmx'].map((c, i) => [c, '₀₁₂₃₄₅₆₇₈₉₊₋₋₌₍₎ₐₑᵢⱼₖₙₘₓ'[i]]));

// Solo se agregan paréntesis cuando el operando tiene operadores: «15/2», «(a+1)/2».
const group = raw => {
  const text = raw.trim();
  return /[\s+\-−±=<>≤≥≠,;/·×]/.test(text) && !/^\([^()]*\)$/.test(text) ? `(${text})` : text;
};

function script(text, table, marker) {
  const chars = [...text.trim()];
  return chars.length && chars.every(c => c in table) ? chars.map(c => table[c]).join('') : marker + group(text);
}

function linear(node) {
  if (node.type === 'text') return node.data.replace(/[\u2061-\u2064]/g, '');
  if (node.type !== 'tag') return '';
  const kids = node.children.filter(child => child.type === 'tag');
  const all = () => node.children.map(linear).join('');
  const [a, b, c] = kids.map(linear);
  switch (node.name) {
    case 'annotation':
    case 'annotation-xml':
    case 'mphantom':
      return '';
    case 'mspace':
      return ' ';
    case 'mi':
      // Nombres de función (ln, sen, diag) separados del factor anterior: «a ln(x)».
      return [...all()].length > 1 ? ' ' + all() : all();
    case 'mfrac':
      return `${group(a)}/${group(b)}`;
    case 'msqrt':
      return `√${group(all())}`;
    case 'mroot':
      return `${script(b, SUPERSCRIPT, '')}√${group(a)}`;
    case 'msup':
      return a + script(b, SUPERSCRIPT, '^');
    case 'msub':
      return a + script(b, SUBSCRIPT, '_');
    case 'msubsup':
      return a + script(b, SUBSCRIPT, '_') + script(c, SUPERSCRIPT, '^');
    case 'munder':
      return node.attribs.accentunder === 'true' ? a + b : a + script(b, SUBSCRIPT, '_');
    case 'mover':
      return node.attribs.accent === 'true' ? a + b : a + script(b, SUPERSCRIPT, '^');
    case 'munderover':
      return a + script(b, SUBSCRIPT, '_') + script(c, SUPERSCRIPT, '^');
    case 'mtable':
      return kids.map(linear).join('; ');
    case 'mtr':
      return kids.map(linear).join(' ');
    default:
      return all();
  }
}

/** Reemplaza cada fórmula KaTeX del documento por su versión en texto plano. */
export function plainSearchMath($) {
  $('.katex').each((_, element) => {
    const math = $(element).find('.katex-mathml math').get(0);
    const text = math ? linear(math) : $(element).find('annotation').text();
    $(element).replaceWith($('<span>').text(text.replace(/\s+/g, ' ').trim()));
  });
}
