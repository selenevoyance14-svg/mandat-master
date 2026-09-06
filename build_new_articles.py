#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère 30 nouveaux articles MandatMaster + patche index.html et sitemap.xml."""
import os, re

TAG = "lebrunnathali-21"
BASE = os.path.dirname(os.path.abspath(__file__))

def amz(terms):
    return f"https://www.amazon.fr/s?k={terms.replace(' ', '+')}&tag={TAG}"

# Titres des articles existants (pour le maillage "À lire aussi")
EXISTING = {
    "equipement-mandataire-immobilier": "L'équipement indispensable du mandataire",
    "photos-immobilieres-smartphone": "Photos immobilières au smartphone",
    "video-visite-virtuelle-immobilier": "Vidéo et visite virtuelle",
    "home-staging-materiel-conseils": "Home staging : le matériel",
    "bureau-domicile-agent-immobilier": "Le bureau à domicile de l'agent",
    "meilleurs-livres-agent-immobilier": "Les 7 meilleurs livres pour agents",
    "gestion-comptabilite-mandataire": "Comptabilité du mandataire",
    "premiere-annee-mandataire-immobilier": "Première année mandataire",
    "pige-immobiliere-scripts": "Pige immobilière : 3 phrases",
    "farming-porte-a-porte-immobilier": "Farming & porte-à-porte",
    "prospection-digitale-emailing-immobilier": "Prospection digitale",
    "partenariats-locaux-immobilier": "Partenariats locaux",
    "estimation-immobiliere-visite": "Estimation : convaincre en visite",
    "fixer-prix-vente-immobilier": "Fixer le bon prix de vente",
    "reseaux-sociaux-immobilier": "Réseaux sociaux pour agents",
    "creer-site-web-agent-immobilier": "Créer son site web d'agent",
    "panneaux-signaletique-immobilier": "Panneaux & signalétique",
    "voiture-agent-immobilier-accessoires": "La voiture de l'agent",
    "relance-suivi-vendeur-immobilier": "Relance vendeur",
    "mandat-exclusif-strategie": "Mandat exclusif : le remède",
    "negociation-immobiliere-techniques": "Négociation : 4 techniques",
    "personal-branding-agent-immobilier": "Personal branding immobilier",
    "intelligence-artificielle-immobilier": "L'IA dans l'immobilier",
}

# Couleurs de badge par section
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

def P(terms, name, label):
    return {"terms": terms, "name": name, "label": label}

A = []  # liste des articles

# ============ MATÉRIEL (18) ============
A.append(dict(slug="meilleur-telemetre-laser-immobilier", section="materiel", emoji="📏", color="bg-amber-100",
    title="Télémètre laser : lequel choisir pour vos estimations",
    desc="Comment choisir un télémètre laser pour mesurer un bien rapidement et précisément. Critères, portée et modèles pour agents immobiliers.",
    h1="Télémètre laser : ", accent="mesurer un bien comme un pro",
    sub="\"Sortir un mètre ruban devant un vendeur, c'est l'image de l'amateur.\"",
    intro="Mesurer les surfaces fait partie de chaque estimation. Le télémètre laser remplace le mètre ruban : plus rapide, plus précis, et surtout beaucoup plus crédible devant un vendeur. En quelques secondes vous relevez les dimensions d'une pièce sans bouger. Voici comment choisir le bon modèle.",
    sections=[
        dict(h2="1. La portée : 30 à 50 mètres suffisent", html="Pour un usage immobilier, une portée de 30 à 50 mètres couvre la quasi-totalité des biens, du studio à la grande maison. Inutile de payer pour 100 mètres réservés aux professionnels du bâtiment. Privilégiez la précision (± 2 mm) plutôt que la portée maximale.",
             product=P("telemetre laser 50m precision immobilier", "Télémètre laser portée 40-50 m, précision ± 2 mm, écran rétroéclairé.", "Voir les télémètres sur Amazon")),
        dict(h2="2. Les fonctions utiles : surface et volume automatiques", html="Le calcul automatique de surface (longueur × largeur) et de volume vous fait gagner un temps précieux pendant la visite. Certains modèles mémorisent les dernières mesures et calculent l'addition de plusieurs pièces. Pratique pour annoncer une surface totale sans calculatrice."),
        dict(h2="3. La connexion Bluetooth : reporter directement dans une appli", html="Les modèles Bluetooth envoient les mesures vers une application sur votre smartphone ou tablette. Vous construisez le plan du bien au fur et à mesure de la visite, sans recopier de chiffres. Un vrai plus si vous réalisez des plans 2D pour vos annonces.",
             product=P("telemetre laser bluetooth application", "Télémètre laser Bluetooth compatible application de mesure.", "Voir les modèles Bluetooth sur Amazon")),
        dict(h2="4. Robustesse et autonomie", html="Votre télémètre voyage dans la sacoche toute la journée. Choisissez un modèle avec protection caoutchouc, indice de résistance à la poussière, et une bonne autonomie sur piles. Un étui de protection évite les chocs."),
    ],
    related=["equipement-mandataire-immobilier", "estimation-immobiliere-visite", "fixer-prix-vente-immobilier"]))

A.append(dict(slug="ordinateur-portable-agent-immobilier", section="materiel", emoji="💻", color="bg-blue-100",
    title="Quel PC portable choisir quand on est agent immobilier",
    desc="Le bon ordinateur portable pour un mandataire immobilier : critères, autonomie, légèreté et budget pour travailler partout.",
    h1="Quel ordinateur portable ", accent="pour un agent immobilier",
    sub="\"Votre PC vous suit du café du matin au rendez-vous notaire.\"",
    intro="Annonces, CRM, dossiers d'estimation, signatures électroniques : l'ordinateur portable est l'outil central du mandataire. Inutile de viser la machine de gamer, mais quelques critères font la différence au quotidien.",
    sections=[
        dict(h2="1. Légèreté et autonomie avant tout", html="Vous travaillez en mobilité : un poids sous 1,5 kg et une autonomie de 8 heures minimum changent la vie. Un format 13 à 14 pouces est le meilleur compromis entre confort d'écran et transportabilité.",
             product=P("ordinateur portable 14 pouces leger autonomie bureautique", "PC portable 14 pouces léger, bonne autonomie, idéal mobilité.", "Voir les PC portables sur Amazon")),
        dict(h2="2. Assez de puissance pour le quotidien", html="Pour la bureautique, le web, le CRM et la retouche photo légère, visez 16 Go de RAM et un SSD. Vous éviterez les ralentissements quand vous jonglez entre navigateur, visio et logiciel d'annonce."),
        dict(h2="3. Un bon écran pour présenter au client", html="Vous montrez régulièrement votre écran au vendeur (estimation, photos, plan de com). Un écran lumineux et bien défini soigne votre image. Pensez aussi à un support de PC portable pour une posture correcte au bureau.",
             product=P("support ordinateur portable reglable aluminium", "Support PC portable réglable en aluminium pour le bureau.", "Voir les supports sur Amazon")),
        dict(h2="4. La souris et les accessoires qui font gagner du temps", html="Une souris sans fil silencieuse et un hub USB-C (pour brancher écran, clé USB et imprimante) complètent l'équipement. Petit budget, gros confort.",
             product=P("souris sans fil silencieuse bureautique", "Souris sans fil silencieuse, confortable pour de longues sessions.", "Voir les souris sur Amazon")),
    ],
    related=["bureau-domicile-agent-immobilier", "equipement-mandataire-immobilier", "tablette-agent-immobilier"]))

A.append(dict(slug="tablette-agent-immobilier", section="materiel", emoji="📲", color="bg-slate-100",
    title="La tablette idéale pour les visites et signatures",
    desc="Pourquoi et comment choisir une tablette quand on est agent immobilier : visites, présentations, signature électronique sur le terrain.",
    h1="La tablette idéale ", accent="pour vos visites et signatures",
    sub="\"Tendre une tablette à signer, c'est moderne et rassurant.\"",
    intro="La tablette est l'outil de terrain par excellence : présenter un dossier d'estimation en visite, faire défiler des photos, signer un mandat électroniquement. Plus légère que le PC, plus grande que le téléphone, elle soigne votre image high-tech.",
    sections=[
        dict(h2="1. La taille : 10 à 11 pouces, le bon équilibre", html="Un écran de 10 à 11 pouces est assez grand pour présenter confortablement, tout en restant facile à tenir d'une main et à glisser dans la sacoche. En dessous, on perd en lisibilité ; au-dessus, ça devient encombrant.",
             product=P("tablette 11 pouces ecran lecture documents", "Tablette 10-11 pouces, écran net, idéale présentation et lecture.", "Voir les tablettes sur Amazon")),
        dict(h2="2. Le stylet pour la signature et l'annotation", html="Un stylet permet la signature électronique fluide et l'annotation de plans ou de documents en direct. Vérifiez la compatibilité avant l'achat.",
             product=P("stylet tablette signature precis", "Stylet précis pour tablette, signature et annotation.", "Voir les stylets sur Amazon")),
        dict(h2="3. Une bonne connexion data", html="En visite, vous n'avez pas toujours de Wi-Fi. Une tablette avec carte SIM (4G/5G) ou un simple partage de connexion depuis votre téléphone garantit l'accès à vos outils en ligne partout."),
        dict(h2="4. La protection : étui clavier et coque", html="Un étui avec support intégré transforme la tablette en petit poste de travail, et une coque la protège des chutes en rendez-vous. Indispensable pour un outil qui passe de main en main.",
             product=P("etui tablette support clavier protection", "Étui tablette avec support et protection renforcée.", "Voir les étuis sur Amazon")),
    ],
    related=["ordinateur-portable-agent-immobilier", "equipement-mandataire-immobilier", "estimation-immobiliere-visite"]))

