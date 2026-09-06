const fs = require('node:fs');
const path = require('node:path');
const cp = require('node:child_process');

const root = path.resolve(__dirname, '..');
const articlesDir = path.join(root, 'articles');
const today = new Date().toISOString().slice(0, 10);
const site = 'https://mandatmaster.fr';

const categories = {
  prospection: { name: 'Prospection & mandats', description: 'Méthodes, scripts et plans d’action pour trouver des vendeurs et décrocher davantage de mandats.', keywords: ['prospection', 'pige', 'mandat', 'vendeur', 'relance', 'client', 'farming', 'partenariat', 'réseau'] },
  estimation: { name: 'Estimation & négociation', description: 'Guides pratiques pour estimer un bien, défendre son prix, négocier et obtenir un mandat exclusif.', keywords: ['estimation', 'prix', 'négociation', 'commission', 'objection', 'exclusif'] },
  marketing: { name: 'Marketing immobilier', description: 'Développez votre visibilité locale, votre image de marque et la présentation de vos biens immobiliers.', keywords: ['marketing', 'photo', 'vidéo', 'annonce', 'réseaux sociaux', 'site web', 'branding', 'avis google', 'canva', 'home staging'] },
  materiel: { name: 'Matériel de l’agent immobilier', description: 'Sélections et conseils pour choisir les outils et équipements utiles au quotidien sur le terrain.', keywords: ['matériel', 'équipement', 'ordinateur', 'tablette', 'imprimante', 'sacoche', 'télémètre', 'caméra', 'trépied', 'voiture', 'bureau', 'fourniture', 'powerbank', 'ring light', 'casque', 'boîte à clés', 'cartes de visite', 'panneau'] },
  carriere: { name: 'Carrière & organisation', description: 'Statut, formation, organisation et ressources pour développer durablement son activité immobilière.', keywords: ['carrière', 'devenir', 'salaire', 'statut', 'impôt', 'comptabilité', 'organisation', 'stress', 'livre', 'temps partiel', 'première année', 'ia'] }
};

