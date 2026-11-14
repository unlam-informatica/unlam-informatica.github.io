// Use Starlight groups for the course structure and autogenerate only the actual
// notes. Folder names and legacy Just the Docs navigation pages are not labels.
const unitNumbers = count => Array.from({ length: count }, (_, index) => index + 1);
const notes = (label, directory) => ({
  label,
  collapsed: true,
  items: [{ autogenerate: { directory } }],
});

export const sidebar = [
  { label: 'Inicio', link: '/' },
  {
    label: '1er año · Análisis Matemático I',
    collapsed: true,
    items: [
      { slug: 'analisis-matematico-i', label: 'Presentación' },
      ...unitNumbers(4).map(number => ({
        label: `Unidad ${number}`,
        collapsed: true,
        items: [
          { slug: `analisis-matematico-i/unidad-${number}`, label: 'Presentación' },
          { slug: `analisis-matematico-i/unidad-${number}/teoria/unidad-${number}`, label: 'Teoría' },
          notes('Práctica', `analisis-matematico-i/unidad-${number}/practica`),
        ],
      })),
      notes('GeoGebra', 'analisis-matematico-i/geogebra'),
    ],
  },
  {
    label: '2do año · BBDD Aplicadas',
    collapsed: true,
    items: [
      { slug: 'bbdd-aplicadas', label: 'Presentación' },
      ...unitNumbers(6).map(number => ({
        label: `Unidad ${number}`,
        collapsed: true,
        items: [
          notes('Teoría', `bbdd-aplicadas/unidad-${number}/teoria`),
          notes('Práctica', `bbdd-aplicadas/unidad-${number}/practica`),
        ],
      })),
    ],
  },
  {
    label: '3er año · Diseño de Software',
    collapsed: true,
    items: [
      { slug: 'diseno-de-software', label: 'Presentación' },
      ...unitNumbers(6).map(number => ({
        label: `Unidad ${number}`,
        collapsed: true,
        items: [
          { slug: `diseno-de-software/unidad-${number}`, label: 'Presentación' },
          { slug: `diseno-de-software/unidad-${number}/teoria`, label: 'Teoría' },
          { slug: `diseno-de-software/unidad-${number}/resumen`, label: 'Resumen' },
        ],
      })),
      notes('Prácticas', 'diseno-de-software/practicas'),
      { slug: 'diseno-de-software/diagramas', label: 'Diagramas' },
    ],
  },
];