A.append(dict(slug="imprimante-agent-immobilier", section="materiel", emoji="🖨️", color="bg-sky-100",
    title="Quelle imprimante pour un mandataire indépendant",
    desc="Bien choisir son imprimante d'agent immobilier : mandats, flyers, dossiers d'estimation. Jet d'encre ou laser, multifonction, coût à la page.",
    h1="Quelle imprimante ", accent="pour un mandataire indépendant",
    sub="\"Imprimer un mandat à 22 h sans courir au tabac : ça n'a pas de prix.\"",
    intro="Mandats à signer, dossiers d'estimation, flyers de boîtage, attestations : l'agent indépendant imprime plus qu'il ne le croit. Une bonne imprimante multifonction à domicile vous fait gagner un temps fou et soigne vos supports.",
    sections=[
        dict(h2="1. Laser ou jet d'encre ?", html="Pour beaucoup de documents en noir et blanc (mandats, contrats), une laser monochrome est rapide et économique à la page. Si vous imprimez des flyers et photos en couleur, une jet d'encre couleur est plus polyvalente. Le mieux : une multifonction couleur avec un coût d'encre raisonnable.",
             product=P("imprimante multifonction wifi recto verso couleur", "Imprimante multifonction couleur Wi-Fi, recto-verso, scanner intégré.", "Voir les imprimantes sur Amazon")),
        dict(h2="2. Le scanner intégré : indispensable", html="Vous numérisez en permanence : pièces d'identité, diagnostics, justificatifs. Une multifonction avec scanner (idéalement chargeur automatique) vous évite l'application photo approximative et accélère la constitution des dossiers."),
        dict(h2="3. Le Wi-Fi et l'impression mobile", html="Imprimer directement depuis le téléphone ou la tablette, sans brancher de câble, est un confort quotidien. Vérifiez la compatibilité avec l'impression mobile (AirPrint et équivalents)."),
        dict(h2="4. Anticiper le coût des consommables", html="Une imprimante pas chère peut coûter cher en encre. Regardez le prix des cartouches ou optez pour un modèle à réservoirs rechargeables si vous imprimez beaucoup. Gardez toujours un jeu de cartouches d'avance.",
             product=P("cartouches encre compatibles imprimante lot", "Lot de cartouches d'encre compatibles, économique.", "Voir les cartouches sur Amazon")),
    ],
    related=["gestion-comptabilite-mandataire", "panneaux-signaletique-immobilier", "equipement-mandataire-immobilier"]))

A.append(dict(slug="sacoche-sac-agent-immobilier", section="materiel", emoji="💼", color="bg-amber-100",
    title="Bien choisir sa sacoche d'agent immobilier",
    desc="La sacoche de l'agent immobilier : comment choisir un sac professionnel pratique et élégant pour transporter PC, tablette et dossiers.",
    h1="Bien choisir ", accent="sa sacoche d'agent immobilier",
    sub="\"Le premier objet que le client voit, c'est votre sac.\"",
    intro="La sacoche, c'est votre bureau ambulant et un élément fort de votre image. Elle doit accueillir votre PC, votre tablette, vos dossiers et vos accessoires, tout en restant élégante. Voici les critères pour bien la choisir.",
    sections=[
        dict(h2="1. L'élégance professionnelle", html="Cuir ou simili de qualité, couleur sobre (noir, marron, gris foncé) : votre sac doit inspirer le sérieux. Évitez les sacs de sport ou trop casual pour les rendez-vous d'estimation.",
             product=P("sacoche cuir homme femme ordinateur professionnelle", "Sacoche professionnelle en cuir/simili, sobre et élégante.", "Voir les sacoches sur Amazon")),
        dict(h2="2. L'organisation interne", html="Compartiment matelassé pour le PC, emplacement tablette, poches pour stylos, cartes de visite, télémètre et chargeur. Une sacoche bien compartimentée vous évite de fouiller devant le client."),
        dict(h2="3. Le format porte-documents", html="Vos mandats et dossiers d'estimation sont en A4 : vérifiez que la sacoche les accueille sans les plier. Un parapheur ou porte-documents rigide protège vos contrats des froissures.",
             product=P("porte documents A4 conferencier professionnel", "Porte-documents / conférencier A4 pour mandats et dossiers.", "Voir les porte-documents sur Amazon")),
        dict(h2="4. Confort et solidité", html="Bandoulière réglable et matelassée, fond renforcé, fermetures solides : votre sac est sollicité toute la journée. La qualité de fabrication évite le remplacement tous les six mois."),
    ],
    related=["equipement-mandataire-immobilier", "vetements-look-agent-immobilier", "cartes-de-visite-agent-immobilier"]))

A.append(dict(slug="boite-a-cles-securisee-immobilier", section="materiel", emoji="🔐", color="bg-slate-100",
    title="Boîte à clés sécurisée : le guide d'achat de l'agent",
    desc="Tout savoir sur la boîte à clés à code pour agents immobiliers : sécuriser l'accès à un bien, faciliter les visites, choisir un modèle fiable.",
    h1="Boîte à clés sécurisée : ", accent="le guide d'achat",
    sub="\"Une clé bien gérée, c'est une visite qui se fait sans vous.\"",
    intro="La boîte à clés à code est l'outil discret qui simplifie l'organisation des visites, surtout sur les biens vacants ou éloignés. Elle sécurise l'accès tout en vous évitant des allers-retours. Encore faut-il choisir un modèle fiable.",
    sections=[
        dict(h2="1. Fixation murale ou anse ?", html="Le modèle à anse s'accroche à une poignée ou une grille : pratique et déplaçable. Le modèle mural se fixe à demeure, plus discret et plus sécurisé. Pour un agent, l'anse est souvent le bon compromis.",
             product=P("boite a cles securisee code anse immobilier", "Boîte à clés à code avec anse, robuste, usage extérieur.", "Voir les boîtes à clés sur Amazon")),
        dict(h2="2. La résistance aux intempéries et aux chocs", html="Installée dehors, la boîte subit pluie, gel et tentatives d'effraction. Privilégiez un corps en métal (zinc/aluminium), un mécanisme protégé et une coque résistante. Vérifiez la capacité : certaines clés volumineuses ne rentrent pas dans les petits modèles."),
        dict(h2="3. Un code que vous maîtrisez", html="Changez le code après chaque visite sensible et ne le communiquez jamais en clair par SMS public. La boîte à clés est un confort, pas un blanc-seing : restez vigilant sur la sécurité du bien que le vendeur vous confie."),
        dict(h2="4. En complément : l'étiquette et le porte-clés pro", html="Identifiez chaque clé sans révéler l'adresse (un simple code interne) à l'aide d'étiquettes et de porte-clés numérotés. Vous gagnez en organisation et en discrétion.",
             product=P("porte cles numerotes etiquettes agence immobiliere", "Porte-clés numérotés avec étiquettes pour gestion des biens.", "Voir les porte-clés sur Amazon")),
    ],
    related=["panneaux-signaletique-immobilier", "equipement-mandataire-immobilier", "farming-porte-a-porte-immobilier"]))

A.append(dict(slug="trepied-stabilisateur-smartphone-immobilier", section="materiel", emoji="🎚️", color="bg-red-100",
    title="Trépied et stabilisateur pour vos visites filmées",
    desc="Filmer des visites immobilières stables et pro avec un smartphone : trépied, stabilisateur (gimbal) et accessoires à connaître.",
    h1="Trépied et stabilisateur ", accent="pour des vidéos stables",
    sub="\"Une vidéo qui tremble, c'est une vidéo qu'on ne regarde pas.\"",
    intro="La vidéo de visite est devenue incontournable pour se démarquer. Le problème n°1 des vidéos d'agents : l'image qui tremble. Un trépied et un stabilisateur transforment un film amateur en visite fluide et professionnelle.",
    sections=[
        dict(h2="1. Le stabilisateur (gimbal) smartphone", html="Le gimbal compense vos mouvements et donne ce rendu \"glissé\" des vidéos pro. Pour filmer une visite en marchant de pièce en pièce, c'est l'accessoire qui fait toute la différence.",
             product=P("stabilisateur gimbal smartphone 3 axes", "Stabilisateur gimbal 3 axes pour smartphone, vidéo fluide.", "Voir les stabilisateurs sur Amazon")),
        dict(h2="2. Le trépied polyvalent", html="Pour les plans fixes (façade, séjour, time-lapse) et les vidéos face caméra, un trépied réglable est indispensable. Un modèle avec rotule et tête flexible s'adapte à toutes les situations.",
             product=P("trepied smartphone reglable telecommande", "Trépied smartphone réglable avec télécommande Bluetooth.", "Voir les trépieds sur Amazon")),
        dict(h2="3. Le micro-cravate pour les visites commentées", html="Si vous commentez la visite, le son du smartphone ne suffit pas. Un micro-cravate sans fil capte votre voix proprement, même dans une grande pièce qui résonne.",
             product=P("micro cravate sans fil smartphone", "Micro-cravate sans fil pour smartphone, son clair.", "Voir les micros sur Amazon")),
        dict(h2="4. Travailler la lumière", html="La vidéo, comme la photo, vit de la lumière. Ouvrez les volets, allumez les lampes, et complétez si besoin avec un petit panneau LED portable pour les pièces sombres."),
    ],
    related=["video-visite-virtuelle-immobilier", "photos-immobilieres-smartphone", "ring-light-eclairage-photo-immobiliere"]))

