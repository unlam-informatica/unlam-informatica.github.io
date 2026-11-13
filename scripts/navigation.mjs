// Keep canonical/legacy directory URLs, but navigate to actual files. GitHub Pages
// can cache a project site's 404 independently of the unified portal's index.html.
export const navigationPath = canonical => canonical === '/' ? '/' : canonical + 'index.html';

export function navigationHref(value, base, routes) {
  if (!value || value.startsWith('#') || value.startsWith('?')) return value;
  let url;
  try { url = new URL(value, base); } catch { return value; }
  if (url.origin !== base.origin) return value;
  const destination = routes.get(decodeURI(url.pathname));
  return destination ? destination + url.search + url.hash : value;
}
