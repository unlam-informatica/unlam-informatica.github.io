import { visit } from 'unist-util-visit';
export default function mathCompat() {
  return tree => visit(tree, ['inlineMath', 'math'], node => {
    // Kramdown escaped table pipes survive remark's math tokenizer.
    node.value = node.value.replace(/\\begin\{array\}\{([^}]+)\}/g, (_, spec) => `\\begin{array}{${spec.replaceAll('\\|', '|')}}`);
    if (node.data?.hChildren?.[0]) node.data.hChildren[0].value = node.value;
  });
}