A.append(dict(slug="ring-light-eclairage-photo-immobiliere", section="materiel", emoji="💡", color="bg-amber-100",
    title="Éclairage et ring light pour des photos qui vendent",
    desc="Comment éclairer ses photos et vidéos immobilières : ring light, panneau LED et astuces lumière pour des visuels professionnels au smartphone.",
    h1="Éclairage et ring light ", accent="pour des visuels qui vendent",
    sub="\"En photo immobilière, la lumière fait 80 % du résultat.\"",
    intro="Une belle photo de bien, c'est avant tout une question de lumière. Pièces sombres, contre-jour, ambiance jaune : sans un minimum d'éclairage, même un beau bien paraît terne. Voici le matériel simple pour des visuels lumineux.",
    sections=[
        dict(h2="1. Le panneau LED portable", html="Compact et puissant, le panneau LED éclaire les pièces sombres, les couloirs et les salles de bain sans fenêtre. Avec température de couleur réglable, vous évitez les rendus trop jaunes ou trop bleus.",
             product=P("panneau led photo video temperature reglable", "Panneau LED portable, intensité et température réglables.", "Voir les panneaux LED sur Amazon")),
        dict(h2="2. La ring light pour vos vidéos face caméra", html="Pour vos stories, reels et vidéos de présentation, la ring light donne un éclairage flatteur et homogène sur le visage. Un modèle sur trépied avec support smartphone est parfait pour le contenu réseaux sociaux.",
             product=P("ring light trepied support smartphone", "Ring light sur trépied avec support smartphone.", "Voir les ring lights sur Amazon")),
        dict(h2="3. Maîtriser la lumière naturelle", html="Le meilleur éclairage reste la lumière du jour. Photographiez aux heures lumineuses, ouvrez rideaux et volets, et évitez le plein contre-jour. Le matériel vient compléter, pas remplacer, une bonne lumière naturelle."),
        dict(h2="4. Stabiliser pour éviter le flou", html="En basse lumière, le smartphone allonge le temps de pose et l'image devient floue. Un trépied évite ce problème et permet des photos nettes même en intérieur sombre."),
    ],
    related=["photos-immobilieres-smartphone", "objectif-grand-angle-smartphone-immobilier", "home-staging-materiel-conseils"]))

A.append(dict(slug="objectif-grand-angle-smartphone-immobilier", section="materiel", emoji="🔭", color="bg-sky-100",
    title="Objectif grand-angle smartphone pour l'immobilier",
    desc="Pourquoi utiliser un objectif grand-angle clipsable sur smartphone pour photographier des biens immobiliers, et comment bien s'en servir.",
    h1="L'objectif grand-angle ", accent="pour photographier vos biens",
    sub="\"Une petite pièce bien cadrée paraît deux fois plus grande.\"",
    intro="Le défi de la photo immobilière : faire entrer une pièce entière dans le cadre sans se coller au mur. L'objectif grand-angle clipsable, ou simplement le mode ultra grand-angle du smartphone, élargit le champ et met en valeur les volumes.",
    sections=[
        dict(h2="1. L'objectif clipsable grand-angle", html="Un objectif grand-angle se clipse sur l'appareil photo du smartphone et élargit fortement le champ. Idéal pour les petites pièces, les salles de bain et les couloirs où l'on manque de recul.",
             product=P("objectif grand angle smartphone clip photo", "Objectif grand-angle clipsable pour smartphone.", "Voir les objectifs sur Amazon")),
        dict(h2="2. Attention à la déformation", html="Trop de grand-angle déforme les lignes et trahit les proportions, ce qui crée des déceptions en visite. Restez honnête : le but est de montrer le volume réel, pas de tromper l'acheteur. Tenez l'appareil droit et à mi-hauteur."),
        dict(h2="3. Le cadrage qui agrandit", html="Photographiez depuis un angle de la pièce, à hauteur de poitrine, lignes verticales bien droites. Rangez et dépersonnalisez avant la photo : un espace dégagé paraît toujours plus grand."),
        dict(h2="4. Compléter avec un mini-trépied", html="Pour des photos nettes et un cadrage régulier sur toutes les pièces, un mini-trépied de table ou flexible stabilise le smartphone et harmonise vos prises de vue.",
             product=P("mini trepied flexible smartphone", "Mini-trépied flexible pour smartphone, stable et léger.", "Voir les mini-trépieds sur Amazon")),
    ],
    related=["photos-immobilieres-smartphone", "ring-light-eclairage-photo-immobiliere", "video-visite-virtuelle-immobilier"]))

A.append(dict(slug="drone-photo-immobiliere-debutant", section="materiel", emoji="🚁", color="bg-blue-100",
    title="Drone immobilier : par où commencer quand on débute",
    desc="Utiliser un drone pour des photos immobilières aériennes : intérêt, choix d'un modèle débutant et règles à connaître pour un agent immobilier.",
    h1="Drone immobilier : ", accent="par où commencer",
    sub="\"Une vue aérienne, et une maison de campagne devient un coup de cœur.\"",
    intro="Pour les maisons, les biens avec terrain ou en bord de mer, la photo aérienne par drone fait sensation et valorise fortement l'annonce. Les drones débutants sont aujourd'hui accessibles et faciles à piloter. Voici comment vous lancer.",
    sections=[
        dict(h2="1. Un drone débutant suffit", html="Pour de la photo et vidéo immobilière, un drone compact avec bonne caméra stabilisée et modes automatiques fait parfaitement l'affaire. Les modèles légers sont aussi plus simples côté réglementation.",
             product=P("drone camera debutant stabilise compact", "Drone compact pour débutant, caméra stabilisée.", "Voir les drones sur Amazon")),
        dict(h2="2. Connaître les règles avant de voler", html="Le pilotage de drone est encadré : zones autorisées, distance, survol de tiers, et selon les cas une formation ou un enregistrement en ligne. Renseignez-vous sur la réglementation en vigueur et les zones de vol autorisées avant chaque prise de vue. C'est non négociable."),
        dict(h2="3. Les prises de vue qui valorisent un bien", html="Vue d'ensemble du terrain, mise en situation dans le quartier, plan descendant sur la toiture : quelques images aériennes bien choisies suffisent. Inutile d'en abuser, deux ou trois plans forts marquent les esprits."),
        dict(h2="4. Protéger et transporter le matériel", html="Batteries supplémentaires, sac de transport et carte mémoire rapide complètent le kit. Un drone est fragile : un étui dédié évite les mauvaises surprises dans le coffre.",
             product=P("sac transport drone batteries accessoires", "Sac de transport pour drone et accessoires.", "Voir les sacs drone sur Amazon")),
    ],
    related=["video-visite-virtuelle-immobilier", "photos-immobilieres-smartphone", "trepied-stabilisateur-smartphone-immobilier"]))

A.append(dict(slug="camera-360-visite-virtuelle-immobilier", section="materiel", emoji="🌀", color="bg-purple-100",
    title="Caméra 360° pour vos visites virtuelles immobilières",
    desc="Créer des visites virtuelles immobilières avec une caméra 360 : intérêt, choix du matériel et méthode pour des biens visités à distance.",
    h1="La caméra 360° ", accent="pour vos visites virtuelles",
    sub="\"Filtrer les visites inutiles, c'est récupérer des heures chaque semaine.\"",
    intro="La visite virtuelle 360° permet à un acheteur de parcourir le bien depuis chez lui. Résultat : moins de visites \"touristiques\", des acheteurs plus qualifiés, et un argument de poids face au vendeur lors de l'estimation. La caméra 360 rend tout cela simple.",
    sections=[
        dict(h2="1. Pourquoi la 360 change la donne", html="Un acheteur à distance, un bien atypique, un vendeur pressé : la visite virtuelle élargit l'audience et fait gagner du temps à tout le monde. C'est aussi un argument différenciant quand vous présentez votre offre de services au vendeur."),
        dict(h2="2. Choisir sa caméra 360", html="Une caméra 360 grand public, associée à une application de visite virtuelle, suffit pour démarrer. Privilégiez une bonne résolution et la compatibilité avec les plateformes de visite que vous comptez utiliser.",
             product=P("camera 360 photo video haute resolution", "Caméra 360° haute résolution pour visites virtuelles.", "Voir les caméras 360 sur Amazon")),
        dict(h2="3. La méthode pour une visite virtuelle propre", html="Rangez et éclairez chaque pièce comme pour une photo. Placez la caméra sur un trépied au centre de la pièce, à hauteur des yeux, et restez hors champ. Enchaînez les points de capture de manière logique, comme une vraie visite.",
             product=P("trepied camera 360 leger", "Trépied léger pour caméra 360.", "Voir les trépieds 360 sur Amazon")),
        dict(h2="4. Valoriser la visite dans vos annonces", html="Intégrez le lien de visite virtuelle dans vos annonces et vos emails aux acheteurs. C'est un signal de professionnalisme qui augmente le taux de prise de contact."),
    ],
    related=["video-visite-virtuelle-immobilier", "creer-site-web-agent-immobilier", "reseaux-sociaux-immobilier"]))