// La page d’accueil est la source de vérité pour le classement éditorial.
const categoryBySlug = {};
const indexSource = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
for (const [sectionId, category] of Object.entries({ prospection: 'prospection', negociation: 'estimation', marketing: 'marketing', materiel: 'materiel', carriere: 'carriere' })) {
  const start = indexSource.search(new RegExp(`<section[^>]+id=["']${sectionId}["']`, 'i'));
  if (start < 0) continue;
  const next = indexSource.slice(start + 1).search(/<section\b/i);
  const section = next < 0 ? indexSource.slice(start) : indexSource.slice(start, start + 1 + next);
  for (const match of section.matchAll(/href=["']\/?articles\/([^"'#?]+?)(?:\.html)?["'#?]/gi)) categoryBySlug[match[1]] = category;
}

const esc = s => s.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const text = s => s.replace(/<script[\s\S]*?<\/script>/gi, ' ').replace(/<style[\s\S]*?<\/style>/gi, ' ').replace(/<[^>]+>/g, ' ').replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&').replace(/&#39;/g, "'").replace(/\s+/g, ' ').trim();
const meta = (html, name) => html.match(new RegExp(`<meta\\s+(?:name|property)=["']${name}["']\\s+content=["']([^"']*)`, 'i'))?.[1] || '';
const titleOf = html => text(html.match(/<title>([\s\S]*?)<\/title>/i)?.[1] || '');
const h1Of = html => text(html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/i)?.[1] || '');
const slugOf = file => path.basename(file, '.html');
const cleanUrl = file => `${site}/articles/${slugOf(file)}`;

function categoryFor(html, file) {
  if (categoryBySlug[slugOf(file)]) return categoryBySlug[slugOf(file)];
  const haystack = `${file} ${titleOf(html)} ${h1Of(html)} ${text(html).slice(0, 1000)}`.toLowerCase();
  let best = 'carriere', score = -1;
  for (const [slug, c] of Object.entries(categories)) {
    const current = c.keywords.reduce((n, keyword) => n + (haystack.includes(keyword) ? 1 : 0), 0);
    if (current > score) { best = slug; score = current; }
  }
  return best;
}

function gitDate(file, first = false) {
  try {
    const args = first ? 'git log --follow --diff-filter=A --format=%cs --' : 'git log -1 --format=%cs --';
    const dates = cp.execSync(`${args} ${JSON.stringify(path.relative(root, file))}`, { cwd: root, encoding: 'utf8' }).trim().split(/\s+/).filter(Boolean);
    return first ? dates.at(-1) || today : dates[0] || today;
  } catch { return today; }
}

function conciseTitle(value) {
  let out = value.replace(/\s*\|\s*MandatMaster\s*$/i, '').trim();
  if (out.length <= 62) return out;
  const cut = out.slice(0, 63);
  const boundary = Math.max(cut.lastIndexOf(' : '), cut.lastIndexOf(' — '), cut.lastIndexOf(' - '));
  if (boundary >= 38) out = cut.slice(0, boundary);
  else out = cut.slice(0, cut.lastIndexOf(' '));
  if ((out.match(/\(/g) || []).length > (out.match(/\)/g) || []).length) out = out.slice(0, out.lastIndexOf('('));
  return out.replace(/[,:;\-–—]+$/, '').trim();
}

function goodDescription(html, existing) {
  let out = text(existing);
  if (out.length < 110) {
    const main = html.match(/<main[\s\S]*?<p[^>]*>([\s\S]*?)<\/p>/i)?.[1] || html.match(/<header[\s\S]*?<p[^>]*>([\s\S]*?)<\/p>/i)?.[1] || '';
    const lead = text(main).replace(/^['“"]|['”"]$/g, '');
    if (lead.length > out.length) out = lead;
  }
  if (out.length > 158) out = out.slice(0, 158).replace(/\s+\S*$/, '').replace(/[,:;\-–—]+$/, '') + '.';
  return out;
}

function upsertMeta(html, attr, key, value) {
  const re = new RegExp(`<meta\\s+${attr}=["']${key}["'][^>]*>`, 'i');
  const tag = `<meta ${attr}="${key}" content="${esc(value)}">`;
  return re.test(html) ? html.replace(re, tag) : html.replace('</head>', `    ${tag}\n</head>`);
}

function articleSchema(html, file, category, title, description) {
  const canonical = cleanUrl(file);
  const published = gitDate(file, true);
  const modified = gitDate(file);
  return {
    '@context': 'https://schema.org', '@type': 'Article', headline: title, description,
    mainEntityOfPage: { '@type': 'WebPage', '@id': canonical }, inLanguage: 'fr-FR',
    image: `${site}/og-image.png`, datePublished: published, dateModified: modified,
    author: { '@type': 'Person', name: 'Nathalie Lebrun', url: `${site}/a-propos` },
    publisher: { '@type': 'Organization', name: 'MandatMaster', url: `${site}/`, logo: { '@type': 'ImageObject', url: `${site}/og-image.png` } },
    articleSection: categories[category].name
  };
}

const files = fs.readdirSync(articlesDir).filter(f => f.endsWith('.html')).sort();
const grouped = Object.fromEntries(Object.keys(categories).map(k => [k, []]));

for (const file of files) {
  const full = path.join(articlesDir, file);
  let html = fs.readFileSync(full, 'utf8');
  const category = categoryFor(html, file);
  const currentTitle = titleOf(html);
  const titleSource = (currentTitle.match(/\(/g) || []).length === (currentTitle.match(/\)/g) || []).length ? currentTitle : h1Of(html);
  const title = conciseTitle(titleSource);
  const socialTitle = title.length > 52 ? title : `${title} | MandatMaster`;
  const description = goodDescription(html, meta(html, 'description'));
  const canonical = cleanUrl(file);
  grouped[category].push({ slug: slugOf(file), title, description });

  html = html.replace(/<title>[\s\S]*?<\/title>/i, `<title>${esc(socialTitle)}</title>`);
  html = upsertMeta(html, 'name', 'description', description);
  html = html.replace(/<link\s+rel=["']canonical["'][^>]*>/i, `<link rel="canonical" href="${canonical}">`);
  html = upsertMeta(html, 'property', 'og:title', socialTitle);
  html = upsertMeta(html, 'property', 'og:description', description);
  html = upsertMeta(html, 'property', 'og:url', canonical);
  html = upsertMeta(html, 'property', 'og:image', `${site}/og-image.png`);
  html = upsertMeta(html, 'name', 'twitter:card', 'summary_large_image');
  html = upsertMeta(html, 'name', 'twitter:title', socialTitle);
  html = upsertMeta(html, 'name', 'twitter:description', description);
  html = upsertMeta(html, 'name', 'twitter:image', `${site}/og-image.png`);

  const scripts = [...html.matchAll(/<script\s+type=["']application\/ld\+json["'][^>]*>[\s\S]*?<\/script>/gi)];
  for (const match of scripts.reverse()) {
    if (/"@type"\s*:\s*"Article"/.test(match[0]) || /"@type"\s*:\s*"BreadcrumbList"/.test(match[0])) html = html.slice(0, match.index) + html.slice(match.index + match[0].length);
  }
  const crumbs = { '@context': 'https://schema.org', '@type': 'BreadcrumbList', itemListElement: [
    { '@type': 'ListItem', position: 1, name: 'Accueil', item: `${site}/` },
    { '@type': 'ListItem', position: 2, name: categories[category].name, item: `${site}/${category}` },
    { '@type': 'ListItem', position: 3, name: title, item: canonical }
  ]};
  html = html.replace('</head>', `    <script type="application/ld+json">\n${JSON.stringify(articleSchema(html, full, category, title, description), null, 2)}\n    </script>\n    <script type="application/ld+json">\n${JSON.stringify(crumbs, null, 2)}\n    </script>\n</head>`);

  html = html.replace(/href=["']\.\.\/index\.html(#[^"']*)?["']/g, (_, hash = '') => `href="/${hash}"`);
  html = html.replace(/href=["']([^"']+)\.html([#?][^"']*)?["']/g, (_, url, suffix = '') => `href="${url}${suffix}"`);
  html = html.replace(/<nav aria-label="Fil d’Ariane"[\s\S]*?<\/nav>/i, `<nav aria-label="Fil d’Ariane" class="bg-white border-b border-gray-100"><ol class="container mx-auto px-6 py-3 flex items-center gap-2 text-sm text-gray-500"><li><a href="/" class="hover:text-primary transition">Accueil</a></li><li aria-hidden="true">/</li><li><a href="/${category}" class="hover:text-primary transition">${categories[category].name}</a></li><li aria-hidden="true">/</li><li class="text-gray-700 truncate" aria-current="page">${esc(title)}</li></ol></nav>`);
  if (!/class="article-meta"/.test(html)) {
    html = html.replace(/(<\/header>)/i, `<div class="article-meta text-center text-sm text-gray-500 mt-6">Par <a href="/a-propos" rel="author" class="font-semibold text-primary hover:underline">Nathalie Lebrun</a> · Mis à jour le <time datetime="${gitDate(full)}">${gitDate(full).split('-').reverse().join('/')}</time></div>\n    $1`);
  }
  html = html.replace(/href=["']\/#[^"']+["']/g, match => match);
  html = html.replace(/href=["'](?:\.\.\/)?index(?:\.html)?#mentions["']/gi, 'href="/mentions-legales"');
  html = html.replace(/[ \t]+$/gm, '');
  fs.writeFileSync(full, html);
}

function shell(title, description, canonical, body) {
  return `<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${esc(title)} | MandatMaster</title><meta name="description" content="${esc(description)}"><link rel="canonical" href="${canonical}"><meta property="og:title" content="${esc(title)} | MandatMaster"><meta property="og:description" content="${esc(description)}"><meta property="og:type" content="website"><meta property="og:url" content="${canonical}"><meta property="og:image" content="${site}/og-image.png"><meta name="twitter:card" content="summary_large_image"><link rel="stylesheet" href="/output.css"></head><body class="bg-white text-dark font-sans leading-relaxed"><nav class="border-b border-gray-200 bg-white sticky top-0 z-50"><div class="container mx-auto px-4 h-16 flex items-center justify-between"><a href="/" class="font-extrabold text-xl text-navy">Mandat<span class="text-primary">Master</span></a><a href="/guides" class="text-sm font-semibold text-primary">Tous les guides</a></div></nav><main class="max-w-4xl mx-auto px-6 py-16">${body}</main><footer class="bg-gray-900 text-gray-400 py-10"><div class="max-w-4xl mx-auto px-6 text-sm flex flex-wrap gap-5"><a href="/mentions-legales">Mentions légales</a><a href="/confidentialite">Confidentialité</a><a href="/a-propos">À propos</a><a href="mailto:contact@mandatmaster.fr">Contact</a></div></footer></body></html>`;
}

for (const [slug, cat] of Object.entries(categories)) {
  const cards = grouped[slug].map(a => `<article class="border border-gray-200 rounded-2xl p-6 hover:shadow-lg transition"><h2 class="text-xl font-bold text-navy mb-2"><a href="/articles/${a.slug}" class="hover:text-primary">${esc(a.title)}</a></h2><p class="text-gray-600">${esc(a.description)}</p></article>`).join('');
  fs.writeFileSync(path.join(root, `${slug}.html`), shell(cat.name, cat.description, `${site}/${slug}`, `<header class="mb-12"><p class="font-bold text-primary uppercase tracking-wider text-sm">Guides MandatMaster</p><h1 class="text-4xl md:text-5xl font-black text-navy mt-3 mb-5">${cat.name}</h1><p class="text-xl text-gray-600">${cat.description}</p></header><section class="grid md:grid-cols-2 gap-6">${cards}</section>`));
}

const allCards = Object.values(grouped).flat().sort((a,b) => a.title.localeCompare(b.title, 'fr')).map(a => `<li><a class="text-primary hover:underline" href="/articles/${a.slug}">${esc(a.title)}</a></li>`).join('');
fs.writeFileSync(path.join(root, 'guides.html'), shell('Tous les guides pour agents immobiliers', 'Retrouvez les 71 guides MandatMaster classés par thème pour développer votre activité immobilière.', `${site}/guides`, `<h1 class="text-4xl md:text-5xl font-black text-navy mb-5">Tous les guides MandatMaster</h1><p class="text-xl text-gray-600 mb-10">71 ressources pratiques pour les agents et mandataires immobiliers indépendants.</p><ul class="grid md:grid-cols-2 gap-4">${allCards}</ul>`));

fs.writeFileSync(path.join(root, 'a-propos.html'), shell('À propos de MandatMaster', 'Découvrez la mission de MandatMaster, son éditrice et la méthode utilisée pour créer ses guides immobiliers.', `${site}/a-propos`, `<h1 class="text-4xl font-black text-navy mb-8">À propos de MandatMaster</h1><div class="prose prose-lg max-w-none space-y-6"><p>MandatMaster est un centre de ressources indépendant destiné aux agents et mandataires immobiliers. Sa mission est de proposer des outils simples, concrets et directement applicables sur le terrain.</p><h2 class="text-2xl font-bold">Éditrice et responsable de publication</h2><p>Le site est édité par <strong>Nathalie Lebrun</strong>, entrepreneure individuelle et directrice de la publication. Les guides sont relus et mis à jour lorsque les pratiques, outils ou règles mentionnés évoluent.</p><h2 class="text-2xl font-bold">Méthode éditoriale</h2><p>Les articles privilégient les exemples pratiques, les sources officielles lorsqu’un sujet touche au droit, à la fiscalité ou au statut professionnel, et la transparence sur les liens commerciaux. Les sélections de produits reposent sur leur utilité pour le métier, leurs caractéristiques et leur rapport qualité-prix. MandatMaster ne reçoit aucune rémunération pour classer un produit.</p><h2 class="text-2xl font-bold">Affiliation</h2><p>Certains liens Amazon sont affiliés. MandatMaster peut percevoir une commission sur un achat, sans surcoût pour le lecteur. Cette rémunération contribue au financement des contenus gratuits.</p><p><a class="text-primary font-semibold" href="mailto:contact@mandatmaster.fr">contact@mandatmaster.fr</a></p></div>`));

fs.writeFileSync(path.join(root, 'mentions-legales.html'), shell('Mentions légales', 'Mentions légales, éditeur, responsable de publication et hébergeur du site MandatMaster.', `${site}/mentions-legales`, `<h1 class="text-4xl font-black text-navy mb-8">Mentions légales</h1><div class="space-y-5 text-gray-700"><p><strong>Éditrice :</strong> Nathalie Lebrun, entrepreneure individuelle — MandatMaster</p><p><strong>Adresse :</strong> 524 rue de la Tourrache, 83600 Fréjus, France</p><p><strong>SIREN :</strong> 101 331 585 — <strong>SIRET :</strong> 101 331 585 00014</p><p><strong>Directrice de la publication :</strong> Nathalie Lebrun</p><p><strong>Contact :</strong> <a class="text-primary" href="mailto:contact@mandatmaster.fr">contact@mandatmaster.fr</a></p><p><strong>Hébergement :</strong> Cloudflare, Inc., 101 Townsend St, San Francisco, CA 94107, États-Unis.</p><p>Le contenu est fourni à titre informatif et ne remplace pas l’avis d’un professionnel du droit, de la fiscalité ou de l’immobilier.</p></div>`));

fs.writeFileSync(path.join(root, 'confidentialite.html'), shell('Politique de confidentialité', 'Politique de confidentialité et informations sur les cookies, la publicité et les données du site MandatMaster.', `${site}/confidentialite`, `<h1 class="text-4xl font-black text-navy mb-8">Politique de confidentialité</h1><div class="prose prose-lg max-w-none space-y-6"><p>MandatMaster ne demande pas d’inscription pour consulter ses guides ou télécharger son kit gratuit. Lorsque vous écrivez par email, vos coordonnées sont utilisées uniquement pour répondre à votre demande.</p><h2 class="text-2xl font-bold">Mesure d’audience et publicité</h2><p>Le site peut utiliser des services de mesure d’audience et Google AdSense. Ces services peuvent déposer des cookies ou traiter des données techniques, sous réserve de votre consentement lorsqu’il est requis.</p><h2 class="text-2xl font-bold">Liens externes et affiliation</h2><p>Certains liens mènent vers Amazon et peuvent être affiliés. Le site tiers applique alors sa propre politique de confidentialité.</p><h2 class="text-2xl font-bold">Vos droits</h2><p>Vous pouvez demander l’accès, la rectification ou la suppression des données transmises directement à MandatMaster en écrivant à <a class="text-primary" href="mailto:contact@mandatmaster.fr">contact@mandatmaster.fr</a>.</p><p>Dernière mise à jour : ${today.split('-').reverse().join('/')}</p></div>`));

let index = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
index = index.replace(/href=["']articles\/([^"']+)\.html([#?][^"']*)?["']/g, 'href="/articles/$1$2"');
index = index.replace(/href="#(prospection|negociation|marketing|materiel|carriere)"/g, (_, s) => `href="/${s === 'negociation' ? 'estimation' : s}"`);
index = index.replace(/<a href="#mentions"[^>]*>Mentions légales<\/a>/i, '<a href="/mentions-legales" class="hover:text-white transition">Mentions légales</a>');
index = index.replace('</footer>', `<div class="max-w-5xl mx-auto px-6 pb-8 flex justify-center flex-wrap gap-5 text-sm text-gray-400"><a href="/guides">Tous les guides</a><a href="/a-propos">À propos</a><a href="/mentions-legales">Mentions légales</a><a href="/confidentialite">Confidentialité</a></div></footer>`);
fs.writeFileSync(path.join(root, 'index.html'), index);

let merci = fs.readFileSync(path.join(root, 'merci.html'), 'utf8').replace(/https:\/\/mandatmaster\.fr\/merci\.html/g, `${site}/merci`).replace(/href=["']index\.html/g, 'href="/');
fs.writeFileSync(path.join(root, 'merci.html'), merci);

const sitemapPages = ['', 'guides', ...Object.keys(categories), 'a-propos', 'mentions-legales', 'confidentialite', ...files.map(f => `articles/${slugOf(f)}`)];
const sitemap = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${sitemapPages.map(p => `  <url><loc>${site}/${p}</loc><lastmod>${today}</lastmod></url>`).join('\n')}\n</urlset>\n`;
fs.writeFileSync(path.join(root, 'sitemap.xml'), sitemap);

fs.writeFileSync(path.join(root, '_headers'), `/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: SAMEORIGIN\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n\n/output.css\n  Cache-Control: public, max-age=604800\n\n/og-image.png\n  Cache-Control: public, max-age=2592000\n`);

const notFound = shell('Page introuvable', 'La page demandée est introuvable. Retrouvez tous les guides MandatMaster.', `${site}/404`, `<div class="text-center py-20"><p class="text-primary font-black text-6xl mb-4">404</p><h1 class="text-4xl font-black text-navy mb-5">Page introuvable</h1><p class="text-gray-600 mb-8">Cette page n’existe plus ou son adresse a changé.</p><a href="/guides" class="inline-block bg-primary text-white font-bold px-7 py-3 rounded-full">Voir tous les guides</a></div>`)
  .replace('</head>', '<meta name="robots" content="noindex,follow"></head>');
fs.writeFileSync(path.join(root, '404.html'), notFound);

console.log(`SEO Cloudflare appliqué à ${files.length} articles et ${Object.keys(categories).length} catégories.`);
