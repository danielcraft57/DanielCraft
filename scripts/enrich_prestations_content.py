#!/usr/bin/env python3
"""Ajoute contenu fiche détaillée aux prestations catalogue (has_page, exemples, FAQ, SEO)."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = ROOT / 'src' / 'data' / 'prestations.json'

# Contenu enrichi par slug (langage grand public)
ENRICHMENTS: dict[str, dict] = {
    'site-vitrine': {
        'examples': [
            'Un plombier à Metz veut une page « Nos services », « Tarifs indicatifs » et un formulaire : les clients appellent moins pour demander l\'adresse du site.',
            'Une boutique de pâtisserie affiche ses horaires, sa carte et un bouton « Commander par téléphone » visible dès l\'accueil sur mobile.',
        ],
        'promo': 'Premier pas en ligne sans engagement lourd : un site clair vaut souvent plus qu\'une page Facebook seule.',
    },
    'identite-harmonieuse': {
        'examples': [
            'Même logo, mêmes couleurs sur le site, la page Facebook et les devis PDF envoyés aux clients.',
            'Un artisan dont les photos Instagram et le site web ne se ressemblaient pas : une charte simple pour tout aligner.',
        ],
        'promo': 'Une image cohérente rassure avant même le premier rendez-vous.',
    },
    'visibilite-complete': {
        'examples': [
            'Un restaurant local apparaît sur Google Maps et ses horaires sont corrects quand on demande à un assistant « restaurants ouverts ce soir ».',
            'Un coach affiche une FAQ claire : Google et les assistants IA reprennent les mêmes réponses sur ses tarifs et sa zone.',
        ],
        'promo': 'Être trouvable aujourd\'hui, c\'est Google + les assistants que vos clients utilisent déjà.',
    },
    'referencement-google': {
        'examples': [
            'Correction des titres de pages (« Plombier Metz » au lieu de « Accueil ») : plus de clics depuis Google.',
            'Accélération du chargement sur mobile : moins de visiteurs qui repartent avant d\'avoir lu votre numéro.',
        ],
        'promo': 'Petit budget, impact mesurable : idéal si vous avez déjà un site mais peu de visites.',
    },
    'visible-assistants-ia': {
        'examples': [
            'Quand on demande « qui fait des sites vitrine à Metz », l\'assistant cite votre activité avec la bonne description.',
            'FAQ structurée sur vos délais et tarifs : reprise fidèle dans les réponses automatiques.',
        ],
        'promo': 'Vos futurs clients posent déjà leurs questions à ChatGPT — autant y être bien présenté.',
    },
    'repondeur-intelligent': {
        'examples': [
            'Un salon de coiffure : l\'assistant répond aux horaires, tarifs coupe et adresse pendant que vous êtes en prestation.',
            'Un cabinet comptable : questions sur les documents à apporter, réponses immédiates sur le site.',
        ],
        'promo': 'Comme un accueil téléphonique, mais sur votre site, 24 h/24.',
    },
    'aide-emails-clients': {
        'examples': [
            'Demande de devis reçue le soir : brouillon de réponse prêt le lendemain matin, vous n\'avez qu\'à relire et envoyer.',
            'Question récurrente sur les délais : l\'outil propose une réponse dans votre ton habituel.',
        ],
        'promo': 'Vous gardez le contrôle : l\'outil propose, vous validez avant envoi.',
    },
    'entretien-mensuel': {
        'examples': [
            'Mise à jour de sécurité appliquée sans que vous ayez à y penser.',
            'Petite typo sur la page Contact corrigée dans le quota mensuel inclus.',
        ],
        'promo': 'Moins cher qu\'une panne ou un piratage à réparer en urgence.',
    },
    'ia-contenus': {
        'has_page': True,
        'tagline': 'Des textes prêts à publier, dans votre ton',
        'description': 'Je rédige ou adapte les pages et articles de votre site à partir de vos informations métier. Vous recevez des textes clairs, sans jargon inutile, prêts à mettre en ligne ou à valider.',
        'benefits': ['Gain de temps sur la rédaction', 'Textes adaptés à votre clientèle', 'Meilleure visibilité sur Google'],
        'includes': ['Brief par échange ou questionnaire', 'Rédaction ou reprise de vos notes', 'Relecture et mise en forme web', '1 aller-retour de corrections'],
        'examples': [
            'Page « Nos services » pour un électricien : chaque prestation expliquée en langage simple.',
            'Trois articles de blog pour un naturopathe : sujets fréquents de ses patients, optimisés pour la recherche locale.',
        ],
        'promo': 'Vous savez quoi dire — je m\'occupe de le mettre par écrit correctement.',
        'faq': [
            {'q': 'Est-ce que les textes sont générés automatiquement ?', 'a': 'J\'utilise des outils d\'aide à la rédaction, mais chaque texte est relu, adapté à vous et validé avant livraison.'},
            {'q': 'Combien de pages sont incluses ?', 'a': 'Le forfait couvre l\'équivalent d\'environ 5 à 8 pages standard ; on précise ensemble au devis.'},
        ],
        'seo_title': 'Rédaction de textes pour site web — articles & pages',
        'seo_description': 'Textes clairs pour votre site vitrine ou blog. Rédaction adaptée à votre métier, sans jargon. Devis par e-mail, Metz & Lorraine.',
    },
    'ia-redaction': {
        'has_page': True,
        'tagline': 'Vos e-mails commerciaux, prêts plus vite',
        'description': 'Un assistant configuré avec votre offre et votre façon de parler. Il vous propose des brouillons pour devis, relances, messages LinkedIn ou newsletters — vous gardez la main sur l\'envoi.',
        'benefits': ['Moins de page blanche', 'Ton professionnel et cohérent', 'Réponses plus rapides aux prospects'],
        'includes': ['Configuration sur votre activité', 'Modèles pour vos cas fréquents', 'Courte formation à l\'usage', 'Ajustements après 2 semaines d\'essai'],
        'examples': [
            'Relance d\'un prospect qui n\'a pas répondu : proposition de message personnalisé en 2 minutes.',
            'Présentation de votre nouveau service sur LinkedIn : plusieurs variantes à choisir.',
        ],
        'promo': 'Idéal si vous prospectez seul et manquez de temps pour écrire.',
        'faq': [
            {'q': 'L\'outil envoie-t-il les e-mails à ma place ?', 'a': 'Non par défaut : il prépare le texte, vous copiez ou validez avant envoi depuis votre messagerie.'},
        ],
        'seo_title': 'Assistant rédaction commerciale — e-mails & LinkedIn',
        'seo_description': 'Gagnez du temps sur vos e-mails commerciaux et messages pro. Assistant configuré à votre image. Installation et accompagnement.',
    },
    'ia-analyse': {
        'has_page': True,
        'tagline': 'Vos chiffres expliqués simplement',
        'description': 'À partir de vos fichiers (ventes, stocks, rendez-vous…), je mets en place des tableaux de bord lisibles et des explications en français clair — pas besoin d\'être comptable pour comprendre.',
        'benefits': ['Vision claire de votre activité', 'Moins de tableurs à manipuler', 'Repérer ce qui marche (ou non)'],
        'includes': ['Analyse de vos sources de données', 'Tableau de bord adapté à votre métier', 'Documentation simple', 'Session de prise en main'],
        'examples': [
            'Un commerce suit ses ventes par mois et ses produits les plus demandés sans ouvrir dix fichiers Excel.',
            'Un indépendant visualise son chiffre d\'affaires et ses charges sur une seule page mise à jour.',
        ],
        'promo': 'Arrêtez de vous noyer dans les colonnes : voyez l\'essentiel d\'un coup d\'œil.',
        'faq': [
            {'q': 'Quels fichiers faut-il fournir ?', 'a': 'Export Excel, CSV ou accès à votre outil de facturation selon les cas — on définit cela au premier échange.'},
        ],
        'seo_title': 'Tableaux de bord & analyse de données — PME & indépendants',
        'seo_description': 'Comprenez vos chiffres avec des tableaux clairs et des explications accessibles. Pour commerces et indépendants en Lorraine.',
    },
    'ia-boutique': {
        'has_page': True,
        'tagline': 'Un vendeur disponible sur votre boutique en ligne',
        'description': 'Un assistant sur votre site e-commerce qui répond aux questions produits, tailles, délais de livraison et disponibilité — comme un conseiller en magasin, mais en ligne.',
        'benefits': ['Moins d\'abandons de panier', 'Réponses immédiates aux hésitations', 'Charge allégée sur le SAV'],
        'includes': ['Connexion à votre catalogue produits', 'Réponses sur les articles fréquents', 'Style adapté à votre marque', 'Tests avant mise en ligne'],
        'examples': [
            'Boutique de vêtements : « Quelle taille si je fais 1m75 ? » — réponse basée sur votre guide des tailles.',
            'Épicerie fine en ligne : l\'assistant suggère des accords ou précise les allergènes.',
        ],
        'promo': 'Vos clients posent les mêmes questions en magasin — autant y répondre sur le site.',
        'faq': [
            {'q': 'Fonctionne avec quelle boutique ?', 'a': 'Shopify, WooCommerce et la plupart des solutions courantes — faisabilité confirmée au devis.'},
        ],
        'seo_title': 'Assistant conversationnel e-commerce — conseil produits',
        'seo_description': 'Assistant sur votre boutique en ligne : questions produits, recommandations, aide à la commande. Installation clé en main.',
    },
    'ia-automatisation': {
        'has_page': True,
        'tagline': 'Fini le copier-coller entre vos outils',
        'description': 'Je configure des automatisations pour les tâches répétitives : tri d\'e-mails, extraction d\'infos de formulaires, rapports hebdomadaires… Vous gagnez des heures chaque mois.',
        'benefits': ['Moins d\'erreurs manuelles', 'Temps libéré pour le métier', 'Processus documentés'],
        'includes': ['Recensement de vos tâches répétitives', 'Mise en place des automatisations', 'Tests et ajustements', 'Notice d\'utilisation'],
        'examples': [
            'Chaque formulaire « devis » du site crée automatiquement une fiche dans votre tableur ou CRM.',
            'Rapport chaque lundi : nombre de demandes reçues la semaine précédente, sans compilation manuelle.',
        ],
        'promo': 'Si vous faites la même manipulation plus de 3 fois par semaine, on peut probablement l\'automatiser.',
        'faq': [
            {'q': 'Faut-il changer tous mes outils ?', 'a': 'Non : on part de ce que vous utilisez déjà (mail, Excel, Notion, etc.) et on les fait travailler ensemble.'},
        ],
        'seo_title': 'Automatisation de tâches — gain de temps PME',
        'seo_description': 'Automatisez e-mails, formulaires et rapports répétitifs. Moins de copier-coller, plus de temps pour vos clients.',
    },
    'ia-maint-mensuelle': {
        'has_page': True,
        'tagline': 'Votre assistant reste à jour chaque mois',
        'description': 'Abonnement mensuel pour actualiser les réponses de votre assistant (nouveaux tarifs, horaires d\'été, nouvelle prestation) et ajouter les questions que vos clients posent souvent.',
        'benefits': ['Réponses toujours exactes', 'Évolution sans repartir de zéro', 'Interlocuteur unique'],
        'includes': ['Mise à jour des connaissances', 'Ajout de questions/réponses', 'Petits ajustements de comportement', 'Rapport mensuel court'],
        'examples': [
            'Changement de tarif en janvier : toutes les réponses de l\'assistant mises à jour en 48 h.',
            'Nouvelle question récurrente détectée : ajoutée au mois suivant dans la base de l\'assistant.',
        ],
        'promo': 'Un assistant figé devient vite faux — cet abonnement évite les mauvaises surprises.',
        'faq': [
            {'q': 'Pour quel type d\'assistant ?', 'a': 'Assistants installés par DanielCraft ou existants — compatibilité vérifiée avant souscription.'},
        ],
        'seo_title': 'Maintenance mensuelle assistant IA — mises à jour',
        'seo_description': 'Abonnement entretien assistant : nouvelles réponses, tarifs à jour, optimisations. Pour sites et outils déjà en place.',
    },
    'ia-evolution': {
        'has_page': True,
        'tagline': 'Une nouvelle capacité pour votre assistant existant',
        'description': 'Votre assistant fonctionne déjà ? J\'ajoute une fonction : connexion à un nouvel outil, nouvelle source d\'information, prise de rendez-vous, etc.',
        'benefits': ['Sans tout refaire', 'Évolution progressive', 'Devis clair à l\'avance'],
        'includes': ['Analyse de faisabilité', 'Développement de la fonction', 'Tests', 'Mise en production'],
        'examples': [
            'L\'assistant peut maintenant consulter votre agenda pour proposer des créneaux.',
            'Connexion à votre FAQ Notion pour enrichir les réponses automatiquement.',
        ],
        'promo': 'À partir de 330 € selon la complexité — devis précis après description du besoin.',
        'faq': [
            {'q': 'Combien de temps ça prend ?', 'a': 'Souvent 3 à 10 jours ouvrés selon l\'intégration demandée.'},
        ],
        'seo_title': 'Évolution assistant IA — nouvelle fonctionnalité',
        'seo_description': 'Ajoutez une capacité à votre assistant existant : nouvel outil, source de données, prise de RDV. Devis sur mesure.',
    },
    'ia-audit': {
        'has_page': True,
        'tagline': 'Où l\'IA peut vraiment vous aider ?',
        'description': 'Bilan de votre activité et de vos habitudes : je repère les tâches où l\'IA apporte un gain réel (et celles où ce n\'est pas utile). Vous repartez avec un plan d\'action priorisé, sans jargon.',
        'benefits': ['Pas de dépense inutile', 'Idées concrètes pour votre métier', 'Feuille de route claire'],
        'includes': ['Entretien sur vos processus', 'Analyse des outils actuels', 'Rapport avec 5 à 10 recommandations', 'Échange de restitution (30 min)'],
        'examples': [
            'Un cabinet médical découvre que l\'IA peut aider sur les rappels de documents, pas sur le diagnostic.',
            'Un artisan identifie trois e-mails types à automatiser en priorité.',
        ],
        'promo': 'Avant d\'investir dans un gros projet IA, 400 € pour voir clair.',
        'faq': [
            {'q': 'Faut-il déjà utiliser l\'IA ?', 'a': 'Non : l\'audit convient aussi si vous débutez et voulez savoir par où commencer.'},
        ],
        'seo_title': 'Audit usage IA pour entreprises — bilan & recommandations',
        'seo_description': 'Audit IA en langage clair : où gagner du temps, quoi éviter. Rapport et plan d\'action pour PME et indépendants.',
    },
    'conseil-projet': {
        'has_page': True,
        'tagline': 'Un plan clair avant de vous lancer',
        'description': 'Vous avez un projet (nouveau site, application, grosse refonte) ? Je vous aide à voir ce qui est faisable, combien ça peut coûter et dans quel ordre avancer — sans vous vendre plus que nécessaire.',
        'benefits': ['Décisions éclairées', 'Budget et délais réalistes', 'Moins de mauvaises surprises'],
        'includes': ['Échange sur vos objectifs', 'Étude de faisabilité', 'Estimation budget et planning', 'Rapport écrit synthétique'],
        'examples': [
            'Refonte de site + boutique en ligne : trois scénarios (minimal, standard, complet) avec budgets.',
            'Connexion entre deux logiciels métier : faisable ou non, et alternatives proposées.',
        ],
        'promo': '380 € pour éviter de dépenser 5 000 € dans la mauvaise direction.',
        'faq': [
            {'q': 'Est-ce que vous réalisez ensuite le projet ?', 'a': 'Si vous le souhaitez, oui — mais le conseil reste utile même si vous travaillez avec un autre prestataire.'},
        ],
        'seo_title': 'Conseil projet web & digital — faisabilité & budget',
        'seo_description': 'Étude de faisabilité et estimation pour votre projet web ou digital. Rapport clair, sans engagement sur la suite.',
    },
    'connexion-crm': {
        'has_page': True,
        'tagline': 'Du site directement dans votre logiciel habituel',
        'description': 'Quand quelqu\'un remplit un formulaire sur votre site, les informations arrivent dans votre CRM, logiciel de devis ou tableur — plus besoin de recopier à la main.',
        'benefits': ['Zéro oubli de prospect', 'Gain de temps au quotidien', 'Données centralisées'],
        'includes': ['Analyse de vos outils', 'Connexion formulaire → logiciel', 'Tests avec fausses demandes', 'Courte documentation'],
        'examples': [
            'Formulaire contact → fiche automatique dans HubSpot ou Pipedrive.',
            'Demande de devis → ligne ajoutée dans votre fichier Excel partagé.',
        ],
        'promo': 'À partir de 290 € selon les logiciels à relier.',
        'faq': [
            {'q': 'Mon logiciel est-il compatible ?', 'a': 'La plupart des outils modernes oui — on vérifie ensemble avant de commencer.'},
        ],
        'seo_title': 'Connexion site web & CRM — synchronisation contacts',
        'seo_description': 'Reliez votre site à votre CRM ou logiciel métier. Formulaires, contacts et devis sans ressaisie manuelle.',
    },
    'transfert-donnees': {
        'has_page': True,
        'tagline': 'Vos anciennes données dans le nouvel outil',
        'description': 'Passage d\'un ancien site, d\'un tableur ou d\'un logiciel vers un nouveau système : je prépare le transfert proprement pour ne rien perdre (clients, produits, articles…).',
        'benefits': ['Pas de perte d\'historique', 'Transfert contrôlé', 'Vérification avant bascule'],
        'includes': ['Inventaire des données à migrer', 'Script ou import sécurisé', 'Contrôle après transfert', 'Rapport de migration'],
        'examples': [
            '500 fiches clients Excel importées dans un nouveau CRM.',
            'Articles d\'un ancien blog WordPress repris sur le nouveau site.',
        ],
        'promo': 'Indispensable lors d\'un changement de site ou d\'outil — mieux vaut le faire une fois bien.',
        'faq': [
            {'q': 'Y a-t-il une interruption de service ?', 'a': 'On planifie souvent le basculement en dehors des heures d\'ouverture ou le week-end.'},
        ],
        'seo_title': 'Migration de données — transfert site & logiciels',
        'seo_description': 'Transfert sécurisé de vos données (clients, produits, contenus) vers un nouvel outil ou site. Sans perte.',
    },
    'liaison-outils': {
        'has_page': True,
        'tagline': 'Vos applications qui se parlent enfin',
        'description': 'Deux logiciels qui ne communiquent pas ? Je mets en place la liaison pour que les infos circulent automatiquement (commande → stock, contact → facture…).',
        'benefits': ['Moins de double saisie', 'Données à jour partout', 'Processus fluides'],
        'includes': ['Cartographie du flux souhaité', 'Connexion API ou webhook', 'Tests de bout en bout', 'Support au démarrage'],
        'examples': [
            'Une vente sur la boutique met à jour le stock dans l\'outil de gestion.',
            'Un nouveau client dans le CRM déclenche l\'envoi d\'un e-mail de bienvenue.',
        ],
        'promo': 'À partir de 150 € pour une liaison simple — devis selon complexité.',
        'faq': [
            {'q': 'C\'est compliqué à maintenir ?', 'a': 'Je documente la liaison ; en cas de changement d\'outil, on évalue une mise à jour.'},
        ],
        'seo_title': 'Intégration API & webhooks — synchronisation outils',
        'seo_description': 'Faites dialoguer vos logiciels : commandes, stocks, contacts. Synchronisation automatique pour PME.',
    },
    'rapport-vitesse': {
        'has_page': True,
        'tagline': 'Votre site charge-t-il assez vite ?',
        'description': 'Mesure complète de la vitesse de votre site sur mobile et ordinateur. Vous recevez un rapport en français clair : ce qui ralentit et quoi améliorer en priorité.',
        'benefits': ['Comprendre pourquoi les visiteurs partent', 'Liste d\'actions prioritaires', 'Pas de jargon technique'],
        'includes': ['Test de performance', 'Analyse mobile + desktop', 'Rapport PDF ou page web', 'Échange de 20 min pour expliquer'],
        'examples': [
            'Images trop lourdes identifiées : gain de 3 secondes au chargement après correction.',
            'Site lent sur 4G : rapport montrant les 3 blocages principaux.',
        ],
        'promo': '120 € pour un diagnostic — souvent rentabilisé par plus de contacts.',
        'faq': [
            {'q': 'Est-ce que vous corrigez aussi ?', 'a': 'Le forfait couvre le rapport ; les corrections peuvent faire l\'objet d\'un devis séparé.'},
        ],
        'seo_title': 'Audit vitesse site web — rapport performances',
        'seo_description': 'Votre site est-il rapide ? Mesure et rapport clair avec recommandations. Pour commerces et sites vitrine.',
    },
    'page-supplementaire': {
        'has_page': True,
        'tagline': 'Une page de plus sur votre site, clé en main',
        'description': 'Besoin d\'une page Témoignages, Tarifs, Équipe ou FAQ ? Je la crée avec la même charte que votre site actuel, textes et mise en page inclus.',
        'benefits': ['Site plus complet', 'Cohérence visuelle', 'Mise en ligne rapide'],
        'includes': ['Structure de la page', 'Intégration au menu', 'Mise en forme responsive', '1 série de retours'],
        'examples': [
            'Page « Nos réalisations » avec galerie photos pour un paysagiste.',
            'Page « Mentions légales & politique de confidentialité » mise à jour.',
        ],
        'promo': '65 € par page — idéal pour compléter un site vitrine existant.',
        'faq': [
            {'q': 'Faut-il fournir les textes ?', 'a': 'Vous pouvez fournir une ébauche ; je peux aussi rédiger (option possible).'},
        ],
        'seo_title': 'Ajout page site vitrine — création sur mesure',
        'seo_description': 'Nouvelle page pour votre site vitrine : témoignages, tarifs, FAQ. 65 €/page, mise en ligne incluse.',
    },
    'formulaire-sur-mesure': {
        'has_page': True,
        'tagline': 'Le bon formulaire pour votre activité',
        'description': 'Formulaire de contact enrichi, demande de devis détaillée, réservation ou questionnaire : champs adaptés à votre métier, envoi par e-mail ou vers votre outil.',
        'benefits': ['Demandes mieux qualifiées', 'Moins d\'allers-retours', 'Image professionnelle'],
        'includes': ['Définition des champs utiles', 'Validation des saisies', 'Envoi e-mail ou export', 'Intégration sur votre site'],
        'examples': [
            'Formulaire devis avec type de travaux, surface et photos pour un artisan.',
            'Prise de rendez-vous avec choix de créneau pour un cabinet.',
        ],
        'promo': '99 € forfait — souvent indispensable pour convertir les visiteurs.',
        'faq': [
            {'q': 'Peut-on connecter à mon CRM ?', 'a': 'Oui, en option via la prestation « Relier votre site à votre logiciel ».'},
        ],
        'seo_title': 'Formulaire web sur mesure — devis & contact',
        'seo_description': 'Formulaire adapté à votre activité : devis, réservation, questionnaire. Validation et envoi par e-mail.',
    },
    'nouveau-look': {
        'has_page': True,
        'tagline': 'Un site rafraîchi sans tout reconstruire',
        'description': 'Votre site fonctionne mais a vieilli visuellement ? Je modernise couleurs, polices et mise en page en gardant vos textes et la structure actuelle.',
        'benefits': ['Image plus actuelle', 'Coût maîtrisé', 'Pas de migration lourde'],
        'includes': ['Proposition de palette et typos', 'Application sur les pages existantes', 'Vérification mobile', 'Mise en ligne'],
        'examples': [
            'Site de 2018 : nouveau header, couleurs et boutons — aspect 2025 en quelques jours.',
            'Harmonisation avec une nouvelle carte de visite imprimée.',
        ],
        'promo': '330 € pour un coup de jeune visible sans refonte complète.',
        'faq': [
            {'q': 'Est-ce que le contenu change ?', 'a': 'Non par défaut : uniquement l\'apparence. Les textes peuvent être mis à jour via un pack contenu séparé.'},
        ],
        'seo_title': 'Refonte visuelle site web — design & couleurs',
        'seo_description': 'Rafraîchissez l\'apparence de votre site : couleurs, polices, mise en page. Sans reconstruire tout le site.',
    },
    'maj-contenus': {
        'has_page': True,
        'tagline': '5 heures pour mettre votre site à jour',
        'description': 'Pack de 5 heures pour modifier textes, photos, horaires, tarifs ou pages sur votre site existant. Vous listez les changements, je les réalise.',
        'benefits': ['Site à jour rapidement', 'Pas besoin de formation technique', 'Heures utilisables sur plusieurs petits sujets'],
        'includes': ['Jusqu\'à 5 h de modifications', 'Mises à jour textes et images', 'Petites retouches de mise en page', 'Compte-rendu des changements'],
        'examples': [
            'Horaires d\'été, nouveau numéro de téléphone et photo d\'équipe remplacée.',
            'Ajout de trois nouveaux services sur la page Prestations.',
        ],
        'promo': '170 € le pack — pratique une ou deux fois par an.',
        'faq': [
            {'q': 'Que se passe-t-il si ça dépasse 5 h ?', 'a': 'Je vous préviens avant ; le surplus peut être facturé à l\'heure ou reporté sur un nouveau pack.'},
        ],
        'seo_title': 'Mise à jour contenu site web — pack 5 heures',
        'seo_description': 'Pack 5 h pour actualiser textes, images et pages de votre site. Simple et sans jargon technique.',
    },
    'hebergement-domaine': {
        'has_page': True,
        'tagline': 'Votre adresse www en ligne toute l\'année',
        'description': 'Hébergement fiable pour votre site et gestion de votre nom de domaine (www.monsite.fr). Renouvellement et réglages techniques inclus pour l\'année.',
        'benefits': ['Site accessible 24 h/24', 'Un interlocuteur pour le domaine', 'Moins de paperasse technique'],
        'includes': ['Hébergement web annuel', 'Nom de domaine .fr ou .com', 'Certificat HTTPS de base', 'Support pour la mise en ligne'],
        'examples': [
            'Artisan qui veut « monsite.fr » sans gérer OVH ou Gandi lui-même.',
            'Renouvellement annuel du domaine géré en un seul contact.',
        ],
        'promo': '79 €/an — souvent couplé à la maintenance mensuelle.',
        'faq': [
            {'q': 'Le site est-il créé dans ce forfait ?', 'a': 'Non : c\'est l\'hébergement et le domaine. La création du site est une prestation séparée.'},
        ],
        'seo_title': 'Hébergement web & nom de domaine — forfait annuel',
        'seo_description': 'Hébergement et nom de domaine pour votre site pro. 79 €/an, HTTPS inclus. Metz & France.',
    },
    'sauvegardes-securite': {
        'has_page': True,
        'tagline': 'Votre site protégé et sauvegardé',
        'description': 'Mise en place de copies automatiques de votre site et réglages de sécurité (HTTPS, protections de base). En cas de problème, on peut restaurer une version récente.',
        'benefits': ['Sommeil tranquille', 'Récupération possible après incident', 'Moins de risques de piratage'],
        'includes': ['Sauvegardes automatiques planifiées', 'Renforcement sécurité', 'Vérification HTTPS', 'Procédure de restauration documentée'],
        'examples': [
            'Site piraté : restauration de la veille en quelques heures.',
            'Mise à jour de sécurité bloquée : retour arrière grâce à la sauvegarde.',
        ],
        'promo': '99 € une fois — à combiner avec la maintenance mensuelle pour la surveillance.',
        'faq': [
            {'q': 'Où sont stockées les sauvegardes ?', 'a': 'Sur un espace séparé de l\'hébergement principal, pas sur le même serveur que le site.'},
        ],
        'seo_title': 'Sauvegarde & sécurité site web',
        'seo_description': 'Sauvegardes automatiques et sécurisation de votre site. Protection et restauration en cas d\'incident.',
    },
    'https-site': {
        'has_page': True,
        'tagline': 'Le cadenas vert sur votre adresse web',
        'description': 'Installation du certificat HTTPS pour afficher le cadenas dans le navigateur. Indispensable pour la confiance des visiteurs et pour Google.',
        'benefits': ['Visiteurs rassurés', 'Meilleure image professionnelle', 'Exigence Google respectée'],
        'includes': ['Certificat SSL', 'Configuration sur l\'hébergement', 'Redirection http → https', 'Test sur navigateurs courants'],
        'examples': [
            'Site encore en « non sécurisé » : correction en une demi-journée.',
            'Avertissement Chrome supprimé après installation du certificat.',
        ],
        'promo': '45 € — rapide et souvent oublié sur les vieux sites.',
        'faq': [
            {'q': 'C\'est obligatoire ?', 'a': 'Pas légalement pour tous, mais fortement recommandé : les navigateurs affichent des avertissements sans HTTPS.'},
        ],
        'seo_title': 'Certificat SSL HTTPS — installation site web',
        'seo_description': 'Installation du cadenas HTTPS sur votre site. 45 € forfait, configuration complète.',
    },
    'support-mensuel': {
        'has_page': True,
        'tagline': 'Une aide par e-mail chaque mois',
        'description': 'Abonnement léger pour poser vos questions techniques par e-mail : petites modifications, conseils, orientation quand vous êtes bloqué sur votre site.',
        'benefits': ['Pas seul face au technique', 'Réponse sous quelques jours ouvrés', 'Budget prévisible'],
        'includes': ['Support par e-mail', 'Petites questions et orientations', 'Mises à jour mineures simples', 'Historique de vos demandes'],
        'examples': [
            '« Comment changer cette image sur l\'accueil ? » — réponse pas à pas.',
            '« Mon formulaire ne part plus » — diagnostic et correction simple.',
        ],
        'promo': '25 €/mois — l\'alternative douce à l\'accompagnement à l\'heure.',
        'faq': [
            {'q': 'Qu\'est-ce qui n\'est pas inclus ?', 'a': 'Les gros développements ou refontes : ils font l\'objet d\'un devis séparé.'},
        ],
        'seo_title': 'Support technique site web — abonnement mensuel',
        'seo_description': 'Assistance par e-mail pour votre site : questions, petites corrections. 25 €/mois, sans engagement long.',
    },
    'depannage-2h': {
        'has_page': True,
        'tagline': '2 heures pour débloquer la situation',
        'description': 'Bug, page blanche, formulaire cassé ou petite évolution urgente : intervention ciblée de 2 heures pour remettre d\'aplomb ou avancer concrètement.',
        'benefits': ['Réaction rapide', 'Forfait connu à l\'avance', 'Pas de surprise sur la durée'],
        'includes': ['Jusqu\'à 2 h d\'intervention', 'Diagnostic du problème', 'Correction ou contournement', 'Compte-rendu court'],
        'examples': [
            'Site affiche une erreur après une mise à jour : retour en ligne le jour même.',
            'Lien mort sur la page Contact réparé + test du formulaire.',
        ],
        'promo': '120 € forfait 2 h — à réserver quand ça presse.',
        'faq': [
            {'q': 'Et si 2 h ne suffisent pas ?', 'a': 'Je vous préviens avant de dépasser ; on peut étendre à l\'heure ou planifier une suite.'},
        ],
        'seo_title': 'Dépannage site web — intervention 2 heures',
        'seo_description': 'Dépannage express site internet : bug, page cassée, correctif. Forfait 2 h, 120 €.',
    },
    'accompagnement-heure': {
        'has_page': True,
        'tagline': 'Conseil et aide pas à pas, à l\'heure',
        'description': 'Vous gérez votre site vous-même mais avez besoin d\'un coup de main ? Je vous accompagne à l\'heure : conseil, relecture, aide à la mise en place d\'une fonctionnalité.',
        'benefits': ['Flexible', 'Vous apprenez en faisant', 'Payez seulement le temps utile'],
        'includes': ['Visio ou échange écrit', 'Conseils adaptés à votre niveau', 'Démonstrations pas à pas', 'Compte-rendu si besoin'],
        'examples': [
            '1 h pour comprendre comment mettre à jour les horaires vous-même.',
            '2 h pour configurer un outil de prise de rendez-vous avec mon aide.',
        ],
        'promo': '60 €/h — sans engagement minimum.',
        'faq': [
            {'q': 'Facturation au quart d\'heure ?', 'a': 'Facturation à l\'heure entamée, avec transparence sur le temps passé.'},
        ],
        'seo_title': 'Accompagnement technique — conseil à l\'heure',
        'seo_description': 'Aide et conseil pour votre site, à l\'heure. Débutants bienvenus, explications claires. 60 €/h.',
    },
    'support-prioritaire': {
        'has_page': True,
        'tagline': 'Réponse rapide quand vous êtes bloqué',
        'description': 'Même principe que l\'accompagnement à l\'heure, avec priorité de traitement : pour les situations urgentes (site en panne avant un événement, lancement imminent…).',
        'benefits': ['Délai de réponse raccourci', 'Intervention en urgence possible', 'Sérénité avant une échéance'],
        'includes': ['Canal prioritaire', 'Prise en charge rapide', 'Jusqu\'à 1 h incluse selon cas', 'Suivi jusqu\'à résolution'],
        'examples': [
            'Site inaccessible la veille d\'une promo : traitement en priorité.',
            'Formulaire d\'inscription événement à réparer avant l\'ouverture des ventes.',
        ],
        'promo': '70 €/h — quand chaque heure compte.',
        'faq': [
            {'q': 'Disponible le week-end ?', 'a': 'Sur demande et selon disponibilité — précisez l\'urgence dans votre message.'},
        ],
        'seo_title': 'Support prioritaire site web — intervention urgente',
        'seo_description': 'Support technique prioritaire pour urgences web. Réponse rapide, 70 €/h. Metz & remote.',
    },
}


def main() -> None:
    data = json.loads(JSON_PATH.read_text(encoding='utf-8'))
    for item in data.get('items', []):
        slug = (item.get('slug') or '').strip()
        extra = ENRICHMENTS.get(slug)
        if not extra:
            continue
        for key, value in extra.items():
            item[key] = value
        if extra.get('has_page'):
            item['has_page'] = True
    JSON_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + '\n',
        encoding='utf-8',
    )
    pages = sum(1 for i in data['items'] if i.get('has_page'))
    print(f'[OK] {pages} prestation(s) avec page détaillée')


if __name__ == '__main__':
    main()
