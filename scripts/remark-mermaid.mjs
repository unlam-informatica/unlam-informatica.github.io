import { visit } from 'unist-util-visit';
// Starlight has no native Mermaid renderer. Keep diagram sources editable in Markdown.
export default function mermaidBlocks() {
  return (tree) => visit(tree, 'code', (node) => {
    if (node.lang !== 'mermaid') return;
    node.type = 'html';
    node.value = `<pre class="mermaid">${node.value.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')}</pre>`;
  });
}