A.append(dict(slug="cartes-de-visite-agent-immobilier", section="materiel", emoji="🪪", color="bg-slate-100",
    title="Cartes de visite agent immobilier : modèles et impression",
    desc="Réussir ses cartes de visite d'agent immobilier : informations à mettre, design, format et où les faire imprimer pour un rendu pro.",
    h1="Cartes de visite : ", accent="le réflexe qui rapporte des mandats",
    sub="\"La carte qu'on garde, c'est l'agent qu'on rappelle.\"",
    intro="À l'ère du digital, la carte de visite reste un outil de prospection redoutable : boîtage, porte-à-porte, commerçants partenaires, fin de visite. Une carte soignée, c'est une trace physique qui circule et qui rappelle votre nom au bon moment.",
    sections=[
        dict(h2="1. Les informations essentielles", html="Nom, fonction, réseau, téléphone, email, QR code vers votre site ou vos avis Google. Allez à l'essentiel : une carte surchargée se jette. Une photo peut aider à créer le lien et à ce qu'on vous reconnaisse."),
        dict(h2="2. Un design qui inspire confiance", html="Restez sobre et cohérent avec votre identité visuelle (couleurs, logo du réseau). Un papier épais et une finition mate ou vernie donnent une impression de qualité. La carte est un échantillon de votre professionnalisme."),
        dict(h2="3. Le porte-cartes, détail qui compte", html="Sortir une carte froissée du fond de la poche ruine l'effet. Un porte-cartes élégant garde vos cartes nickel et soigne le geste devant le client.",
             product=P("porte cartes de visite metal elegant", "Porte-cartes de visite en métal, élégant et protecteur.", "Voir les porte-cartes sur Amazon")),
        dict(h2="4. Toujours en avoir sur soi", html="La meilleure carte est celle que vous avez sur vous au bon moment. Gardez-en dans la sacoche, la voiture et la poche. Un distributeur ou un présentoir chez vos commerçants partenaires démultiplie la diffusion.",
             product=P("presentoir cartes de visite comptoir", "Présentoir de comptoir pour cartes de visite.", "Voir les présentoirs sur Amazon")),
    ],
    related=["personal-branding-agent-immobilier", "partenariats-locaux-immobilier", "sacoche-sac-agent-immobilier"]))

A.append(dict(slug="powerbank-chargeur-agent-immobilier", section="materiel", emoji="🔋", color="bg-green-100",
    title="Batterie externe et chargeurs pour agent nomade",
    desc="Ne jamais tomber en panne de batterie : powerbank, chargeurs et câbles indispensables pour un agent immobilier toujours en mobilité.",
    h1="Batterie externe et chargeurs ", accent="pour ne jamais tomber en panne",
    sub="\"Un téléphone à plat, c'est un mandat qui passe à la concurrence.\"",
    intro="Téléphone, tablette, parfois micro ou caméra : votre journée d'agent dépend de vos appareils. Tomber en panne entre deux visites n'est pas une option. Quelques accessoires bien choisis vous garantissent l'autonomie toute la journée.",
    sections=[
        dict(h2="1. La powerbank 20 000 mAh", html="Une batterie externe de 20 000 mAh recharge votre téléphone trois à quatre fois. Glissée dans la sacoche, c'est votre assurance pour les journées chargées et le porte-à-porte loin de la voiture.",
             product=P("batterie externe 20000mah charge rapide usb c", "Batterie externe 20 000 mAh, charge rapide USB-C.", "Voir les batteries sur Amazon")),
        dict(h2="2. Le chargeur secteur multiport", html="Au bureau ou à l'hôtel, un chargeur multiport recharge téléphone, tablette et powerbank en même temps. Un seul bloc, plusieurs appareils, moins de câbles.",
             product=P("chargeur secteur usb multiport charge rapide", "Chargeur secteur multiport, charge rapide.", "Voir les chargeurs sur Amazon")),
        dict(h2="3. Des câbles de rechange partout", html="Le câble qui lâche au mauvais moment est un classique. Gardez des câbles renforcés dans la voiture, la sacoche et au bureau. Le coût est dérisoire face à la tranquillité.",
             product=P("cable usb c renforce lot resistant", "Lot de câbles USB-C renforcés, résistants.", "Voir les câbles sur Amazon")),
        dict(h2="4. Le chargeur voiture rapide", html="Votre voiture est votre bureau mobile : un chargeur allume-cigare rapide double port maintient vos appareils chargés entre chaque rendez-vous.",
             product=P("chargeur voiture rapide usb c double port", "Chargeur voiture rapide double port USB-C.", "Voir les chargeurs voiture sur Amazon")),
    ],
    related=["voiture-agent-immobilier-accessoires", "equipement-mandataire-immobilier", "tablette-agent-immobilier"]))

A.append(dict(slug="casque-antibruit-teletravail-mandataire", section="materiel", emoji="🎧", color="bg-indigo-100",
    title="Casque antibruit pour le télétravail du mandataire",
    desc="Bien choisir un casque ou des écouteurs antibruit pour passer ses appels de prospection et visios au calme quand on est mandataire.",
    h1="Le casque antibruit ", accent="pour des appels au calme",
    sub="\"En pige, votre voix doit être la seule chose qu'on entende.\"",
    intro="Le mandataire passe une grande partie de ses journées au téléphone : pige, relances, visios avec clients et notaires. Un bon casque antibruit améliore la qualité de vos appels, votre concentration et votre image au téléphone.",
    sections=[
        dict(h2="1. Le micro avant tout", html="Pour la prospection, ce qui compte le plus, c'est que votre interlocuteur vous entende clairement. Un casque avec micro à réduction de bruit isole votre voix des bruits ambiants (café, rue, open space).",
             product=P("casque bluetooth micro reduction bruit teletravail", "Casque Bluetooth avec micro à réduction de bruit.", "Voir les casques sur Amazon")),
        dict(h2="2. La réduction de bruit active pour se concentrer", html="Travailler dans un café ou un espace partagé devient confortable avec la réduction de bruit active. Vous gagnez en concentration pour rédiger vos annonces ou préparer vos estimations."),
        dict(h2="3. L'autonomie et le confort", html="Vous portez le casque plusieurs heures par jour : visez de bons coussinets et une autonomie suffisante pour tenir la journée. Un modèle pliable se range facilement dans la sacoche."),
        dict(h2="4. Les écouteurs, l'option mobile", html="Pour les appels en marchant ou en voiture, des écouteurs sans fil avec bon micro sont plus pratiques qu'un casque. Beaucoup d'agents ont les deux : casque au bureau, écouteurs en déplacement.",
             product=P("ecouteurs sans fil micro appels clair", "Écouteurs sans fil avec micro clair pour les appels.", "Voir les écouteurs sur Amazon")),
    ],
    related=["bureau-domicile-agent-immobilier", "pige-immobiliere-scripts", "relance-suivi-vendeur-immobilier"]))

A.append(dict(slug="agenda-planner-agent-immobilier", section="materiel", emoji="📓", color="bg-amber-100",
    title="Agenda et planner papier pour s'organiser",
    desc="Pourquoi un agenda ou planner papier reste utile à l'agent immobilier, et comment le choisir pour piloter prospection, visites et objectifs.",
    h1="Agenda et planner papier ", accent="pour piloter votre activité",
    sub="\"Ce qui n'est pas planifié n'est pas fait.\"",
    intro="Entre les visites, les estimations, la prospection et l'administratif, l'agent jongle avec mille choses. Même à l'ère du numérique, beaucoup des meilleurs reviennent au papier pour planifier leur semaine et garder le cap sur leurs objectifs.",
    sections=[
        dict(h2="1. Pourquoi le papier fonctionne", html="Écrire à la main ancre les priorités et limite les distractions du téléphone. Un planner sous les yeux rappelle vos objectifs de prospection chaque matin, là où une appli se referme et s'oublie."),
        dict(h2="2. Le bon format pour un agent", html="Un planner hebdomadaire avec vue d'ensemble de la semaine convient mieux qu'un agenda jour par jour : vous visualisez vos créneaux de visite, vos plages de pige et vos relances. Un format A5 se glisse dans la sacoche.",
             product=P("planner hebdomadaire organiseur professionnel a5", "Planner hebdomadaire A5 pour professionnels.", "Voir les planners sur Amazon")),
        dict(h2="3. Suivre ses indicateurs", html="Notez chaque semaine vos chiffres clés : appels de pige, estimations, mandats rentrés, ventes. Un carnet de suivi simple vous montre noir sur blanc ce qui marche et ce qu'il faut corriger.",
             product=P("carnet professionnel pages lignees a5 qualite", "Carnet professionnel A5 de qualité pour le suivi.", "Voir les carnets sur Amazon")),
        dict(h2="4. Coupler papier et numérique", html="Le papier pour réfléchir et planifier, l'agenda du téléphone pour les rappels et le partage. Les deux ne s'opposent pas : ils se complètent."),
    ],
    related=["organisation-productivite-agent-immobilier", "plan-prospection-90-jours-debutant", "premiere-annee-mandataire-immobilier"]))

