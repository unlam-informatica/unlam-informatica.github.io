// Use Starlight groups for the course structure and autogenerate only the actual
// notes. Folder names and legacy Just the Docs navigation pages are not labels.
//
// `subjects` es la única lista de materias: alimenta el menú lateral (todas las materias,
// en orden alfabético, cada una colapsada salvo la de la página actual) y los menús por año
// del header (src/components/YearMenu.astro). Para sumar una materia, agregarla acá con su
// año y su página de presentación: el orden y los menús se arman solos.
const unitNumbers = count => Array.from({ length: count }, (_, index) => index + 1);
const notes = (label, directory) => ({
  label,
  collapsed: true,
  items: [{ autogenerate: { directory } }],
});

// Bases de Datos Aplicadas: cada unidad abre con su presentación (la ruta de estudio, que vive en
// `teoria/index.md` y se oculta del autogenerado para no duplicarla), sigue con Teoría y Práctica en
// orden pedagógico (`sidebar.order` de cada página) y cierra, cuando existen, con el resumen
// integrador y la guía de repaso. La paginación de Starlight recorre ese mismo orden.
const bbddUnits = [
  { title: 'Conceptos básicos y SQL' },
  { title: 'Relacionales: aspectos básicos' },
  { title: 'Relacionales: aspectos avanzados' },
  { title: 'No relacionales', review: [['apunte-completo', 'Resumen integrador'], ['guia-parcial', 'Guía para el parcial']] },
  { title: 'Protección de los datos', review: [['apunte-completo', 'Resumen integrador'], ['guia-parcial', 'Guía de repaso']] },
  { title: 'Calidad en bases de datos', review: [['apunte-completo', 'Resumen integrador'], ['guia-parcial', 'Guía de repaso']] },
];

export const subjects = [
  {
    year: 1,
    label: 'Análisis Matemático I',
    href: '/analisis-matematico-i/',
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
    year: 2,
    label: 'Bases de Datos Aplicadas',
    href: '/bbdd-aplicadas/',
    items: [
      { slug: 'bbdd-aplicadas', label: 'Presentación' },
      { slug: 'bbdd-aplicadas/como-estudiar', label: 'Cómo estudiar' },
      ...bbddUnits.map(({ title, review = [] }, index) => {
        const unit = `bbdd-aplicadas/unidad-${index + 1}`;
        return {
          label: `Unidad ${index + 1} · ${title}`,
          collapsed: true,
          items: [
            { slug: `${unit}/teoria`, label: 'Presentación y ruta' },
            notes('Teoría', `${unit}/teoria`),
            notes('Práctica', `${unit}/practica`),
            ...review.map(([page, label]) => ({ slug: `${unit}/teoria/${page}`, label })),
          ],
        };
      }),
    ],
  },
  {
    year: 3,
    label: 'Álgebra y Geometría Analítica II',
    href: '/algebra-ii/',
    items: [
      { slug: 'algebra-ii', label: 'Presentación' },
      { slug: 'algebra-ii/programa', label: 'Programa' },
      { slug: 'algebra-ii/como-estudiar', label: 'Cómo estudiar' },
      { slug: 'algebra-ii/notacion', label: 'Notación' },
      { slug: 'algebra-ii/laboratorio', label: 'Laboratorio interactivo' },
      notes('Repaso de Álgebra I', 'algebra-ii/repaso'),
      ...[
        'Espacios vectoriales',
        'Transformaciones lineales',
        'Autovalores y autovectores',
        'Espacios con producto interno',
      ].map((title, index) => ({
        label: `Unidad ${index + 1} · ${title}`,
        collapsed: true,
        items: [
          { slug: `algebra-ii/unidad-${index + 1}`, label: 'Presentación' },
          notes('Teoría', `algebra-ii/unidad-${index + 1}/teoria`),
          notes('Práctica', `algebra-ii/unidad-${index + 1}/practica`),
        ],
      })),
      notes('Integradores y simulacros', 'algebra-ii/integradores'),
      { slug: 'algebra-ii/bibliografia', label: 'Bibliografía' },
    ],
  },
  {
    year: 3,
    label: 'Diseño de Software',
    href: '/diseno-de-software/',
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

export const yearLabels = { 1: '1er año', 2: '2do año', 3: '3er año', 4: '4to año', 5: '5to año' };
export const alphabetical = (a, b) => a.label.localeCompare(b.label, 'es', { sensitivity: 'base' });

/** Años con sus materias en orden alfabético, para los menús del header. */
export const years = [...new Set(subjects.map(subject => subject.year))].sort((a, b) => a - b).map(year => ({
  year,
  label: yearLabels[year] ?? `Año ${year}`,
  subjects: subjects.filter(subject => subject.year === year).sort(alphabetical)
    .map(({ label, href }) => ({ label, href })),
}));

export const sidebar = [
  { label: 'Inicio', link: '/' },
  {
    // Lucode muestra el primer nivel como encabezado fijo: las materias van un nivel más
    // abajo para que cada una se pueda colapsar.
    label: 'Materias',
    items: [...subjects].sort(alphabetical).map(({ label, items }) => ({ label, collapsed: true, items })),
  },
];
