const fs = require('node:fs');
const path = require('node:path');

const root = path.resolve(__dirname, '..');
const pages = fs.readdirSync(root).filter(f => f.endsWith('.html'))
  .concat(fs.readdirSync(path.join(root, 'articles')).filter(f => f.endsWith('.html')).map(f => `articles/${f}`));
const issues = [];
const canonicals = new Map();

function get(html, re) { return html.match(re)?.[1]?.replace(/\s+/g, ' ').trim() || ''; }

for (const file of pages) {
  const html = fs.readFileSync(path.join(root, file), 'utf8');
  const title = get(html, /<title>([\s\S]*?)<\/title>/i);
  const description = get(html, /<meta\s+name="description"\s+content="([^"]*)"/i);
  const canonical = get(html, /<link\s+rel="canonical"\s+href="([^"]*)"/i);
  if (!title) issues.push(`${file}: title manquant`);
  if (!description) issues.push(`${file}: description manquante`);
  if (!canonical) issues.push(`${file}: canonical manquante`);
  if (title.length > 70) issues.push(`${file}: title trop long (${title.length})`);
  if (description && (description.length < 70 || description.length > 170)) issues.push(`${file}: description à revoir (${description.length})`);
  if ((html.match(/<h1\b/gi) || []).length !== 1) issues.push(`${file}: nombre de H1 incorrect`);
  if (/canonical[^>]+\.html/i.test(html)) issues.push(`${file}: canonical avec .html`);
  if (canonical && canonicals.has(canonical)) issues.push(`${file}: canonical dupliquée avec ${canonicals.get(canonical)}`);
  canonicals.set(canonical, file);
  for (const match of html.matchAll(/<script[^>]+type="application\/ld\+json"[^>]*>([\s\S]*?)<\/script>/gi)) {
    try { JSON.parse(match[1]); } catch (error) { issues.push(`${file}: JSON-LD invalide (${error.message})`); }
  }
  for (const match of html.matchAll(/href="([^"]+)"/g)) {
    const href = match[1];
    if (/^(https?:|mailto:|tel:|#)/.test(href)) continue;
    const clean = href.split(/[?#]/)[0];
    if (!clean) continue;
    const target = clean.startsWith('/') ? path.join(root, clean) : path.resolve(path.dirname(path.join(root, file)), clean);
    if (![target, `${target}.html`, path.join(target, 'index.html')].some(fs.existsSync)) issues.push(`${file}: lien cassé ${href}`);
  }
}

if (issues.length) {
  console.error(`Audit SEO échoué (${issues.length} problème(s)):\n- ${issues.join('\n- ')}`);
  process.exit(1);
}
console.log(`Audit SEO réussi : ${pages.length} pages, canonicals, H1, métadonnées, JSON-LD et liens internes valides.`);
