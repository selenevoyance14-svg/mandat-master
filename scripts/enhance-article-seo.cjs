const fs = require("node:fs");
const path = require("node:path");

const articlesDir = path.join(process.cwd(), "articles");
const files = fs.readdirSync(articlesDir).filter((file) => file.endsWith(".html"));

function escapeJson(value) {
    return value.replace(/\s+/g, " ").trim();
}

for (const file of files) {
    const fullPath = path.join(articlesDir, file);
    let html = fs.readFileSync(fullPath, "utf8");
    const title = html.match(/<title>([\s\S]*?)<\/title>/i)?.[1];
    const description = html.match(/<meta\s+name="description"\s+content="([^"]*)"/i)?.[1];
    if (!title || !description) continue;

    const canonical = `https://mandatmaster.fr/articles/${file}`;
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