A.append(dict(slug="materiel-classement-comptabilite-immobilier", section="materiel", emoji="🗂️", color="bg-sky-100",
    title="Matériel de classement pour votre comptabilité",
    desc="Le matériel pour classer factures, justificatifs et frais quand on est mandataire immobilier : classeurs, étiqueteuse, scanner et organisation.",
    h1="Le matériel de classement ", accent="pour une compta sereine",
    sub="\"Chaque justificatif perdu, c'est de l'argent qui part en impôts.\"",
    intro="Le mandataire indépendant doit suivre ses frais et conserver ses justificatifs. Un système de classement simple vous évite le stress de fin d'année et vous fait récupérer chaque euro de frais déductibles. Voici le matériel qui structure tout ça.",
    sections=[
        dict(h2="1. Le classeur à intercalaires", html="Un classeur par année, avec intercalaires (frais de véhicule, fournitures, communication, cotisations…), garde vos justificatifs en ordre. Simple, visuel, efficace.",
             product=P("classeur factures intercalaires pochettes comptabilite", "Classeur à intercalaires et pochettes pour la comptabilité.", "Voir les classeurs sur Amazon")),
        dict(h2="2. L'étiqueteuse pour s'y retrouver", html="Une étiqueteuse rend votre classement clair et durable : dossiers, boîtes d'archives, classeurs. Un détail qui fait gagner du temps à chaque recherche de document.",
             product=P("etiqueteuse portable rubans", "Étiqueteuse portable avec rubans.", "Voir les étiqueteuses sur Amazon")),
        dict(h2="3. Numériser pour ne rien perdre", html="Scannez ou photographiez chaque justificatif et sauvegardez-le dans un dossier daté. Un scanner avec chargeur automatique accélère le traitement des piles de factures. La double conservation papier + numérique vous protège."),
        dict(h2="4. Le carnet de kilométrage", html="Vos déplacements sont déductibles : un carnet de kilométrage (ou une appli) bien tenu peut représenter une économie importante. Notez date, trajet et motif au fil de l'eau, pas en bloc en décembre.",
             product=P("carnet kilometrage frais professionnels", "Carnet de kilométrage pour frais professionnels.", "Voir les carnets sur Amazon")),
    ],
    related=["gestion-comptabilite-mandataire", "gerer-ses-impots-mandataire-immobilier", "imprimante-agent-immobilier"]))

A.append(dict(slug="coffret-cadeau-client-immobilier", section="materiel", emoji="🎁", color="bg-pink-100",
    title="Coffret cadeau client : les meilleures idées",
    desc="Quelles idées de cadeaux offrir à un client après la vente d'un bien : coffrets et attentions qui marquent et génèrent des recommandations.",
    h1="Le cadeau client : ", accent="l'attention qui rapporte des recommandations",
    sub="\"Un cadeau de remise des clés, et le client parle de vous pendant des années.\"",
    intro="La remise des clés est un moment fort et émotionnel. Une attention bien choisie transforme un client satisfait en ambassadeur qui vous recommande à son entourage. Le meilleur retour sur investissement de votre activité, pour quelques dizaines d'euros.",
    sections=[
        dict(h2="1. Le coffret gourmand ou bien-être", html="Une valeur sûre, appréciée de tous : coffret de produits locaux, vin (à éviter selon le contexte), thé/café haut de gamme, ou coffret bien-être. L'idée : marquer le coup avec élégance.",
             product=P("coffret cadeau gourmand produits du terroir", "Coffret cadeau gourmand de produits du terroir.", "Voir les coffrets sur Amazon")),
        dict(h2="2. Le cadeau \"emménagement\"", html="Pour des acheteurs qui arrivent dans un nouveau logement, un kit emménagement (bougie d'intérieur, petit nécessaire, plante) tombe à pic et reste utile. C'est attentionné et mémorable.",
             product=P("coffret cadeau emmenagement maison bougie", "Coffret cadeau emménagement avec bougie et accessoires maison.", "Voir les coffrets emménagement sur Amazon")),
        dict(h2="3. Personnaliser pour marquer les esprits", html="Une carte manuscrite, une photo de la maison encadrée, ou un mot personnalisé valent souvent plus que le cadeau lui-même. C'est l'intention qui crée le bouche-à-oreille."),
        dict(h2="4. Le cadeau qui circule", html="Un objet utile et durable (tote bag, mug, carnet de qualité au design soigné) que le client utilisera devant d'autres personnes prolonge votre visibilité bien après la vente.",
             product=P("coffret bougie parfumee maison elegant cadeau", "Coffret bougie parfumée élégant pour cadeau.", "Voir les idées cadeaux sur Amazon")),
    ],
    related=["cadeaux-clients-closing-immobilier", "fidelisation-recommandation-immobilier", "personal-branding-agent-immobilier"]))

A.append(dict(slug="fournitures-bureau-agent-immobilier", section="materiel", emoji="✏️", color="bg-slate-100",
    title="Les fournitures de bureau utiles au quotidien",
    desc="La liste des fournitures de bureau vraiment utiles à un agent immobilier indépendant : du stylo de qualité au tableau de suivi.",
    h1="Les fournitures de bureau ", accent="qui font gagner du temps",
    sub="\"Un bureau bien équipé, c'est une journée sans friction.\"",
    intro="Ce ne sont pas les outils les plus glamour, mais les fournitures du quotidien fluidifient votre travail et soignent les petits détails que voient vos clients. Voici la liste utile, sans superflu.",
    sections=[
        dict(h2="1. Le stylo de qualité pour les signatures", html="Faire signer un mandat avec un stylo bon marché qui bave, ce n'est pas le bon message. Un beau stylo, agréable à écrire, accompagne dignement le moment de la signature.",
             product=P("stylo elegant cadeau professionnel signature", "Stylo élégant pour la signature, finition soignée.", "Voir les stylos sur Amazon")),
        dict(h2="2. Le tableau blanc ou planning mural", html="Au bureau, un tableau blanc affiche vos biens en cours, votre pipeline et vos objectifs. Avoir ses priorités sous les yeux booste la productivité.",
             product=P("tableau blanc magnetique mural bureau", "Tableau blanc magnétique mural pour le bureau.", "Voir les tableaux sur Amazon")),
        dict(h2="3. Les pochettes et protège-documents", html="Pour remettre un dossier d'estimation propre et présentable, des pochettes de présentation transparentes ou un porte-vues font la différence. Le fond et la forme comptent.",
             product=P("pochettes presentation transparentes lot a4", "Lot de pochettes de présentation transparentes A4.", "Voir les pochettes sur Amazon")),
        dict(h2="4. Les indispensables qui dépannent", html="Surligneurs, post-it, agrafeuse, ramette de papier de qualité : un petit stock évite la course de dernière minute avant un rendez-vous. Gardez aussi un kit minimal dans la voiture."),
    ],
    related=["bureau-domicile-agent-immobilier", "imprimante-agent-immobilier", "materiel-classement-comptabilite-immobilier"]))

# ============ CARRIÈRE (7) ============
A.append(dict(slug="comment-devenir-mandataire-immobilier", section="carriere", emoji="🚀", color="bg-blue-100",
    title="Comment devenir mandataire immobilier",
    desc="Devenir mandataire immobilier indépendant : étapes, statut, réseau, formation et premiers pas pour se lancer dans le métier.",
    h1="Comment devenir ", accent="mandataire immobilier",
    sub="\"Le métier est ouvert : c'est le travail qui fait la différence.\"",
    intro="Le métier de mandataire immobilier attire de plus en plus de personnes en reconversion, pour sa liberté et son potentiel de revenus. Bonne nouvelle : il est accessible sans diplôme spécifique, à condition de rejoindre un réseau et de se former. Voici les grandes étapes.",
    sections=[
        dict(h2="1. Mandataire ou agent : la différence", html="L'agent immobilier titulaire détient la carte professionnelle (carte T) et peut diriger une agence. Le mandataire, lui, travaille sous l'égide d'un réseau qui détient cette carte : il n'a pas besoin de la carte T pour exercer, mais agit pour le compte du réseau. C'est la voie la plus accessible pour démarrer."),
        dict(h2="2. Choisir son réseau", html="Le réseau vous apporte le cadre légal, les outils, la formation et la marque. Comparez les conditions : taux de commission reversé, frais mensuels, qualité de la formation et accompagnement. C'est une décision structurante pour vos débuts."),
        dict(h2="3. Se former aux fondamentaux", html="Prospection, estimation, droit, négociation : même sans diplôme, vous devez maîtriser les bases. Les réseaux proposent des formations, mais les meilleurs complètent par des lectures et de la pratique intensive dès les premières semaines."),
        dict(h2="4. Déclarer son activité et se lancer", html="La plupart des mandataires démarrent sous un statut indépendant et s'inscrivent au registre dédié. Renseignez-vous sur les démarches en vigueur auprès de votre réseau et des organismes officiels. Puis place au terrain : la prospection commence dès le premier jour."),
    ],
    related=["premiere-annee-mandataire-immobilier", "statut-auto-entrepreneur-mandataire", "iad-safti-capifrance-comparatif-reseaux"]))

