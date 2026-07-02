#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère des articles LIVRES pour MandatMaster (forte demande SEO "livre + immobilier")
et patche index.html + sitemap.xml. Même rendu que build_new_articles.py.
Chaque livre = un lien de recherche Amazon tagué (pattern natif du site).
Idempotent : n'insère pas de carte / d'URL déjà présente."""
import os

TAG = "lebrunnathali-21"
BASE = os.path.dirname(os.path.abspath(__file__))


def amz(terms):
    return f"https://www.amazon.fr/s?k={terms.replace(' ', '+')}&tag={TAG}"


def P(terms, name, label):
    return {"terms": terms, "name": name, "label": label}


BADGE = {
    "materiel": ("bg-amber-100", "text-amber-700", "Matériel"),
    "carriere": ("bg-blue-100", "text-blue-700", "Carrière"),
    "prospection": ("bg-green-100", "text-green-700", "Prospection"),
    "negociation": ("bg-purple-100", "text-purple-700", "Négociation"),
    "marketing": ("bg-pink-100", "text-pink-700", "Marketing"),
}
CTA_TARGET = {
    "materiel": ("#materiel", "Voir tout le matériel"),
    "carriere": ("#carriere", "Voir les guides carrière"),
    "prospection": ("#prospection", "Voir les guides prospection"),
    "negociation": ("#negociation", "Voir les guides négociation"),
    "marketing": ("#marketing", "Voir les guides marketing"),
}

# Titres pour le maillage "À lire aussi" (nouveaux + existants référencés)
TITLES = {
    "livres-devenir-agent-immobilier": "Livres pour devenir agent immobilier",
    "livres-prospection-immobiliere": "Livres de prospection immobilière",
    "livres-estimation-immobiliere": "Livres sur l'estimation immobilière",
    "livres-home-staging": "Livres de home staging",
    "livres-investissement-immobilier-locatif": "Livres sur l'investissement locatif",
    "livres-droit-fiscalite-immobilier": "Livres de droit et fiscalité immobilière",
    "meilleurs-livres-agent-immobilier": "Les 7 meilleurs livres pour agents",
    "livres-negociation-immobiliere": "5 livres sur la négociation",
    "estimation-immobiliere-visite": "Estimation : convaincre en visite",
    "home-staging-materiel-conseils": "Home staging : le matériel",
    "premiere-annee-mandataire-immobilier": "Première année mandataire",
    "comment-devenir-mandataire-immobilier": "Devenir mandataire immobilier",
    "fixer-prix-vente-immobilier": "Fixer le bon prix de vente",
}

NAV = '''    <nav class="border-b border-gray-200 bg-white/90 backdrop-blur-md sticky top-0 z-50">
        <div class="container mx-auto px-4 h-16 flex items-center justify-between">
            <a href="../index.html" class="flex items-center gap-2 font-extrabold text-xl text-navy">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-primary"><rect width="16" height="20" x="4" y="2" rx="2" ry="2" /><path d="M9 22v-4h6v4" /></svg>
                Mandat<span class="text-primary">Master</span>
            </a>
            <div class="hidden md:flex items-center gap-7 text-sm font-medium text-gray-600">
                <a href="../index.html#prospection" class="hover:text-primary transition">Prospection</a>
                <a href="../index.html#negociation" class="hover:text-primary transition">Négociation</a>
                <a href="../index.html#marketing" class="hover:text-primary transition">Marketing</a>
                <a href="../index.html#materiel" class="hover:text-primary transition">Matériel</a>
                <a href="../index.html#carriere" class="hover:text-primary transition">Carrière</a>
            </div>
            <a href="../index.html#materiel" class="bg-primary text-white px-5 py-2 rounded-full font-semibold text-sm hover:bg-blue-700 transition">Le matériel</a>
        </div>
    </nav>'''


def render_article(a):
    bg = BADGE[a["section"]]
    has_product = any("product" in s for s in a["sections"])
    secs = []
    for s in a["sections"]:
        block = f'''            <h2 class="text-2xl font-bold text-gray-900 mt-12 mb-4">{s["h2"]}</h2>
            <p class="mb-4 leading-relaxed text-gray-700">{s["html"]}</p>'''
        if "product" in s:
            p = s["product"]
            block += f'''
            <div class="bg-blue-50 border-l-4 border-primary p-6 mb-8 rounded-r-xl">
                <p class="font-bold text-primary mb-2">Notre sélection</p>
                <p class="text-gray-800 mb-4">{p["name"]}</p>
                <a href="{amz(p["terms"])}" target="_blank" rel="noopener sponsored" class="inline-block bg-yellow-400 text-gray-900 font-bold px-6 py-3 rounded-lg hover:bg-yellow-500 transition">{p["label"]} →</a>
            </div>'''
        secs.append(block)
    sections_html = "\n".join(secs)

    disclosure = ""
    if has_product:
        disclosure = '''
            <p class="text-xs text-gray-400 mt-2 mb-8">En tant que Partenaire Amazon, je réalise un bénéfice sur les achats remplissant les conditions requises. Certains liens ci-dessus sont des liens d'affiliation, sans surcoût pour vous.</p>'''

    related_items = []
    for rs in a["related"]:
        t = TITLES.get(rs, rs)
        related_items.append(f'<li><a href="{rs}.html" class="text-primary font-semibold hover:underline">{t} →</a></li>')
    related_html = "\n                ".join(related_items)

    target, label = CTA_TARGET[a["section"]]
    return f'''<!DOCTYPE html>
<html lang="fr" class="scroll-smooth">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{a["title"]} | MandatMaster</title>
    <meta name="description" content="{a["desc"]}">
    <link rel="canonical" href="https://mandatmaster.fr/articles/{a["slug"]}.html">
    <meta property="og:title" content="{a["title"]} | MandatMaster">
    <meta property="og:description" content="{a["desc"]}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://mandatmaster.fr/articles/{a["slug"]}.html">
    <meta property="og:locale" content="fr_FR">
    <link rel="stylesheet" href="../output.css">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5064203547863113" crossorigin="anonymous"></script>
</head>

<body class="bg-white text-dark font-sans leading-relaxed">

    <!-- NAVBAR -->
{NAV}

    <!-- ARTICLE HEADER -->
    <header class="bg-gray-50 py-16 border-b border-gray-100">
        <div class="max-w-3xl mx-auto px-6 text-center">
            <div class="inline-block px-3 py-1 {bg[0]} {bg[1]} text-xs font-bold rounded-full mb-4 uppercase tracking-widest">{bg[2]}</div>
            <h1 class="text-3xl md:text-5xl font-black text-gray-900 mb-6 leading-tight">{a["h1"]}<span class="text-primary italic">{a["accent"]}</span></h1>
            <p class="text-xl text-gray-600 italic">{a["sub"]}</p>
        </div>
    </header>

    <!-- CONTENT -->
    <main class="max-w-3xl mx-auto px-6 py-16">
        <div class="prose prose-lg prose-blue">
            <p class="text-lg mb-8">{a["intro"]}</p>

{sections_html}
{disclosure}
            <hr class="my-12 border-gray-200">

            <h2 class="text-2xl font-bold text-gray-900 mb-4">À lire aussi</h2>
            <ul class="space-y-2 mb-12">
                {related_html}
            </ul>

            <!-- CTA -->
            <div class="bg-navy rounded-3xl p-8 md:p-12 text-center text-white relative overflow-hidden">
                <div class="absolute top-0 right-0 p-4 opacity-10 text-8xl">{a["emoji"]}</div>
                <h3 class="text-2xl md:text-3xl font-bold mb-6">Tous nos guides pour réussir</h3>
                <p class="text-blue-100 mb-8 max-w-xl mx-auto leading-relaxed">Retrouvez l'ensemble de nos conseils et de notre sélection de matériel pour décrocher plus de mandats.</p>
                <a href="../index.html{target}" class="bg-secondary text-navy px-8 py-4 rounded-full font-black text-lg hover:scale-105 transition transform inline-block shadow-lg">{label} →</a>
            </div>
        </div>
    </main>

    <!-- FOOTER -->
    <footer class="bg-gray-900 text-gray-400 py-12">
        <div class="max-w-5xl mx-auto px-6 text-center">
            <p class="mb-3">© 2026 MandatMaster. Tous droits réservés.</p>
            <p class="text-xs max-w-2xl mx-auto mb-4">En tant que Partenaire Amazon, MandatMaster réalise un bénéfice sur les achats remplissant les conditions requises.</p>
            <div class="flex justify-center gap-6 text-sm">
                <a href="../index.html#mentions" class="hover:text-white transition">Mentions légales</a>
                <a href="../index.html" class="hover:text-white transition">Accueil</a>
            </div>
        </div>
    </footer>

</body>

</html>
'''


def card_light(a, card_bg):
    return f'''                <a href="articles/{a["slug"]}.html" class="group block {card_bg} rounded-2xl border border-gray-200 hover:border-primary/40 hover:shadow-lg transition p-5">
                    <div class="flex items-start gap-4">
                        <div class="shrink-0 w-12 h-12 rounded-xl {a["color"]} flex items-center justify-center text-2xl">{a["emoji"]}</div>
                        <div><h3 class="font-bold text-navy leading-snug group-hover:text-primary transition">{a["title"]}</h3>
                        <p class="text-sm text-gray-500 mt-1.5 leading-relaxed">{a["desc"][:95]}…</p></div>
                    </div>
                </a>'''


def card_dark(a):
    return f'''                <a href="articles/{a["slug"]}.html" class="group block bg-white/5 border border-white/10 rounded-2xl hover:bg-white/10 hover:border-secondary/50 transition p-5">
                    <div class="flex items-start gap-4">
                        <div class="shrink-0 w-12 h-12 rounded-xl bg-secondary/20 flex items-center justify-center text-2xl">{a["emoji"]}</div>
                        <div><h3 class="font-bold leading-snug group-hover:text-secondary transition">{a["title"]}</h3>
                        <p class="text-sm text-blue-100/70 mt-1.5 leading-relaxed">{a["desc"][:95]}…</p></div>
                    </div>
                </a>'''


# ────────────────────────────────────────────────────────────────────────────
A = []

A.append(dict(slug="livres-devenir-agent-immobilier", section="carriere", emoji="📚", color="bg-blue-100",
    title="Les meilleurs livres pour devenir agent immobilier",
    desc="Notre sélection de livres pour débuter et réussir dans l'immobilier : méthode, prospection, prise de mandats et état d'esprit du bon agent.",
    h1="Devenir agent immobilier : ", accent="les livres qui font la différence",
    sub="\"Un bon livre coûte 20 €. Une erreur de débutant peut coûter un mandat.\"",
    intro="On ne naît pas bon agent immobilier, on le devient — et la lecture est le raccourci le moins cher. Avant de dépenser des centaines d'euros en formation, ces ouvrages posent les bases du métier : méthode commerciale, prospection, prise de mandats et bon état d'esprit. Voici notre sélection pour bien démarrer.",
    sections=[
        dict(h2="1. « The Millionaire Real Estate Agent » — Gary Keller", html="Considéré comme la bible du métier, ce livre du fondateur de Keller Williams décortique les modèles qui font la réussite d'un agent : générer des contacts, convertir, s'organiser et penser son activité comme une vraie entreprise. Dense mais fondateur.",
             product=P("the millionaire real estate agent gary keller", "« The Millionaire Real Estate Agent » — Gary Keller (la référence mondiale du métier).", "Voir le livre sur Amazon")),
        dict(h2="2. « Agent immobilier : 100 Conseils, Méthodes et Astuces »", html="Le plus concret et le plus direct sur la prospection, la prise de mandats et les réflexes du terrain. 100 conseils classés en méthodes, conseils et astuces : parfait à garder dans la sacoche pour piocher une idée avant un rendez-vous.",
             product=P("agent immobilier 100 conseils methodes astuces reussir", "« Agent immobilier : 100 Conseils, Méthodes et Astuces pour Réussir ».", "Voir le livre sur Amazon")),
        dict(h2="3. « Devenir agent immobilier, les clés pour réussir » — Stéphane Fritz", html="Un tour d'horizon clair du métier signé par un dirigeant du secteur : statuts, missions, compétences et pièges à éviter. Idéal pour ceux qui hésitent encore à se lancer ou débutent leur première année.",
             product=P("devenir agent immobilier stephane fritz", "« Devenir agent immobilier : les clés pour réussir » — Stéphane Fritz.", "Voir le livre sur Amazon")),
        dict(h2="4. « Les secrets d'une agente » — Sandra Viricel", html="Un regard de terrain, personnel et très concret sur le métier d'agente : notoriété locale, relation client, organisation et motivation. Une lecture inspirante pour se projeter dans le quotidien réel de la profession.",
             product=P("les secrets d'une agente sandra viricel", "« Les secrets d'une agente » — Sandra Viricel.", "Voir le livre sur Amazon")),
        dict(h2="5. « Influence et Manipulation » — Robert Cialdini", html="Pas un livre d'immobilier, mais LE livre sur les leviers de persuasion. Comprendre les principes d'influence (réciprocité, preuve sociale, rareté) transforme votre façon de présenter un prix ou de défendre un mandat exclusif.",
             product=P("influence et manipulation cialdini", "« Influence et Manipulation » — Robert Cialdini (le classique de la persuasion).", "Voir le livre sur Amazon")),
    ],
    related=["meilleurs-livres-agent-immobilier", "premiere-annee-mandataire-immobilier", "livres-prospection-immobiliere"]))

A.append(dict(slug="livres-prospection-immobiliere", section="prospection", emoji="📞", color="bg-green-100",
    title="Les meilleurs livres de prospection immobilière",
    desc="Prospecter sans se décourager : notre sélection de livres pour trouver des mandats, décrocher son téléphone et convertir plus de vendeurs.",
    h1="Prospection immobilière : ", accent="les livres pour remplir son agenda",
    sub="\"La prospection, c'est 80 % du métier. Autant apprendre à la faire bien.\"",
    intro="Aucun mandat ne tombe du ciel : tout part de la prospection. Or c'est la partie que la plupart des agents redoutent le plus. Ces livres donnent la méthode et surtout l'état d'esprit pour prospecter régulièrement, sans se décourager, et transformer les contacts en rendez-vous.",
    sections=[
        dict(h2="1. « Fanatical Prospecting » — Jeb Blount", html="La référence mondiale sur la prospection commerciale. Blount démonte les excuses, donne une méthode multicanale (téléphone, email, réseaux) et un cadre pour ne plus jamais avoir un agenda vide. Transposable mot pour mot à l'immobilier.",
             product=P("fanatical prospecting jeb blount", "« Fanatical Prospecting » — Jeb Blount (la bible de la prospection).", "Voir le livre sur Amazon")),
        dict(h2="2. « The Millionaire Real Estate Agent » — Gary Keller", html="Incontournable ici aussi : Keller montre comment industrialiser sa génération de contacts et bâtir une base de prospects qui travaille pour vous sur le long terme. La prospection vue comme un système, pas comme une corvée.",
             product=P("the millionaire real estate agent gary keller", "« The Millionaire Real Estate Agent » — Gary Keller.", "Voir le livre sur Amazon")),
        dict(h2="3. « Vendeur d'élite » — Michaël Aguilar", html="Le best-seller français de la vente. Techniques concrètes de prise de contact, de traitement des objections et de conclusion, expliquées avec des exemples simples. Parfait pour muscler ses scripts de pige et de porte-à-porte.",
             product=P("vendeur d'elite michael aguilar", "« Vendeur d'élite » — Michaël Aguilar (la vente à la française).", "Voir le livre sur Amazon")),
        dict(h2="4. « Ne coupez jamais la poire en deux » — Chris Voss", html="Écrit par un ex-négociateur du FBI, ce livre apprend à écouter, poser les bonnes questions et faire dire « oui » sans forcer. Redoutable pour décrocher un rendez-vous d'estimation ou désamorcer un vendeur méfiant au téléphone.",
             product=P("ne coupez jamais la poire en deux chris voss", "« Ne coupez jamais la poire en deux » — Chris Voss.", "Voir le livre sur Amazon")),
    ],
    related=["livres-devenir-agent-immobilier", "livres-negociation-immobiliere", "fixer-prix-vente-immobilier"]))

A.append(dict(slug="livres-estimation-immobiliere", section="carriere", emoji="📐", color="bg-blue-100",
    title="Estimation immobilière : les livres de référence",
    desc="Estimer juste et le défendre : notre sélection de livres sur l'estimation et l'expertise immobilière pour fiabiliser vos avis de valeur.",
    h1="Estimation immobilière : ", accent="les ouvrages pour estimer juste",
    sub="\"Un bien surestimé ne se vend pas. Un bien sous-estimé vous coûte votre crédibilité.\"",
    intro="L'estimation est le socle de votre crédibilité : trop haute, le bien stagne ; trop basse, le vendeur fuit. Au-delà des outils en ligne, quelques ouvrages solides expliquent la vraie mécanique de la valeur d'un bien et de l'expertise. De quoi défendre vos avis de valeur avec des arguments, pas au feeling.",
    sections=[
        dict(h2="1. « Guide complet de l'estimation immobilière » — Fares Zlitni", html="Un guide pédagogique qui couvre les méthodes d'estimation pour les particuliers comme pour les professionnels : comparaison, capitalisation, décote et facteurs de valeur. Concret, à jour, idéal pour structurer sa démarche d'estimation.",
             product=P("guide complet estimation immobiliere fares zlitni", "« Guide complet de l'estimation immobilière » — Fares Zlitni.", "Voir le livre sur Amazon")),
        dict(h2="2. « Les secrets de l'expertise immobilière » — Favarger & Thalmann", html="Plus technique, cet ouvrage de référence sur « prix et valeurs » explique ce qui fait réellement la valeur d'un bien et comment un expert la détermine. Pour l'agent qui veut comprendre en profondeur, au-delà des recettes.",
             product=P("les secrets de l'expertise immobiliere prix et valeurs", "« Les secrets de l'expertise immobilière – Prix et valeurs » — Favarger & Thalmann.", "Voir le livre sur Amazon")),
        dict(h2="3. Compléter avec un guide pratique", html="Pour aller plus loin, plusieurs guides pratiques de l'estimation sortent chaque année avec des cas concrets et des grilles prêtes à l'emploi. Comparez les avis avant d'acheter : privilégiez les éditions récentes qui intègrent les dernières évolutions du marché.",
             product=P("livre estimation immobiliere professionnel guide pratique", "Guides pratiques récents sur l'estimation immobilière.", "Voir la sélection sur Amazon")),
    ],
    related=["estimation-immobiliere-visite", "fixer-prix-vente-immobilier", "livres-devenir-agent-immobilier"]))

A.append(dict(slug="livres-home-staging", section="marketing", emoji="🛋️", color="bg-pink-100",
    title="Home staging : les meilleurs livres pour valoriser un bien",
    desc="Valoriser un bien pour le vendre plus vite : notre sélection de livres de home staging, du guide illustré aux cas avant/après.",
    h1="Home staging : ", accent="les livres pour vendre plus vite",
    sub="\"On ne vend pas des murs, on vend un coup de cœur.\"",
    intro="Un bien bien présenté se vend plus vite et souvent plus cher. Le home staging est devenu un argument massue pour convaincre un vendeur de vous confier son bien. Ces livres, écrits par des professionnelles françaises, donnent les principes et les astuces concrètes pour transformer un logement sans se ruiner.",
    sections=[
        dict(h2="1. « Le Livre du Home Staging » — Sylvie Aubin", html="Un guide détaillé et illustré par une home stageuse professionnelle, avec de vrais exemples avant/après. Il couvre le désencombrement, la dépersonnalisation et la mise en scène, pièce par pièce. La base solide pour se lancer.",
             product=P("le livre du home staging sylvie aubin", "« Le Livre du Home Staging » — Sylvie Aubin.", "Voir le livre sur Amazon")),
        dict(h2="2. « Le guide du home staging pour mieux vendre sa maison » — Sophie Sarfati", html="Pensé pour valoriser un bien afin de séduire le plus grand nombre : ambiance neutre, lumière, circulation, petits travaux à fort impact. Clair et directement actionnable, y compris pour conseiller un vendeur.",
             product=P("guide home staging mieux vendre sa maison sophie sarfati", "« Le guide du home staging pour mieux vendre sa maison » — Sophie Sarfati.", "Voir le livre sur Amazon")),
        dict(h2="3. « 100 questions sur le home staging » — Yasmine Médicis & Daniel Van", html="Un format questions-réponses très pratique pour distinguer un bien et répondre aux attentes des acheteurs. Idéal à feuilleter avant une prise de mandat pour arriver avec des conseils concrets à donner au vendeur.",
             product=P("100 questions sur le home staging yasmine medicis", "« 100 questions sur le home staging » — Y. Médicis & D. Van.", "Voir le livre sur Amazon")),
    ],
    related=["home-staging-materiel-conseils", "fixer-prix-vente-immobilier", "livres-estimation-immobiliere"]))

A.append(dict(slug="livres-investissement-immobilier-locatif", section="carriere", emoji="🏘️", color="bg-blue-100",
    title="Investissement locatif : les livres incontournables",
    desc="Mieux conseiller (et investir) : notre sélection des meilleurs livres sur l'investissement immobilier locatif, du débutant au confirmé.",
    h1="Investissement locatif : ", accent="les livres incontournables",
    sub="\"Un agent qui comprend l'investisseur signe des mandats que les autres ratent.\"",
    intro="Beaucoup de vos clients investissent — et beaucoup d'agents investissent aussi. Comprendre l'investissement locatif, c'est parler le langage de l'acheteur investisseur, repérer les bons biens et fidéliser une clientèle qui rachète. Ces best-sellers français sont la meilleure porte d'entrée sur le sujet.",
    sections=[
        dict(h2="1. « L'investissement immobilier locatif intelligent » — Julien Delagrandanne", html="La référence du domaine, notée près de 4,8/5. Une approche méthodique et prudente de l'investissement, appuyée sur des cas réels : sélection du bien, financement, rentabilité et gestion du risque. À lire en premier.",
             product=P("investissement immobilier locatif intelligent julien delagrandanne", "« L'investissement immobilier locatif intelligent » — J. Delagrandanne.", "Voir le livre sur Amazon")),
        dict(h2="2. « Comment investir en immobilier locatif ? » — Daniel Vu", html="Plus de 600 pages très opérationnelles qui accompagnent pas à pas : statut LMNP, SCI, achat-revente, fiscalité, dispositifs. Le guide-outil le plus complet pour ceux qui veulent tout comprendre avant de se lancer.",
             product=P("comment investir en immobilier locatif daniel vu", "« Comment investir en immobilier locatif ? » — Daniel Vu.", "Voir le livre sur Amazon")),
        dict(h2="3. « Investir dans l'immobilier locatif » — Joël B.", html="Le récit pédagogique d'un investisseur, de son premier achat à la constitution d'un patrimoine. Accessible et motivant, parfait pour un débutant ou pour un client à qui recommander une première lecture.",
             product=P("investir dans l'immobilier locatif joel", "« Investir dans l'immobilier locatif » — Joël B.", "Voir le livre sur Amazon")),
    ],
    related=["livres-devenir-agent-immobilier", "livres-droit-fiscalite-immobilier", "fixer-prix-vente-immobilier"]))

A.append(dict(slug="livres-droit-fiscalite-immobilier", section="carriere", emoji="⚖️", color="bg-blue-100",
    title="Droit et fiscalité immobilière : les ouvrages de référence",
    desc="Sécuriser ses transactions : notre sélection d'ouvrages de droit et de fiscalité immobilière pour agents et mandataires.",
    h1="Droit et fiscalité : ", accent="les ouvrages de référence de l'agent",
    sub="\"Connaître la règle, c'est protéger son client — et sa commission.\"",
    intro="Mandat, offre, compromis, diagnostics, fiscalité de la plus-value : chaque transaction est un champ de mines juridique. Un agent qui maîtrise le cadre rassure ses clients et évite les litiges coûteux. Ces ouvrages de référence sont à garder à portée de main pour vérifier un point avant de s'engager.",
    sections=[
        dict(h2="1. Un manuel de droit immobilier à jour", html="Un bon manuel de droit immobilier couvre l'ensemble : baux, vente, copropriété, mandats et responsabilités de l'agent. Privilégiez une édition récente (les Éditions Dalloz et les ouvrages de spécialistes comme Camille Beddeleem font autorité) avec un index thématique pour retrouver vite l'information.",
             product=P("droit immobilier manuel dalloz edition recente", "Manuels de droit immobilier à jour (Dalloz et références du secteur).", "Voir les manuels sur Amazon")),
        dict(h2="2. « Mémento Pratique Immobilier » — Éditions Francis Lefebvre", html="L'outil des professionnels : un mémento dense et fiable qui synthétise droit et fiscalité de l'immobilier, mis à jour chaque année. Un investissement, mais la sécurité qu'il apporte sur une transaction en vaut largement le prix.",
             product=P("memento pratique immobilier francis lefebvre", "« Mémento Pratique Immobilier » — Éditions Francis Lefebvre.", "Voir le livre sur Amazon")),
        dict(h2="3. Un guide de fiscalité immobilière", html="Plus-value, revenus fonciers, LMNP, SCI : un guide de fiscalité immobilière grand public permet d'expliquer simplement les enjeux à un vendeur ou à un acheteur. Comparez les avis et choisissez l'édition de l'année en cours.",
             product=P("guide fiscalite immobiliere plus value revenus fonciers", "Guides de fiscalité immobilière (édition de l'année).", "Voir la sélection sur Amazon")),
    ],
    related=["livres-investissement-immobilier-locatif", "comment-devenir-mandataire-immobilier", "livres-devenir-agent-immobilier"]))


# ── Génération des fichiers ──────────────────────────────────────────────────
art_dir = os.path.join(BASE, "articles")
for a in A:
    with open(os.path.join(art_dir, a["slug"] + ".html"), "w", encoding="utf-8") as f:
        f.write(render_article(a))
print(f"✅ {len(A)} articles livres écrits dans articles/")

# ── Patch index.html : insérer les cartes après une ancre existante par section ─
LAST_CARD = {
    "prospection": ("partenariats-locaux-immobilier", "bg-white"),
    "marketing": ("intelligence-artificielle-immobilier", "bg-white"),
    "carriere": ("fidelisation-recommandation-immobilier", "bg-light"),
}
idx_path = os.path.join(BASE, "index.html")
with open(idx_path, encoding="utf-8") as f:
    html = f.read()

inserted = 0
for section, (anchor_slug, card_bg) in LAST_CARD.items():
    cards = [a for a in A if a["section"] == section and f'articles/{a["slug"]}.html' not in html]
    if not cards:
        continue
    cards_html = "\n".join(card_light(a, card_bg) for a in cards)
    needle = f'articles/{anchor_slug}.html'
    pos = html.find(needle)
    if pos == -1:
        print(f"⚠️  ancre introuvable pour {section} ({anchor_slug})")
        continue
    close = html.find("</a>", pos)
    insert_at = close + len("</a>")
    html = html[:insert_at] + "\n" + cards_html + html[insert_at:]
    inserted += len(cards)
with open(idx_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"✅ {inserted} cartes insérées dans index.html")

# ── Patch sitemap.xml ────────────────────────────────────────────────────────
sm_path = os.path.join(BASE, "sitemap.xml")
with open(sm_path, encoding="utf-8") as f:
    sm = f.read()
entries, added = "", 0
for a in A:
    loc = f"https://mandatmaster.fr/articles/{a['slug']}.html"
    if loc in sm:
        continue
    entries += f"  <url>\n    <loc>{loc}</loc>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>\n"
    added += 1
if entries:
    sm = sm.replace("</urlset>", entries + "</urlset>")
    with open(sm_path, "w", encoding="utf-8") as f:
        f.write(sm)
print(f"✅ {added} URLs ajoutées au sitemap.xml")
