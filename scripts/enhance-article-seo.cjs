const fs = require("node:fs");
const path = require("node:path");

const articlesDir = path.join(process.cwd(), "articles");
const files = fs.readdirSync(articlesDir).filter((file) => file.endsWith(".html"));

function escapeJson(value) {
    return value.replace(/\s+/g, " ").trim();
}

function stripHtml(value) {
    return value.replace(/<[^>]*>/g, " ").replace(/&nbsp;/g, " ").replace(/&amp;/g, "&").replace(/&#39;/g, "'").replace(/\s+/g, " ").trim();
}

for (const file of files) {
    const fullPath = path.join(articlesDir, file);
    let html = fs.readFileSync(fullPath, "utf8");
    const title = html.match(/<title>([\s\S]*?)<\/title>/i)?.[1];
    const description = html.match(/<meta\s+name="description"\s+content="([^"]*)"/i)?.[1];
    if (!title || !description) continue;

    const canonical = `https://mandatmaster.fr/articles/${file.replace(/\.html$/, "")}`;
    if (!/<link\s+rel="canonical"/i.test(html)) {
        html = html.replace(
            /(<meta\s+name="description"[^>]*>)/i,
            `$1\n    <link rel="canonical" href="${canonical}">`
        );
    }

    if (!/<meta\s+property="og:title"/i.test(html)) {
        const social = `
    <meta property="og:title" content="${title.replaceAll('"', "&quot;")}">
    <meta property="og:description" content="${description.replaceAll('"', "&quot;")}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="${canonical}">
    <meta property="og:image" content="https://mandatmaster.fr/og-image.png">
    <meta property="og:locale" content="fr_FR">`;
        html = html.replace(/(<link\s+rel="canonical"[^>]*>)/i, `$1${social}`);
    } else if (!/<meta\s+property="og:image"/i.test(html)) {
        html = html.replace(
            /(<meta\s+property="og:url"[^>]*>)/i,
            `$1\n    <meta property="og:image" content="https://mandatmaster.fr/og-image.png">`
        );
    }

    if (!/<script\s+type="application\/ld\+json"/i.test(html)) {
        const schema = {
            "@context": "https://schema.org",
            "@type": "Article",
            headline: escapeJson(title.replace(/\s*\|\s*MandatMaster\s*$/i, "")),
            description: escapeJson(description),
            mainEntityOfPage: canonical,
            inLanguage: "fr-FR",
            author: { "@type": "Organization", name: "MandatMaster" },
            publisher: { "@type": "Organization", name: "MandatMaster", url: "https://mandatmaster.fr/" },
        };
        html = html.replace(
            "</head>",
            `    <script type="application/ld+json">\n${JSON.stringify(schema, null, 2)}\n    </script>\n</head>`
        );
    }

    const h1 = html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/i)?.[1];
    const pageName = stripHtml(h1 || title.replace(/\s*\|\s*MandatMaster\s*$/i, ""));

    if (!/BreadcrumbList/i.test(html)) {
        const breadcrumbSchema = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            itemListElement: [
                { "@type": "ListItem", position: 1, name: "Accueil", item: "https://mandatmaster.fr/" },
                { "@type": "ListItem", position: 2, name: pageName, item: canonical },
            ],
        };
        html = html.replace(
            "</head>",
            `    <script type="application/ld+json">\n${JSON.stringify(breadcrumbSchema, null, 2)}\n    </script>\n</head>`
        );
    }

    if (!/aria-label="Fil d’Ariane"/i.test(html)) {
        const breadcrumb = `\n    <nav aria-label="Fil d’Ariane" class="bg-white border-b border-gray-100">\n        <ol class="container mx-auto px-6 py-3 flex items-center gap-2 text-sm text-gray-500">\n            <li><a href="../index.html" class="hover:text-primary transition">Accueil</a></li>\n            <li aria-hidden="true">/</li>\n            <li class="text-gray-700 truncate" aria-current="page">${pageName}</li>\n        </ol>\n    </nav>`;
        html = html.replace(/(<\/nav>)/i, `$1${breadcrumb}`);
    }

    html = html.replace(/<a\b([^>]*href="https:\/\/www\.amazon\.fr[^"]*"[^>]*)>/gi, (match, attrs) => {
        if (/\brel="/i.test(attrs)) {
            return `<a${attrs.replace(/\brel="([^"]*)"/i, (_, rel) => {
                const values = new Set(rel.split(/\s+/).filter(Boolean));
                values.add("noopener");
                values.add("sponsored");
                return `rel="${[...values].join(" ")}"`;
            })}>`;
        }
        return `<a${attrs} rel="noopener sponsored">`;
    });

    fs.writeFileSync(fullPath, html);
}

console.log(`SEO harmonisé sur ${files.length} articles.`);