A.append(dict(slug="salaire-agent-immobilier-independant", section="carriere", emoji="💶", color="bg-green-100",
    title="Combien gagne vraiment un agent immobilier indépendant",
    desc="Le revenu d'un mandataire immobilier indépendant : comment fonctionne la rémunération, ce qui fait varier les gains et comment l'augmenter.",
    h1="Combien gagne vraiment ", accent="un agent indépendant",
    sub="\"Pas de plafond, pas de plancher : tout dépend de votre activité.\"",
    intro="C'est la grande question avant de se lancer. La vérité : le revenu d'un mandataire est très variable, car il dépend des commissions sur les ventes réalisées. Certains gagnent peu, d'autres très bien. Voici les mécanismes pour comprendre et se projeter sereinement.",
    sections=[
        dict(h2="1. Une rémunération à la commission", html="Le mandataire ne touche pas de salaire fixe : il est rémunéré sur les honoraires des ventes qu'il conclut, selon un pourcentage reversé par son réseau. Plus le réseau reverse, plus vous gardez par vente, mais les frais et services varient aussi."),
        dict(h2="2. Ce qui fait varier les revenus", html="Le nombre de mandats rentrés, le prix moyen des biens de votre secteur, votre taux de transformation et votre régularité. Un agent qui prospecte avec méthode et signe en exclusivité gagne structurellement plus qu'un agent passif."),
        dict(h2="3. Les premiers mois sont les plus durs", html="Entre le premier mandat et la première commission, il s'écoule souvent plusieurs mois (délai de vente + acte notarié). Beaucoup d'abandons ont lieu là. Prévoyez une trésorerie de départ et tenez le rythme de prospection malgré l'absence de revenus immédiats."),
        dict(h2="4. Comment augmenter ses revenus", html="Privilégier les mandats exclusifs, soigner son image pour attirer les recommandations, fidéliser ses clients, et viser un secteur ou des biens à valeur plus élevée. Le revenu suit la valeur que vous créez et la constance de vos actions."),
    ],
    related=["fixer-sa-commission-agent-immobilier", "mandat-exclusif-strategie", "premiere-annee-mandataire-immobilier"]))

A.append(dict(slug="iad-safti-capifrance-comparatif-reseaux", section="carriere", emoji="🏢", color="bg-slate-100",
    title="IAD, Safti, Capifrance : quel réseau de mandataires choisir",
    desc="Comparer les réseaux de mandataires immobiliers : critères de choix, commissions, frais, formation et accompagnement pour bien décider.",
    h1="Quel réseau de mandataires ", accent="choisir pour se lancer",
    sub="\"Le bon réseau, c'est celui qui correspond à VOTRE projet.\"",
    intro="IAD, Safti, Capifrance, et bien d'autres : les réseaux de mandataires se multiplient et se ressemblent en apparence. Le choix est pourtant structurant. Plutôt que de chercher \"le meilleur\", cherchez celui qui colle à votre profil et vos objectifs. Voici les critères qui comptent vraiment.",
    sections=[
        dict(h2="1. Le modèle de rémunération", html="Regardez le pourcentage de commission reversé, mais aussi le système de \"marketing de réseau\" (revenus sur le recrutement) que certains proposent et d'autres non. Un fort reversement ne fait pas tout si l'accompagnement est absent."),
        dict(h2="2. Les frais et le coût réel", html="Frais d'entrée, abonnement mensuel aux outils, coûts de formation : additionnez tout pour connaître votre point mort. Un réseau \"pas cher\" peut l'être en surface seulement, et inversement."),
        dict(h2="3. La formation et l'accompagnement", html="Pour un débutant, c'est souvent le critère n°1. Formation initiale, parrain local disponible, outils (CRM, diffusion d'annonces, juridique) : c'est ce qui détermine votre vitesse de démarrage."),
        dict(h2="4. La marque et la présence locale", html="Une marque connue rassure les vendeurs et facilite la prospection. Mais une marque très présente dans votre secteur peut aussi signifier plus de concurrence interne. Pesez le pour et le contre selon votre zone."),
    ],
    related=["comment-devenir-mandataire-immobilier", "premiere-annee-mandataire-immobilier", "salaire-agent-immobilier-independant"]))

A.append(dict(slug="statut-auto-entrepreneur-mandataire", section="carriere", emoji="📑", color="bg-amber-100",
    title="Quel statut pour démarrer comme mandataire",
    desc="Auto-entrepreneur, entreprise individuelle, portage : comprendre les statuts pour se lancer comme mandataire immobilier indépendant.",
    h1="Quel statut ", accent="pour démarrer comme mandataire",
    sub="\"Le bon statut, c'est celui qui colle à votre niveau d'activité.\"",
    intro="Avant de signer votre premier mandat, vous devez choisir un cadre juridique pour exercer. Plusieurs options existent, chacune avec ses avantages selon votre situation et vos objectifs de chiffre d'affaires. Voici les grandes lignes, à confirmer avec un professionnel du chiffre.",
    sections=[
        dict(h2="1. La micro-entreprise (auto-entrepreneur)", html="Simple à créer et à gérer, la micro-entreprise séduit beaucoup de débutants. Comptabilité allégée, cotisations calculées sur le chiffre d'affaires : idéale pour tester l'activité. Attention au plafond de chiffre d'affaires, vite atteint avec quelques belles ventes."),
        dict(h2="2. L'entreprise individuelle au réel", html="Quand l'activité grossit ou que les frais sont importants (véhicule, communication, matériel), le régime réel permet de déduire ses charges. C'est souvent l'étape suivante après la micro-entreprise."),
        dict(h2="3. Anticiper les cotisations et impôts", html="Quel que soit le statut, prévoyez une part de chaque commission pour les cotisations sociales et l'impôt. Les taux et règles évoluent : renseignez-vous sur les barèmes en vigueur et faites-vous accompagner pour ne pas avoir de mauvaise surprise."),
        dict(h2="4. Se faire conseiller dès le départ", html="Un expert-comptable ou un conseiller spécialisé dans l'immobilier vous orientera vers le statut le plus adapté à votre projet. Le bon choix au départ évite des changements coûteux ensuite. Un bon livre sur la micro-entreprise aide aussi à poser les bases.",
             product=P("livre guide micro entreprise auto entrepreneur", "Guide pratique de la micro-entreprise pour bien démarrer.", "Voir les guides sur Amazon")),
    ],
    related=["comment-devenir-mandataire-immobilier", "gerer-ses-impots-mandataire-immobilier", "gestion-comptabilite-mandataire"]))

A.append(dict(slug="fixer-sa-commission-agent-immobilier", section="carriere", emoji="🧮", color="bg-blue-100",
    title="Comment fixer sa commission d'agent immobilier",
    desc="Déterminer et défendre ses honoraires d'agent immobilier : comment fixer sa commission, la justifier au vendeur et éviter de brader.",
    h1="Comment fixer ", accent="et défendre sa commission",
    sub="\"Brader ses honoraires, c'est dévaloriser son travail.\"",
    intro="La commission est le nerf de la guerre du métier. Trop élevée, vous perdez des mandats ; trop basse, vous travaillez à perte et dévalorisez votre service. L'enjeu n'est pas tant le pourcentage que votre capacité à le justifier avec assurance.",
    sections=[
        dict(h2="1. Comprendre les ordres de grandeur", html="Les honoraires d'agence se situent généralement dans une fourchette qui varie selon le prix du bien et le secteur : un pourcentage plus élevé sur les petits montants, plus faible sur les biens chers. Renseignez-vous sur les pratiques de votre zone, sans vous aligner aveuglément vers le bas."),
        dict(h2="2. Vendre la valeur, pas le prix", html="Le vendeur ne paie pas un pourcentage, il paie un résultat : vendre au bon prix, vite, en sécurité. Présentez tout ce que vous apportez (estimation juste, diffusion, photos, visites filtrées, négociation, suivi notaire) pour que vos honoraires paraissent évidents."),
        dict(h2="3. Tenir face à la négociation", html="Beaucoup de vendeurs testent en demandant une remise. Si vous cédez trop vite, vous prouvez que votre prix était surévalué. Préparez vos réponses, défendez votre valeur avec calme, et apprenez à dire non quand c'est justifié."),
        dict(h2="4. La cohérence avec votre positionnement", html="Un agent premium qui soigne tout (image, supports, accompagnement) justifie des honoraires plus élevés. Un positionnement clair rend votre commission cohérente. L'incohérence, elle, se paie en mandats perdus."),
    ],
    related=["salaire-agent-immobilier-independant", "negociation-immobiliere-techniques", "mandat-exclusif-strategie"]))

A.append(dict(slug="mandataire-immobilier-temps-partiel", section="carriere", emoji="⏳", color="bg-green-100",
    title="Se lancer à temps partiel comme mandataire : est-ce viable",
    desc="Devenir mandataire immobilier à temps partiel ou en complément d'activité : avantages, limites et conseils pour réussir malgré le temps limité.",
    h1="Mandataire à temps partiel : ", accent="est-ce vraiment viable",
    sub="\"Possible, mais à condition d'être redoutablement organisé.\"",
    intro="Beaucoup se lancent comme mandataire en gardant un emploi ou une autre activité, pour sécuriser leurs revenus. C'est possible et fréquent, mais cela demande une organisation sans faille. Voici les conditions pour que ça marche vraiment.",
    sections=[
        dict(h2="1. Les avantages du démarrage progressif", html="Garder un revenu pendant que l'activité monte en charge réduit la pression financière, principal facteur d'abandon. Vous apprenez le métier sans jouer votre survie sur les premiers mois."),
        dict(h2="2. Le vrai défi : la disponibilité", html="Les vendeurs et acheteurs sont souvent disponibles en soirée et le week-end, ce qui peut coïncider avec votre temps libre. Mais la réactivité en journée (appels, rendez-vous) reste un enjeu : un acheteur qui ne vous joint pas appelle un autre agent."),
        dict(h2="3. Concentrer ses efforts", html="Avec peu de temps, pas de dispersion : ciblez un secteur précis, concentrez votre prospection sur des créneaux fixes, et automatisez ce qui peut l'être (réponses, suivi). La régularité prime sur le volume."),
        dict(h2="4. Savoir quand passer à plein temps", html="Quand l'activité génère un revenu régulier et que le manque de disponibilité commence à vous coûter des mandats, c'est le signal pour basculer à plein temps. Le temps partiel est un tremplin, rarement une fin en soi."),
    ],
    related=["organisation-productivite-agent-immobilier", "comment-devenir-mandataire-immobilier", "plan-prospection-90-jours-debutant"]))

