"use client";

import React, { useState } from 'react';
import {
    Building2,
    MessageSquare,
    FileText,
    Star,
    Check,
    ShieldCheck,
    Download,
    ChevronRight,
    Key,
    Users,
    Target,
    PenTool,
    Phone
} from 'lucide-react';

export default function Home() {
    const [email, setEmail] = useState('');

    const benefits = [
        {
            icon: <Target size={24} className="text-secondary" />,
            title: "Plus de Mandats",
            desc: "Arrêtez de courir après les prospects. Laissez-les venir à vous avec une communication pro."
        },
        {
            icon: <PenTool size={24} className="text-secondary" />,
            title: "Gain de Temps",
            desc: "50 templates prêts à l'emploi. Copiez, collez, publiez. 80% de votre temps récupéré."
        },
        {
            icon: <ShieldCheck size={24} className="text-secondary" />,
            title: "Crédibilité Immédiate",
            desc: "Passez pour l'expert du secteur avec des dossiers d'estimation ultra-qualitatifs."
        }
    ];

    const modules = [
        {
            title: "Module 1 : Visibilité Immédiate",
            subtitle: "50 Templates Canva & Réseaux Sociaux",
            features: [
                "10 Posts 'Nouveau bien à la vente'",
                "10 Posts 'Vendu en 24h' (Preuve sociale)",
                "10 Posts 'Conseils Immo' (Éducation)",
                "5 Bannières LinkedIn/Facebook Pro",
                "Templates de Story à la une"
            ],
            icon: <Users size={32} />
        },
        {
            title: "Module 2 : Prospection Invincible",
            subtitle: "Scripts & Méthodes de Vente",
            features: [
                "10 Scripts Téléphoniques (Pige & Relance)",
                "20 Modèles de SMS/WhatsApp à copier-coller",
                "5 Emails de Nurturing (Suivi prospect)",
                "Trame de réponse aux objections",
                "Guide : Transformer un lead en mandat"
            ],
            icon: <Phone size={32} />
        },
        {
            title: "Module 3 : Estimation Gagnante",
            subtitle: "Dossiers & Outils Print",
            features: [
                "Modèle de Dossier d'Estimation (Word/Canva)",
                "Flyer 'Recherche de biens' pour boîtage",
                "Checklist 'Préparer votre vente'",
                "Fiche découverte acquéreur",
                "Bon de visite professionnel"
            ],
            icon: <FileText size={32} />
        }
    ];

    return (
        <div className="min-h-screen bg-light text-dark font-sans">
            {/* NAVBAR */}
            <nav className="border-b border-gray-200 bg-white/80 backdrop-blur-md sticky top-0 z-50">
                <div className="container mx-auto px-4 h-16 flex items-center justify-between">
                    <div className="flex items-center gap-2 font-bold text-xl text-primary">
                        <Building2 size={24} />
                        MandatMaster
                    </div>
                    <a href="#pricing" className="bg-primary text-white px-5 py-2 rounded-full font-medium hover:bg-blue-700 transition">
                        Télécharger le Kit
                    </a>
                </div>
            </nav>

            {/* HERO SECTION */}
            <header className="py-20 lg:py-32 overflow-hidden relative">
                <div className="absolute inset-0 bg-gradient-to-br from-blue-50 to-amber-50 -z-10" />
                <div className="container mx-auto px-4 text-center max-w-4xl">
                    <div className="inline-flex items-center gap-2 bg-blue-100 text-primary px-4 py-1.5 rounded-full text-sm font-semibold mb-6">
                        <Star size={14} fill="currentColor" /> Nouveau pour 2026
                    </div>
                    <h1 className="text-4xl lg:text-6xl font-extrabold tracking-tight mb-6 text-dark leading-tight">
                        Décrochez plus de mandats exclusifs <span className="text-primary">sans y passer vos soirées.</span>
                    </h1>
                    <p className="text-xl text-gray-600 mb-10 max-w-2xl mx-auto">
                        Le kit tout-en-un pour les agents immobiliers indépendants : 50+ templates,
                        scripts de prospection et outils d'estimation pour doubler votre CA.
                    </p>
                    <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
                        <a href="#pricing" className="w-full sm:w-auto bg-primary text-white px-8 py-4 rounded-lg font-bold text-lg hover:bg-blue-700 transition shadow-lg shadow-blue-500/25 flex items-center justify-center gap-2">
                            <Download size={20} /> Obtenir le Kit Complet
                        </a>
                        <div className="flex items-center gap-2 text-sm text-gray-500">
                            <div className="flex -space-x-2">
                                {[1, 2, 3, 4].map(i => (
                                    <div key={i} className="w-8 h-8 rounded-full bg-gray-200 border-2 border-white flex items-center justify-center text-xs font-bold text-gray-500">
                                        {String.fromCharCode(64 + i)}
                                    </div>
                                ))}
                            </div>
                            <span className="font-medium">+400 agents l'utilisent</span>
                        </div>
                    </div>
                </div>
            </header>

            {/* PROBLEMS / SOLUTIONS */}
            <section className="py-20 bg-white">
                <div className="container mx-auto px-4">
                    <div className="grid md:grid-cols-3 gap-8">
                        {benefits.map((benefit, idx) => (
                            <div key={idx} className="p-6 rounded-2xl bg-gray-50 border border-gray-100 hover:border-primary/20 transition group">
                                <div className="w-12 h-12 bg-white rounded-xl shadow-sm flex items-center justify-center mb-4 text-primary group-hover:scale-110 transition">
                                    {benefit.icon}
                                </div>
                                <h3 className="text-xl font-bold mb-2">{benefit.title}</h3>
                                <p className="text-gray-600">{benefit.desc}</p>
                            </div>
                        ))}
                    </div>
                </div>
            </section>

            {/* MODULES DETAIL */}
            <section className="py-20 bg-dark text-white">
                <div className="container mx-auto px-4">
                    <div className="text-center mb-16">
                        <h2 className="text-3xl lg:text-4xl font-bold mb-4">Tout ce qu'il vous faut pour closer</h2>
                        <p className="text-gray-400">Fini le syndrome de la page blanche et les estimations bricolées.</p>
                    </div>

                    <div className="grid lg:grid-cols-3 gap-8">
                        {modules.map((module, idx) => (
                            <div key={idx} className="bg-gray-800 rounded-2xl p-8 border border-gray-700 hover:border-secondary/50 transition relative overflow-hidden">
                                <div className="absolute top-0 right-0 p-4 opacity-10">
                                    {module.icon}
                                </div>
                                <div className="text-secondary font-bold text-sm mb-2 uppercase tracking-wider">
                                    {module.title.split(':')[0]}
                                </div>
                                <h3 className="text-2xl font-bold mb-6">{module.title.split(':')[1]}</h3>
                                <ul className="space-y-3">
                                    {module.features.map((feature, fIdx) => (
                                        <li key={fIdx} className="flex items-start gap-3 text-gray-300">
                                            <Check size={18} className="text-primary mt-1 shrink-0" />
                                            <span>{feature}</span>
                                        </li>
                                    ))}
                                </ul>
                            </div>
                        ))}
                    </div>
                </div>
            </section>

            {/* PRICING */}
            <section id="pricing" className="py-24 bg-gradient-to-b from-gray-50 to-white">
                <div className="container mx-auto px-4 max-w-5xl">
                    <div className="bg-white rounded-3xl shadow-xl overflow-hidden border border-gray-200 flex flex-col lg:flex-row">
                        <div className="p-10 lg:p-14 lg:w-3/5">
                            <h2 className="text-3xl font-bold mb-6">Prêt à transformer votre business ?</h2>
                            <p className="text-gray-600 mb-8 text-lg">
                                Rejoignez les agents qui passent plus de temps à signer des mandats et moins de temps à chercher quoi poster sur Instagram.
                            </p>

                            <div className="space-y-4 mb-8">
                                <div className="flex items-center gap-3">
                                    <div className="w-10 h-10 rounded-full bg-green-100 flex items-center justify-center text-green-600">
                                        <Key size={20} />
                                    </div>
                                    <div>
                                        <div className="font-bold">Accès à vie</div>
                                        <div className="text-sm text-gray-500">Mises à jour incluses gratuitement</div>
                                    </div>
                                </div>
                                <div className="flex items-center gap-3">
                                    <div className="w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center text-blue-600">
                                        <Download size={20} />
                                    </div>
                                    <div>
                                        <div className="font-bold">Téléchargement immédiat</div>
                                        <div className="text-sm text-gray-500">Commencez dans 2 minutes</div>
                                    </div>
                                </div>
                            </div>

                            <div className="flex items-center gap-4 text-xs text-gray-400">
                                <ShieldCheck size={16} /> Paiement 100% sécurisé via Stripe
                            </div>
                        </div>

                        <div className="bg-primary p-10 lg:p-14 lg:w-2/5 text-white flex flex-col justify-center relative overflow-hidden">
                            <div className="absolute top-0 right-0 bg-secondary text-dark text-xs font-bold px-3 py-1 rounded-bl-lg">
                                OFFRE DE LANCEMENT
                            </div>

                            <div className="text-center">
                                <div className="text-gray-200 mb-2 line-through text-lg">Valeur réelle : 197€</div>
                                <div className="text-5xl font-extrabold mb-2">47€</div>
                                <div className="text-blue-200 text-sm mb-8">Paiement unique</div>

                                <button
                                    onClick={() => alert("Le système de paiement Stripe sera connecté prochainement. Ceci est une démonstration.")}
                                    className="w-full bg-secondary text-dark font-bold py-4 rounded-xl hover:bg-amber-400 transition transform hover:scale-105 shadow-lg"
                                >
                                    Accéder au Kit maintenant
                                </button>
                                <div className="mt-4 text-xs text-blue-200 text-center">
                                    Garantie satisfait ou remboursé 30 jours
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            {/* FOOTER */}
            <footer className="bg-gray-50 py-12 border-t border-gray-200 text-center text-gray-500 text-sm">
                <div className="container mx-auto px-4">
                    <p className="mb-4">© 2026 MandatMaster. Tous droits réservés.</p>
                    <div className="flex justify-center gap-6">
                        <a href="#" className="hover:text-primary">Mentions Légales</a>
                        <a href="#" className="hover:text-primary">Conditions Générales de Vente</a>
                        <a href="#" className="hover:text-primary">Contact</a>
                    </div>
                </div>
            </footer>
        </div>
    );
}