A.append(dict(slug="gerer-ses-impots-mandataire-immobilier", section="carriere", emoji="🧾", color="bg-amber-100",
    title="Impôts et cotisations du mandataire : les bases",
    desc="Comprendre les bases des impôts et cotisations sociales quand on est mandataire immobilier indépendant, et comment bien s'organiser.",
    h1="Impôts et cotisations : ", accent="les bases pour le mandataire",
    sub="\"Mettre de côté à chaque commission, c'est dormir tranquille.\"",
    intro="Indépendant, le mandataire gère lui-même ses cotisations et son impôt. Mal anticipé, c'est la mauvaise surprise garantie. Bien organisé, c'est un non-sujet. Voici les principes de base, à confirmer avec un professionnel du chiffre car les règles évoluent.",
    sections=[
        dict(h2="1. Provisionner à chaque encaissement", html="La règle d'or : à chaque commission perçue, mettez immédiatement de côté une part pour les cotisations sociales et l'impôt sur un compte séparé. Vous ne dépensez jamais de l'argent qui n'est pas vraiment à vous."),
        dict(h2="2. Distinguer cotisations et impôt", html="Les cotisations sociales financent votre protection (retraite, santé). L'impôt sur le revenu s'ajoute. Selon votre statut, les modalités de calcul et de paiement diffèrent : informez-vous précisément sur votre régime."),
        dict(h2="3. Déduire ses frais quand c'est possible", html="Au régime réel, de nombreux frais professionnels sont déductibles : véhicule, communication, matériel, formation. D'où l'importance de conserver chaque justificatif. C'est de l'impôt en moins, légalement."),
        dict(h2="4. Se faire accompagner", html="Un expert-comptable spécialisé immobilier optimise votre situation et vous évite les erreurs. Son coût est souvent largement compensé par les économies et la tranquillité qu'il apporte. Un bon ouvrage de gestion aide aussi à comprendre les mécanismes.",
             product=P("livre comptabilite gestion independant guide", "Guide de gestion et comptabilité pour indépendant.", "Voir les guides sur Amazon")),
    ],
    related=["gestion-comptabilite-mandataire", "statut-auto-entrepreneur-mandataire", "materiel-classement-comptabilite-immobilier"]))

# ============ PROSPECTION (3) ============
A.append(dict(slug="trouver-premiers-clients-vendeurs", section="prospection", emoji="🎯", color="bg-green-100",
    title="Trouver ses premiers clients vendeurs quand on débute",
    desc="Les actions concrètes pour décrocher ses premiers mandats quand on débute comme mandataire immobilier, sans réseau ni notoriété.",
    h1="Trouver ses premiers ", accent="clients vendeurs",
    sub="\"Vos premiers mandats viendront de gens qui vous connaissent déjà.\"",
    intro="Le plus dur dans ce métier, c'est de démarrer sans portefeuille ni notoriété. Pourtant, des dizaines de mandataires signent leur premier mandat dès le premier mois. Le secret n'est pas magique : c'est de l'action ciblée et beaucoup de contacts. Voici par où commencer.",
    sections=[
        dict(h2="1. Activer son réseau personnel", html="Vos premiers mandats viennent presque toujours de votre entourage : famille, amis, anciens collègues, commerçants. Annoncez clairement votre nouvelle activité à tout le monde et demandez qui connaît un projet de vente. C'est gratuit et redoutablement efficace."),
        dict(h2="2. Se rendre visible dans son secteur", html="Choisissez un secteur géographique précis et devenez-y une figure familière : boîtage régulier, présence sur les groupes locaux, partenariats avec les commerçants. La répétition crée la confiance et la notoriété locale."),
        dict(h2="3. Prospecter les biens de particuliers", html="Les annonces de particuliers (\"vente sans agence\") sont une source directe de prospects vendeurs. Un appel de pige bien préparé, avec un vrai apport de valeur, transforme certains de ces particuliers en mandats."),
        dict(h2="4. Tenir le rythme sans se décourager", html="Au début, vous essuierez beaucoup de \"non\". C'est normal et ça fait partie du jeu. Fixez-vous un objectif quotidien de contacts et tenez-le coûte que coûte : la régularité finit toujours par payer."),
    ],
    related=["pige-immobiliere-scripts", "farming-porte-a-porte-immobilier", "plan-prospection-90-jours-debutant"]))

A.append(dict(slug="plan-prospection-90-jours-debutant", section="prospection", emoji="📆", color="bg-blue-100",
    title="Un plan de prospection sur 90 jours pour débuter",
    desc="Un plan d'action de prospection sur 90 jours pour un mandataire débutant : objectifs hebdomadaires, actions concrètes et suivi des résultats.",
    h1="Un plan de prospection ", accent="sur 90 jours",
    sub="\"Sans plan, on prospecte par à-coups. Avec un plan, on prospecte tous les jours.\"",
    intro="Les 90 premiers jours déterminent souvent la réussite d'un mandataire. Sans plan, on s'éparpille et on se décourage. Avec une feuille de route claire, on avance avec régularité. Voici un plan simple à adapter à votre situation.",
    sections=[
        dict(h2="Jours 1-30 : poser les fondations", html="Définissez votre secteur, constituez votre liste de contacts personnels, préparez vos scripts de pige et vos supports. Lancez le boîtage et les premiers appels. Objectif : un volume élevé de contacts pour amorcer la pompe, sans pression de résultat immédiat."),
        dict(h2="Jours 31-60 : intensifier le terrain", html="Augmentez la cadence : pige quotidienne, porte-à-porte ciblé, estimations gratuites proposées dans votre secteur. Visez vos premières estimations et premiers mandats. Notez ce qui fonctionne pour le répéter."),
        dict(h2="Jours 61-90 : transformer et fidéliser", html="Travaillez la conversion des estimations en mandats, soignez le suivi de vos prospects tièdes, et demandez systématiquement des recommandations. À ce stade, vous devriez avoir plusieurs mandats et un pipeline qui s'alimente."),
        dict(h2="Mesurer chaque semaine", html="Suivez vos indicateurs : contacts, appels, estimations, mandats. Un planner ou un carnet de suivi rend ces chiffres visibles et vous permet d'ajuster le tir avant qu'il ne soit trop tard.",
             product=P("planner objectifs suivi hebdomadaire professionnel", "Planner de suivi d'objectifs hebdomadaire.", "Voir les planners sur Amazon")),
    ],
    related=["trouver-premiers-clients-vendeurs", "organisation-productivite-agent-immobilier", "pige-immobiliere-scripts"]))

A.append(dict(slug="developper-son-reseau-immobilier", section="prospection", emoji="🔗", color="bg-teal-100",
    title="Développer son réseau pour signer plus de mandats",
    desc="Comment développer son réseau de contacts et d'apporteurs d'affaires pour générer des mandats immobiliers réguliers sans prospection à froid.",
    h1="Développer son réseau ", accent="pour signer plus de mandats",
    sub="\"Les meilleurs mandats arrivent par recommandation.\"",
    intro="La prospection à froid est nécessaire au début, mais épuisante sur la durée. Les agents qui durent construisent un réseau qui leur apporte des mandats régulièrement, presque sans effort. C'est un investissement de long terme qui change tout. Voici comment le bâtir.",
    sections=[
        dict(h2="1. Cartographier ses apporteurs potentiels", html="Notaires, courtiers, artisans, syndics, commerçants, gestionnaires : tous croisent des projets de vente. Identifiez dans votre secteur ceux qui peuvent vous recommander, et faites-vous connaître d'eux."),
        dict(h2="2. Donner avant de recevoir", html="Un réseau se construit sur la réciprocité. Recommandez vos partenaires, envoyez-leur des clients, rendez service. Celui qui ne fait que demander est vite oublié ; celui qui apporte de la valeur reste en tête."),
        dict(h2="3. Entretenir le lien dans la durée", html="Un contact pris une fois et jamais relancé ne sert à rien. Prenez des nouvelles, passez un café, restez présent sans être lourd. La régularité du lien fait que l'on pense à vous le jour où une vente se présente."),
        dict(h2="4. Soigner sa réputation", html="Votre réseau parle de vous quand vous n'êtes pas là. Un travail sérieux, des clients satisfaits et une image cohérente transforment chaque relation en source de recommandations. La réputation est le meilleur des commerciaux."),
    ],
    related=["partenariats-locaux-immobilier", "fidelisation-recommandation-immobilier", "personal-branding-agent-immobilier"]))

# ============ NÉGOCIATION (1) ============
A.append(dict(slug="erreurs-estimation-immobiliere", section="negociation", emoji="📉", color="bg-red-100",
    title="Les erreurs d'estimation qui font fuir les vendeurs",
    desc="Les erreurs les plus fréquentes lors d'une estimation immobilière et comment les éviter pour décrocher le mandat et inspirer confiance au vendeur.",
    h1="Les erreurs d'estimation ", accent="qui font fuir les vendeurs",
    sub="\"Surévaluer pour plaire, c'est perdre le mandat à coup sûr.\"",
    intro="L'estimation est le moment de vérité face au vendeur. Bien menée, elle décroche le mandat ; bâclée, elle vous décrédibilise. Beaucoup d'agents commettent les mêmes erreurs, souvent par peur de déplaire. Les voici, pour les éviter.",
    sections=[
        dict(h2="1. Surévaluer pour séduire le vendeur", html="L'erreur n°1 : annoncer un prix gonflé pour faire plaisir et rentrer le mandat. Le bien ne se vend pas, le vendeur se braque, et vous portez la responsabilité. Un prix juste et argumenté vaut mieux qu'une promesse intenable."),
        dict(h2="2. Arriver sans préparation", html="Estimer \"au feeling\" sans comparables ni dossier solide ruine votre crédibilité. Préparez votre étude de marché, vos références de ventes récentes et un dossier propre. Le sérieux se voit dès les premières minutes."),
        dict(h2="3. Ne pas écouter le vendeur", html="Foncer sur le prix sans comprendre le projet, les contraintes et les attentes du vendeur est une faute. L'écoute crée la confiance et vous donne les clés pour argumenter. Posez des questions avant d'annoncer quoi que ce soit."),
        dict(h2="4. Ne pas savoir justifier son prix", html="Annoncer un chiffre sans l'expliquer ne convainc personne. Appuyez-vous sur des comparables, l'état du bien et la dynamique du marché local. Un prix justifié, même décevant pour le vendeur, est toujours mieux accepté qu'un chiffre sorti du chapeau."),
    ],
    related=["estimation-immobiliere-visite", "fixer-prix-vente-immobilier", "objections-vendeurs-reponses"]))

# ============ MARKETING (1) ============
A.append(dict(slug="crm-immobilier-comparatif", section="marketing", emoji="🗃️", color="bg-pink-100",
    title="Quel CRM choisir quand on est agent immobilier",
    desc="Bien choisir son CRM immobilier pour suivre prospects, vendeurs et acheteurs : critères, fonctions utiles et conseils pour un mandataire indépendant.",
    h1="Quel CRM ", accent="pour un agent immobilier",
    sub="\"Un contact oublié, c'est un mandat perdu.\"",
    intro="Au-delà de quelques contacts, impossible de tout suivre de tête. Le CRM (logiciel de gestion de la relation client) centralise vos prospects, vos relances et votre pipeline. C'est l'outil qui vous évite de laisser filer des opportunités. Voici comment choisir le vôtre.",
    sections=[
        dict(h2="1. Souvent fourni par le réseau", html="Beaucoup de réseaux de mandataires intègrent un CRM dans leurs outils. Avant de chercher ailleurs, exploitez à fond celui qu'on vous fournit : il est généralement adapté au métier et déjà payé dans votre abonnement."),
        dict(h2="2. Les fonctions vraiment utiles", html="Fiche contact complète, suivi des relances avec rappels, gestion du pipeline (prospect → estimation → mandat → vente), et historique des échanges. Le reste est souvent du superflu. Privilégiez la simplicité d'usage : un CRM compliqué n'est jamais utilisé."),
        dict(h2="3. La discipline avant l'outil", html="Le meilleur CRM ne sert à rien si vous n'y entrez pas vos contacts et n'y notez pas vos actions. La vraie clé, c'est l'habitude quotidienne de tout consigner. Un outil simple bien utilisé bat un outil puissant négligé."),
        dict(h2="4. Mobile et synchronisé", html="Vous travaillez en mobilité : choisissez un CRM accessible sur téléphone et tablette, synchronisé en temps réel. Pouvoir consulter et mettre à jour une fiche entre deux visites change votre réactivité."),
    ],
    related=["relance-suivi-vendeur-immobilier", "prospection-digitale-emailing-immobilier", "organisation-productivite-agent-immobilier"]))

# =================== RENDU ===================
NEW_TITLES = {a["slug"]: a["title"] for a in A}
ALL_TITLES = dict(EXISTING)
ALL_TITLES.update(NEW_TITLES)

NAV = '''    <nav class="border-b border-gray-200 bg-white/90 backdrop-blur-md sticky top-0 z-50">
        <div class="container mx-auto px-4 h-16 flex items-center justify-between">
            <a href="/" class="flex items-center gap-2 font-extrabold text-xl text-navy">
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
        t = ALL_TITLES.get(rs, rs)
        related_items.append(f'<li><a href="/articles/{rs}" class="text-primary font-semibold hover:underline">{t} →</a></li>')
    related_html = "\n                ".join(related_items)

    target, label = CTA_TARGET[a["section"]]
    return f'''<!DOCTYPE html>
<html lang="fr" class="scroll-smooth">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{a["title"]} | MandatMaster</title>
    <meta name="description" content="{a["desc"]}">
    <link rel="canonical" href="https://mandatmaster.fr/articles/{a["slug"]}">
    <meta property="og:title" content="{a["title"]} | MandatMaster">
    <meta property="og:description" content="{a["desc"]}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://mandatmaster.fr/articles/{a["slug"]}">
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
                <a href="/mentions-legales" class="hover:text-white transition">Mentions légales</a>
                <a href="/" class="hover:text-white transition">Accueil</a>
            </div>
        </div>
    </footer>

</body>

</html>
'''

# Carte pour la home
def card_light(a, card_bg):
    return f'''                <a href="/articles/{a["slug"]}" class="group block {card_bg} rounded-2xl border border-gray-200 hover:border-primary/40 hover:shadow-lg transition p-5">
                    <div class="flex items-start gap-4">
                        <div class="shrink-0 w-12 h-12 rounded-xl {a["color"]} flex items-center justify-center text-2xl">{a["emoji"]}</div>
                        <div><h3 class="font-bold text-navy leading-snug group-hover:text-primary transition">{a["title"]}</h3>
                        <p class="text-sm text-gray-500 mt-1.5 leading-relaxed">{a["desc"][:95]}…</p></div>
                    </div>
                </a>'''

def card_dark(a):
    return f'''                <a href="/articles/{a["slug"]}" class="group block bg-white/5 border border-white/10 rounded-2xl hover:bg-white/10 hover:border-secondary/50 transition p-5">
                    <div class="flex items-start gap-4">
                        <div class="shrink-0 w-12 h-12 rounded-xl bg-secondary/20 flex items-center justify-center text-2xl">{a["emoji"]}</div>
                        <div><h3 class="font-bold leading-snug group-hover:text-secondary transition">{a["title"]}</h3>
                        <p class="text-sm text-blue-100/70 mt-1.5 leading-relaxed">{a["desc"][:95]}…</p></div>
                    </div>
                </a>'''

# Génération des fichiers
art_dir = os.path.join(BASE, "articles")
for a in A:
    path = os.path.join(art_dir, a["slug"] + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(render_article(a))
print(f"✅ {len(A)} articles écrits dans articles/")

# Patch index.html : insérer les cartes après la dernière carte de chaque section
LAST_CARD = {
    "prospection": ("partenariats-locaux-immobilier", "bg-white"),
    "negociation": ("rediger-annonce-immobiliere", "bg-light"),
    "marketing": ("intelligence-artificielle-immobilier", "bg-white"),
    "materiel": ("livres-negociation-immobiliere", None),
    "carriere": ("fidelisation-recommandation-immobilier", "bg-light"),
}
idx_path = os.path.join(BASE, "index.html")
with open(idx_path, encoding="utf-8") as f:
    html = f.read()

inserted = 0
for section, (anchor_slug, card_bg) in LAST_CARD.items():
    cards = [a for a in A if a["section"] == section]
    if not cards:
        continue
    # éviter les doublons si déjà inséré
    cards = [a for a in cards if f'/articles/{a["slug"]}' not in html]
    if not cards:
        continue
    if section == "materiel":
        cards_html = "\n".join(card_dark(a) for a in cards)
    else:
        cards_html = "\n".join(card_light(a, card_bg) for a in cards)
    # point d'ancrage : la balise </a> qui ferme la dernière carte de la section
    needle = f'/articles/{anchor_slug}'
    pos = html.find(needle)
    if pos == -1:
        print(f"⚠️  ancre introuvable pour {section}")
        continue
    close = html.find("</a>", pos)
    insert_at = close + len("</a>")
    html = html[:insert_at] + "\n" + cards_html + html[insert_at:]
    inserted += len(cards)
with open(idx_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"✅ {inserted} cartes insérées dans index.html")

# Patch sitemap.xml
sm_path = os.path.join(BASE, "sitemap.xml")
with open(sm_path, encoding="utf-8") as f:
    sm = f.read()
added = 0
entries = ""
for a in A:
    loc = f"https://mandatmaster.fr/articles/{a['slug']}"
    if loc in sm:
        continue
    entries += f"  <url>\n    <loc>{loc}</loc>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>\n"
    added += 1
if entries:
    sm = sm.replace("</urlset>", entries + "</urlset>")
    with open(sm_path, "w", encoding="utf-8") as f:
        f.write(sm)
print(f"✅ {added} URLs ajoutées au sitemap.xml")
