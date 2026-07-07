"""Scénarios narratifs pour vitrines multi-pages DanielCraft."""
from __future__ import annotations

SCENE_TYPE_BY_SLUG: dict[str, str] = {
    "restauration": "food",
    "beaute": "spa",
    "odontologie": "medical",
    "automobile": "garage",
    "commerce": "retail",
    "comptable": "office",
    "industrie": "industrial",
    "immobilier": "property",
    "juridique": "legal",
    "architecture": "architecture",
    "fitness": "sport",
    "photographie": "photo",
    "association": "team",
    "education": "interior",
    "services": "office",
    "etablissement": "interior",
    "technologie": "saas_ui",
    "saas-landing": "saas_ui",
    "saas-onboarding": "saas_ui",
    "saas-dashboard": "saas_ui",
    "saas-empty": "saas_ui",
    "saas-notifications": "saas_ui"
}

SCENARIOS: list[dict] = [
    {
        "slug": 'restauration',
        "brand": 'Brasserie Saint-Jacques',
        "category": 'hcr',
        "layout": 'brasserie',
        "nav_cta": 'Réserver',
        "synopsis": 'Face à la cathédrale de Metz, une brasserie lorraine où le bouchée-à-la-reine rencontre la bière artisanale du pays.',
        "nav": [
            {
                "file": 'index.html',
                "label": 'Accueil',
            },
            {
                "file": 'carte.html',
                "label": 'La carte',
            },
            {
                "file": 'histoire.html',
                "label": 'Notre histoire',
            },
            {
                "file": 'contact.html',
                "label": 'Contact',
            },
        ],
        "pages": [
            {
                "file": 'index.html',
                "title": 'Brasserie Saint-Jacques — Accueil',
                "description": 'Brasserie historique à Metz : cuisine lorraine, terrasse place Saint-Jacques et réservation en ligne.',
                "hero": {
                    "h1": 'La table qui réchauffe Metz depuis 1924',
                    "lead": 'Terrasse sur la place, mijotés au feu de bois et carte des vins mosellans.',
                    "img": 'hero.png',
                    "alt": 'Salle de brasserie chaleureuse avec verrière à Metz',
                },
                "story": ('Une adresse qui traverse les générations', ["Installée dans l'ancienne maison du maître d'hôtel de la gare impériale, la brasserie a survécu aux guerres en gardant son zinc d'origine.", 'Le chef Élodie Marchal revisite le patrimoine culinaire mosellan : quiche au fromage de cow-gomme et mirabelle en dessert.']),
                "chapters": [
                    {
                        "title": 'Le feu de la cuisine',
                        "text": 'Four à bois et casseroles en cuivre derrière le passe.',
                        "img": 'scene-1.png',
                        "alt": 'Cuisine ouverte avec flammes à Metz',
                    },
                    {
                        "title": 'La cave mosellane',
                        "text": 'Quarante-cinq références de vignerons de la vallée de la Moselle.',
                        "img": 'scene-2.png',
                        "alt": 'Cave à vin mosellane',
                    },
                    {
                        "title": 'La terrasse des Messins',
                        "text": 'Face à la cathédrale, apéritif et tapas lorrains au soleil.',
                        "img": 'scene-3.png',
                        "alt": 'Terrasse face à la cathédrale de Metz',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Service du midi sous la verrière',
                        "alt": 'Déjeuner animé place Saint-Jacques',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Soirée jazz au comptoir',
                        "alt": 'Vendredis live dans la salle',
                    },
                ],
                "cards": {
                    "title": 'Nos signatures',
                    "items": [
                        {
                            "title": 'Menu du marché',
                            "text": 'Carte renouvelée chaque semaine selon le marché Saint-Jacques.',
                            "img": 'card-1.png',
                            "alt": 'Assiette gastronomique lorraine',
                        },
                        {
                            "title": 'Brunch dominical',
                            "text": 'Brioche perdue à la mirabelle — réservation conseillée.',
                            "img": 'card-2.png',
                            "alt": 'Brunch dominical',
                        },
                        {
                            "title": 'Privatisation',
                            "text": 'Salon du premier pour 40 couverts.',
                            "img": 'card-3.png',
                            "alt": 'Salon privatisé',
                        },
                    ],
                },
                "cta": {
                    "text": 'Réservez votre table — la terrasse se remplit vite.',
                    "btn": 'Réserver',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'carte.html',
                "title": 'La carte — Brasserie Saint-Jacques',
                "description": 'Carte saisonnière : entrées lorraines, plats mijotés et bières artisanales.',
                "hero": {
                    "h1": 'Une carte qui suit les saisons mosellanes',
                    "lead": 'Du marché à votre assiette.',
                    "img": 'hero.png',
                    "alt": 'Plats colorés en cuisine lorraine',
                },
                "story": ('Produits du terroir', ['Fournisseurs à moins de 80 km : maraîchers de Hagondange, fromager de Saint-Hubert.']),
                "cards": {
                    "title": 'Entrées & plats',
                    "items": [
                        {
                            "title": 'Entrées',
                            "text": "Terrine de canard, salade Munster, soupe à l'oignon.",
                            "img": 'card-1.png',
                            "alt": 'Entrées lorraines',
                        },
                        {
                            "title": 'Plats',
                            "text": 'Bouchée à la reine, jarret confit, sandre du canal.',
                            "img": 'card-2.png',
                            "alt": 'Plat mijoté en cocotte',
                        },
                        {
                            "title": 'Desserts',
                            "text": 'Tarte aux quetsches et clafoutis mirabelle.',
                            "img": 'card-3.png',
                            "alt": 'Dessert à la mirabelle',
                        },
                    ],
                },
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Carte des vins mosellans',
                        "alt": 'Dégustation au verre',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Bières artisanales',
                        "alt": 'Pression et bouteilles locales',
                    },
                ],
                "cta": {
                    "text": 'Allergies ? Prévenez-nous à la réservation.',
                    "btn": 'Nous contacter',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'histoire.html',
                "title": 'Notre histoire — Brasserie Saint-Jacques',
                "description": "Cent ans d'histoire gastronomique au cœur de Metz.",
                "hero": {
                    "h1": 'Cent ans de convivialité messine',
                    "lead": "De l'auberge des voyageurs à la brasserie contemporaine.",
                    "img": 'hero.png',
                    "alt": 'Façade historique en pierre jaune',
                },
                "timeline": [('1924', "Ouverture de l'auberge Saint-Jacques pour les cheminots."), ('1958', "Transformation en brasserie avec zinc d'époque."), ('2003', 'Rénovation de la verrière Art déco.'), ('2019', 'Élodie Marchal reprend les fourneaux.')],
                "chapters": [
                    {
                        "title": 'La verrière',
                        "text": "Chef-d'œuvre Art déco restauré pièce par pièce.",
                        "img": 'scene-1.png',
                        "alt": 'Verrière de brasserie historique',
                    },
                    {
                        "title": 'Le zinc',
                        "text": "Comptoir d'origine où les habitués prennent leur café.",
                        "img": 'scene-2.png',
                        "alt": 'Comptoir en zinc de brasserie',
                    },
                    {
                        "title": 'Les archives',
                        "text": 'Photos de famille et menus jaunis dans le couloir.',
                        "img": 'scene-3.png',
                        "alt": 'Archives historiques du restaurant',
                    },
                ],
                "cta": {
                    "text": 'Visite guidée le premier samedi du mois.',
                    "btn": 'Réserver une visite',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'contact.html',
                "title": 'Contact — Brasserie Saint-Jacques',
                "description": 'Réservez votre table à Metz, place Saint-Jacques.',
                "hero": {
                    "h1": 'Réserver ou nous écrire',
                    "lead": '12 place Saint-Jacques, 57000 Metz.',
                    "img": 'hero.png',
                    "alt": 'Entrée de brasserie à Metz',
                },
                "story": ('Nous trouver', ['Ouvert mar–sam midi et soir. Dimanche brunch 10h–15h. Tél. 03 87 75 12 34.']),
                "cta": {
                    "text": 'Groupes de 8+ : menu sur mesure.',
                    "btn": 'Envoyer ma demande',
                    "href": '#',
                },
            },
        ],
    },
    {
        "slug": 'beaute',
        "brand": 'Spa Thalie',
        "category": 'beaute',
        "layout": 'spa',
        "nav_cta": 'Prendre RDV',
        "synopsis": 'Institut de beauté et spa urbain à Nancy, entre relaxation et soins haute performance.',
        "nav": [
            {
                "file": 'index.html',
                "label": 'Accueil',
            },
            {
                "file": 'soins.html',
                "label": 'Nos soins',
            },
            {
                "file": 'ambiance.html',
                "label": "L'institut",
            },
            {
                "file": 'contact.html',
                "label": 'Contact',
            },
        ],
        "pages": [
            {
                "file": 'index.html',
                "title": 'Spa Thalie — Institut & spa à Nancy',
                "description": 'Spa urbain à Nancy : soins visage, massages et rituels bien-être.',
                "hero": {
                    "h1": 'Votre parenthèse bien-être au cœur de Nancy',
                    "lead": 'Maison de maître rue Stanislas : expertise esthétique et rituels sensoriels.',
                    "img": 'hero.png',
                    "alt": 'Spa lumineux avec fauteuils à Nancy',
                },
                "story": ("L'art du soin, version Lorraine", ['Fondé par deux esthéticiennes formées à Paris, Thalie mise sur des protocoles sur-mesure et produits clean.', 'Chaque visite commence par un diagnostic de peau et finit par un thé bio.']),
                "chapters": [
                    {
                        "title": 'Cabine signature',
                        "text": 'Lumière tamisée et huiles chaudes pour couper le bruit de la ville.',
                        "img": 'scene-1.png',
                        "alt": 'Cabine de massage',
                    },
                    {
                        "title": 'Protocoles visage',
                        "text": 'LED, Kobido et acide hyaluronique maîtrisés.',
                        "img": 'scene-2.png',
                        "alt": 'Soin du visage en institut',
                    },
                    {
                        "title": 'Espace détente',
                        "text": 'Hammam doux et transats chauffants.',
                        "img": 'scene-3.png',
                        "alt": 'Espace détente au spa',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": "Rituel miroir d'eau",
                        "alt": 'Vapeur et gommage au sel de Lorraine',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Atelier maquillage',
                        "alt": 'Cours privés avant un événement',
                    },
                ],
                "cards": {
                    "title": 'Nos univers',
                    "items": [
                        {
                            "title": 'Soins visage',
                            "text": 'Anti-âge, éclat, imperfections.',
                            "img": 'card-1.png',
                            "alt": 'Soin visage',
                        },
                        {
                            "title": 'Massages',
                            "text": 'Suédois, deep tissue, pierres chaudes.',
                            "img": 'card-2.png',
                            "alt": 'Massage pierres chaudes',
                        },
                        {
                            "title": 'Rituels corps',
                            "text": 'Gommage mirabelle et modelage.',
                            "img": 'card-3.png',
                            "alt": 'Rituel corps spa',
                        },
                    ],
                },
                "cta": {
                    "text": 'Offre découverte visage à 59 €.',
                    "btn": 'Réserver mon soin',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'soins.html',
                "title": 'Nos soins — Spa Thalie',
                "description": 'Protocoles visage, massages et rituels corps.',
                "hero": {
                    "h1": 'Des protocoles pensés pour votre peau',
                    "lead": 'Express le midi, rituels complets le week-end.',
                    "img": 'hero.png',
                    "alt": 'Produits de soin en cabine',
                },
                "story": ('Transparence', ['Esthéticiennes diplômées, produits français sans parabènes.']),
                "cards": {
                    "title": 'Catalogue',
                    "items": [
                        {
                            "title": 'Éclat express',
                            "text": '45 min pour un coup de frais.',
                            "img": 'card-1.png',
                            "alt": 'Soin express',
                        },
                        {
                            "title": 'Rituel Stanislas',
                            "text": '90 min gommage et massage.',
                            "img": 'card-2.png',
                            "alt": 'Rituel spa complet',
                        },
                        {
                            "title": 'Cure anti-âge',
                            "text": '4 séances radiofréquence.',
                            "img": 'card-3.png',
                            "alt": 'Soin anti-âge',
                        },
                    ],
                },
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Massage deep tissue',
                        "alt": 'Épaules des cadres nancéiens',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Soin des mains',
                        "alt": 'Manucure spa',
                    },
                ],
                "cta": {
                    "text": 'Carte cadeau valable un an.',
                    "btn": 'Offrir un soin',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'ambiance.html',
                "title": "L'institut — Spa Thalie",
                "description": 'Lieux, cabines et engagements RSE.',
                "hero": {
                    "h1": 'Un écrin de calme rue Stanislas',
                    "lead": 'Pierre de taille et technologies dernière génération.',
                    "img": 'hero.png',
                    "alt": "Hall d'accueil spa nancéien",
                },
                "story": ('Engagements', ['Eau filtrée, linge local, partenariat ESAT de Laxou.']),
                "chapters": [
                    {
                        "title": 'Accueil',
                        "text": "Thé dès l'arrivée et écoute attentive.",
                        "img": 'scene-1.png',
                        "alt": 'Accueil spa',
                    },
                    {
                        "title": 'Cabines doubles',
                        "text": 'Massages synchronisés à deux.',
                        "img": 'scene-2.png',
                        "alt": 'Cabine duo',
                    },
                    {
                        "title": 'Salon de repos',
                        "text": 'Tisanes bio après chaque soin.',
                        "img": 'scene-3.png',
                        "alt": 'Salon de repos',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Façade Stanislas',
                        "alt": 'À deux pas de la place',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Détail pierre',
                        "alt": 'Cachet de la vieille ville',
                    },
                ],
                "cta": {
                    "text": 'Visite sur RDV mercredi après-midi.',
                    "btn": 'Planifier une visite',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'contact.html',
                "title": 'Contact — Spa Thalie',
                "description": 'RDV et accès à Nancy.',
                "hero": {
                    "h1": 'Réserver votre moment Thalie',
                    "lead": '8 rue des Mésanges, 54000 Nancy.',
                    "img": 'hero.png',
                    "alt": 'Réception du spa',
                },
                "story": ('Horaires', ['Lun fermé. Mar–sam 9h–20h. Dim 10h–18h sur RDV.']),
                "cta": {
                    "text": 'Annulation gratuite 24 h avant.',
                    "btn": 'Confirmer mon RDV',
                    "href": '#',
                },
            },
        ],
    },
    {
        "slug": 'odontologie',
        "brand": 'Centre dentaire Mosaïque',
        "category": 'sante',
        "layout": 'medical',
        "nav_cta": 'Prendre RDV',
        "synopsis": 'Cabinet dentaire moderne à Thionville, accueil rassurant et prévention pour toute la famille.',
        "nav": [
            {
                "file": 'index.html',
                "label": 'Accueil',
            },
            {
                "file": 'soins.html',
                "label": 'Nos soins',
            },
            {
                "file": 'equipe.html',
                "label": "L'équipe",
            },
            {
                "file": 'contact.html',
                "label": 'Contact',
            },
        ],
        "pages": [
            {
                "file": 'index.html',
                "title": 'Centre dentaire Mosaïque — Thionville',
                "description": 'Cabinet dentaire à Thionville : soins, prévention et orthodontie pour enfants et adultes.',
                "hero": {
                    "h1": 'Votre sourire, notre priorité à Thionville',
                    "lead": 'Quatre praticiens, plateau technique numérique et parcours patient sans stress.',
                    "img": 'hero.png',
                    "alt": "Salle d'attente lumineuse de cabinet dentaire",
                },
                "story": ('Une approche humaine', ['Ouvert en 2018 avenue de la République, Mosaïque accueille familles et seniors avec des créneaux le samedi matin.', 'Chaque patient reçoit un devis détaillé avant tout acte.']),
                "chapters": [
                    {
                        "title": 'Imagerie 3D',
                        "text": 'Panoramique et scanner intra-oral pour un diagnostic précis.',
                        "img": 'scene-1.png',
                        "alt": 'Équipement dentaire numérique',
                    },
                    {
                        "title": 'Salles de soins',
                        "text": 'Fauteuils ergonomiques et musique au casque.',
                        "img": 'scene-2.png',
                        "alt": 'Salle de soins dentaire moderne',
                    },
                    {
                        "title": 'Espace enfants',
                        "text": 'Coin ludique et protocole douceur pour les plus jeunes.',
                        "img": 'scene-3.png',
                        "alt": 'Espace enfants au cabinet',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Blanchiment',
                        "alt": 'Résultat naturel en une séance',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Urgences',
                        "alt": 'Créneaux réservés chaque jour',
                    },
                ],
                "cards": {
                    "title": 'Nos expertises',
                    "items": [
                        {
                            "title": 'Prévention',
                            "text": 'Détartrage, scellements et bilans annuels.',
                            "img": 'card-1.png',
                            "alt": 'Contrôle dentaire',
                        },
                        {
                            "title": 'Esthétique',
                            "text": 'Facettes et blanchiment professionnel.',
                            "img": 'card-2.png',
                            "alt": 'Sourire blanchi',
                        },
                        {
                            "title": 'Implants',
                            "text": 'Pose guidée par ordinateur.',
                            "img": 'card-3.png',
                            "alt": 'Implant dentaire',
                        },
                    ],
                },
                "cta": {
                    "text": 'Premier rendez-vous découverte offert.',
                    "btn": 'Demander un RDV',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'soins.html',
                "title": 'Nos soins — Centre Mosaïque',
                "description": 'Soins conservateurs, prothèses et orthodontie.',
                "hero": {
                    "h1": 'Des soins adaptés à chaque âge',
                    "lead": 'Tarifs affichés et tiers payant accepté.',
                    "img": 'hero.png',
                    "alt": 'Instruments dentaires stériles',
                },
                "story": ('Tarifs transparents', ["Grille affichée en salle d'attente et envoyée par e-mail avec chaque devis."]),
                "cards": {
                    "title": 'Actes courants',
                    "items": [
                        {
                            "title": 'Détartrage',
                            "text": '45 € — remboursé Sécu.',
                            "img": 'card-1.png',
                            "alt": 'Détartrage',
                        },
                        {
                            "title": 'Couronne céramique',
                            "text": 'Devis personnalisé sous 48 h.',
                            "img": 'card-2.png',
                            "alt": 'Couronne dentaire',
                        },
                        {
                            "title": 'Aligneurs',
                            "text": 'Orthodontie invisible adulte.',
                            "img": 'card-3.png',
                            "alt": 'Gouttières transparentes',
                        },
                    ],
                },
                "chapters": [
                    {
                        "title": 'Parcours implant',
                        "text": 'De la pose à la couronne en 3 rendez-vous.',
                        "img": 'scene-1.png',
                        "alt": "Pose d'implant",
                    },
                    {
                        "title": 'Soins enfants',
                        "text": 'Pédodontie bienveillante dès 3 ans.',
                        "img": 'scene-2.png',
                        "alt": 'Dentiste avec enfant',
                    },
                    {
                        "title": 'Urgences',
                        "text": 'Douleur aiguë : appelez avant 11 h.',
                        "img": 'scene-3.png',
                        "alt": 'Urgence dentaire',
                    },
                ],
                "cta": {
                    "text": 'Question sur un devis ? Demandez un rappel.',
                    "btn": 'Être rappelé',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'equipe.html',
                "title": "L'équipe — Centre Mosaïque",
                "description": 'Chirurgiens-dentistes et assistantes à Thionville.',
                "hero": {
                    "h1": 'Quatre praticiens, une même exigence',
                    "lead": 'Formation continue et congrès européens.',
                    "img": 'hero.png',
                    "alt": 'Équipe dentaire en blouse',
                },
                "story": ('Nos valeurs', ['Écoute, pédagogie et douceur : nous expliquons chaque geste avant de commencer.']),
                "chapters": [
                    {
                        "title": 'Dr Leroy',
                        "text": "15 ans d'expérience en implantologie.",
                        "img": 'scene-1.png',
                        "alt": 'Chirurgien-dentiste',
                    },
                    {
                        "title": 'Dr Ben Saïd',
                        "text": 'Spécialiste orthodontie et aligneurs.',
                        "img": 'scene-2.png',
                        "alt": 'Orthodontiste',
                    },
                    {
                        "title": 'Assistantes',
                        "text": 'Coordination des RDV et suivi post-opératoire.',
                        "img": 'scene-3.png',
                        "alt": 'Assistantes dentaires',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Formation',
                        "alt": 'Congrès à Strasbourg',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Vie de cabinet',
                        "alt": "Petit-déjeuner d'équipe mensuel",
                    },
                ],
                "cta": {
                    "text": 'Rejoignez une équipe en croissance.',
                    "btn": 'Candidater',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'contact.html',
                "title": 'Contact — Centre Mosaïque',
                "description": 'RDV et urgences dentaires à Thionville.',
                "hero": {
                    "h1": 'Prendre rendez-vous',
                    "lead": '42 avenue de la République, 57100 Thionville.',
                    "img": 'hero.png',
                    "alt": 'Accueil cabinet dentaire',
                },
                "story": ('Accès', ['Parking République. Bus ligne 5 arrêt Hôtel de Ville. Samedi 8h–12h.']),
                "cta": {
                    "text": 'Urgence : 03 82 88 45 00 avant 11 h.',
                    "btn": 'Réserver en ligne',
                    "href": '#',
                },
            },
        ],
    },
    {
        "slug": 'automobile',
        "brand": 'Garage Central Plappeville',
        "category": 'mobilite',
        "layout": 'garage',
        "nav_cta": 'Prendre RDV',
        "synopsis": 'Garage familial à Plappeville : mécanique, carrosserie et pneus pour les automobilistes messins.',
        "nav": [
            {
                "file": 'index.html',
                "label": 'Accueil',
            },
            {
                "file": 'services.html',
                "label": 'Services',
            },
            {
                "file": 'atelier.html',
                "label": "L'atelier",
            },
            {
                "file": 'contact.html',
                "label": 'Contact',
            },
        ],
        "pages": [
            {
                "file": 'index.html',
                "title": 'Garage Central Plappeville — Mécanique & carrosserie',
                "description": 'Garage auto à Plappeville : entretien, pneus, carrosserie et contrôle technique.',
                "hero": {
                    "h1": "L'atelier de confiance des Messins depuis 1972",
                    "lead": 'Mécanique générale, carrosserie et pneus — devis clair avant chaque intervention.',
                    "img": 'hero.png',
                    "alt": 'Atelier mécanique avec véhicule sur pont',
                },
                "story": ('Un garage de quartier', ['Fondé par Jean-Pierre Daniel, repris par ses fils en 2005, le Garage Central accompagne trois générations de clients entre Metz et Woippy.', 'Toutes marques, véhicules thermiques et hybrides.']),
                "chapters": [
                    {
                        "title": 'Le pont élévateur',
                        "text": 'Diagnostic rapide et transparence sur les pièces à changer.',
                        "img": 'scene-1.png',
                        "alt": 'Pont élévateur en atelier',
                    },
                    {
                        "title": 'La carrosserie',
                        "text": 'Peinture cabine et débosselage sans peinture.',
                        "img": 'scene-2.png',
                        "alt": 'Atelier carrosserie',
                    },
                    {
                        "title": 'Le parc pneus',
                        "text": 'Montage, équilibrage et géométrie — toutes dimensions.',
                        "img": 'scene-3.png',
                        "alt": 'Stock de pneus en garage',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Révision complète',
                        "alt": 'Vidange et filtres en 1 h',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Véhicule de courtoisie',
                        "alt": 'Sur demande pour les grosses réparations',
                    },
                ],
                "cards": {
                    "title": 'Nos services',
                    "items": [
                        {
                            "title": 'Entretien',
                            "text": 'Révisions constructeur respectées.',
                            "img": 'card-1.png',
                            "alt": 'Révision automobile',
                        },
                        {
                            "title": 'Pneumatiques',
                            "text": 'Été, hiver, toutes marques.',
                            "img": 'card-2.png',
                            "alt": 'Montage de pneus',
                        },
                        {
                            "title": 'Carrosserie',
                            "text": 'Devis assurance en 24 h.',
                            "img": 'card-3.png',
                            "alt": 'Réparation carrosserie',
                        },
                    ],
                },
                "cta": {
                    "text": 'Contrôle anti-pollution : créneaux sans attente.',
                    "btn": 'Réserver un créneau',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'services.html',
                "title": 'Services — Garage Central',
                "description": 'Mécanique, pneus, climatisation et diagnostic.',
                "hero": {
                    "h1": 'Tout pour rouler serein',
                    "lead": 'De la vidange à la distribution, expertise multimarque.',
                    "img": 'hero.png',
                    "alt": 'Mécanicien au travail',
                },
                "story": ('Garanties', ["Pièces d'origine ou équivalent premium. Garantie 2 ans sur les réparations majeures."]),
                "cards": {
                    "title": 'Prestations',
                    "items": [
                        {
                            "title": 'Distribution',
                            "text": 'Kit courroie et pompe à eau.',
                            "img": 'card-1.png',
                            "alt": 'Courroie de distribution',
                        },
                        {
                            "title": 'Climatisation',
                            "text": 'Recharge et désinfection.',
                            "img": 'card-2.png',
                            "alt": 'Recharge clim auto',
                        },
                        {
                            "title": 'Diagnostic',
                            "text": 'Valise multimarque et rapport détaillé.',
                            "img": 'card-3.png',
                            "alt": 'Diagnostic électronique',
                        },
                    ],
                },
                "chapters": [
                    {
                        "title": 'Freinage',
                        "text": 'Disques, plaquettes et liquide de frein.',
                        "img": 'scene-1.png',
                        "alt": 'Freins automobile',
                    },
                    {
                        "title": 'Échappement',
                        "text": 'Ligne complète et catalyseur.',
                        "img": 'scene-2.png',
                        "alt": 'Échappement',
                    },
                    {
                        "title": 'Hybride',
                        "text": 'Formation Bosch pour les véhicules rechargeables.',
                        "img": 'scene-3.png',
                        "alt": 'Véhicule hybride en atelier',
                    },
                ],
                "cta": {
                    "text": 'Devis gratuit en atelier ou par photo.',
                    "btn": 'Demander un devis',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'atelier.html',
                "title": "L'atelier — Garage Central",
                "description": 'Équipe, outils et méthode de travail.',
                "hero": {
                    "h1": '900 m² dédiés à votre véhicule',
                    "lead": 'Ponts, cabine peinture et espace diagnostic.',
                    "img": 'hero.png',
                    "alt": "Vue d'ensemble de l'atelier",
                },
                "story": ("L'équipe", ['Six mécaniciens, deux carrossiers et une coordinatrice accueil — tous formés aux normes constructeur.']),
                "chapters": [
                    {
                        "title": 'Accueil',
                        "text": "Café et wifi en salle d'attente.",
                        "img": 'scene-1.png',
                        "alt": 'Accueil garage',
                    },
                    {
                        "title": 'Outillage',
                        "text": 'Clés dynamométriques et documentation constructeur.',
                        "img": 'scene-2.png',
                        "alt": 'Outillage professionnel',
                    },
                    {
                        "title": 'Propreté',
                        "text": 'Véhicule rendu lavé intérieur/extérieur.',
                        "img": 'scene-3.png',
                        "alt": 'Lavage véhicule',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Équipe 2024',
                        "alt": "Photo de groupe devant l'atelier",
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Héritage',
                        "alt": "Enseigne d'origine conservée",
                    },
                ],
                "cta": {
                    "text": "Visite de l'atelier sur rendez-vous.",
                    "btn": 'Planifier une visite',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'contact.html',
                "title": 'Contact — Garage Central',
                "description": 'RDV atelier à Plappeville.',
                "hero": {
                    "h1": 'Nous contacter',
                    "lead": 'Zone artisanale des Gravières, 57050 Plappeville.',
                    "img": 'hero.png',
                    "alt": 'Façade du garage',
                },
                "story": ('Horaires', ['Lun–ven 8h–18h, sam 8h–12h. Tél. 03 87 65 43 21.']),
                "cta": {
                    "text": 'Panne sur autoroute ? Numéro dépannage 24h/24.',
                    "btn": 'Appeler le dépannage',
                    "href": '#',
                },
            },
        ],
    },
    {
        "slug": 'commerce',
        "brand": 'Halles Thionville',
        "category": 'retail',
        "layout": 'retail',
        "nav_cta": 'Voir le drive',
        "synopsis": 'Commerce de proximité et drive à Thionville : produits frais, click & collect et fidélité locale.',
        "nav": [
            {
                "file": 'index.html',
                "label": 'Accueil',
            },
            {
                "file": 'rayons.html',
                "label": 'Rayons',
            },
            {
                "file": 'drive.html',
                "label": 'Drive',
            },
            {
                "file": 'contact.html',
                "label": 'Contact',
            },
        ],
        "pages": [
            {
                "file": 'index.html',
                "title": 'Halles Thionville — Commerce & drive',
                "description": 'Supermarché de proximité à Thionville : frais, drive et programme fidélité.',
                "hero": {
                    "h1": 'Le marché du quotidien, version moderne',
                    "lead": '3200 m² de rayons, boucherie artisanale et drive en 2 h chrono.',
                    "img": 'hero.png',
                    "alt": 'Allée de supermarché lumineuse',
                },
                "story": ('Ancré dans le bassin thionvillois', ['Les Halles Thionville travaillent avec 40 producteurs mosellans et emploient 85 collaborateurs du quartier.', 'Ouvert 7j/7, avec des horaires élargis le dimanche matin.']),
                "chapters": [
                    {
                        "title": 'Boucherie',
                        "text": 'Viandes label rouge et préparations maison.',
                        "img": 'scene-1.png',
                        "alt": 'Boucherie artisanale',
                    },
                    {
                        "title": 'Boulangerie',
                        "text": 'Four sur place dès 7 h.',
                        "img": 'scene-2.png',
                        "alt": 'Pain frais en rayon',
                    },
                    {
                        "title": 'Fruits & légumes',
                        "text": 'Arrivages quotidiens de Serémange et Corny.',
                        "img": 'scene-3.png',
                        "alt": 'Rayon fruits et légumes',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Vitrine fromages',
                        "alt": 'AOP lorraines et affinés',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Événement dégustation',
                        "alt": 'Samedi producteurs locaux',
                    },
                ],
                "cards": {
                    "title": 'Nos atouts',
                    "items": [
                        {
                            "title": 'Click & collect',
                            "text": 'Commande en ligne, retrait en 2 h.',
                            "img": 'card-1.png',
                            "alt": 'Retrait drive',
                        },
                        {
                            "title": 'Carte fidélité',
                            "text": '1 € dépensé = 1 point, avantages exclusifs.',
                            "img": 'card-2.png',
                            "alt": 'Carte de fidélité',
                        },
                        {
                            "title": 'Livraison',
                            "text": 'Sur Thionville et Yutz en soirée.',
                            "img": 'card-3.png',
                            "alt": 'Livraison à domicile',
                        },
                    ],
                },
                "cta": {
                    "text": 'Inscrivez-vous au programme Halles+',
                    "btn": 'Créer ma carte',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'rayons.html',
                "title": 'Rayons — Halles Thionville',
                "description": 'Boucherie, poissonnerie, épicerie et bio.',
                "hero": {
                    "h1": 'Des rayons qui respirent la fraîcheur',
                    "lead": 'Produits locaux mis en avant chaque semaine.',
                    "img": 'hero.png',
                    "alt": 'Rayon épicerie fine',
                },
                "story": ('Engagement local', ['Étiquetage origine Moselle sur 200 références permanentes.']),
                "cards": {
                    "title": 'Univers',
                    "items": [
                        {
                            "title": 'Frais',
                            "text": 'Crèmerie, traiteur et sushi du jour.',
                            "img": 'card-1.png',
                            "alt": 'Rayon frais',
                        },
                        {
                            "title": 'Épicerie',
                            "text": 'Marques régionales et sans gluten.',
                            "img": 'card-2.png',
                            "alt": 'Étagères épicerie',
                        },
                        {
                            "title": 'Bio & vrac',
                            "text": 'Cosmétiques et céréales en vrac.',
                            "img": 'card-3.png',
                            "alt": 'Rayon vrac bio',
                        },
                    ],
                },
                "chapters": [
                    {
                        "title": 'Poissonnerie',
                        "text": 'Arrivages mer du Nord 3 fois par semaine.',
                        "img": 'scene-1.png',
                        "alt": 'Poissonnerie',
                    },
                    {
                        "title": 'Cave',
                        "text": 'Vins mosellans et conseils sommelier.',
                        "img": 'scene-2.png',
                        "alt": 'Cave à vins',
                    },
                    {
                        "title": 'Surgelés',
                        "text": 'Gamme premium et surgelés maison.',
                        "img": 'scene-3.png',
                        "alt": 'Surgelés',
                    },
                ],
                "cta": {
                    "text": 'Catalogue promo hebdomadaire en ligne.',
                    "btn": 'Voir les promos',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'drive.html',
                "title": 'Drive — Halles Thionville',
                "description": 'Click & collect et retrait express.',
                "hero": {
                    "h1": 'Faites vos courses sans sortir de voiture',
                    "lead": '15 emplacements couverts, prêt en 2 h.',
                    "img": 'hero.png',
                    "alt": 'Point drive couvert',
                },
                "story": ('Comment ça marche', ['Commandez sur halles-thionville.fr, choisissez votre créneau, nous préparons et chargeons votre coffre.']),
                "chapters": [
                    {
                        "title": 'Préparation',
                        "text": 'Préparateurs formés à la fraîcheur.',
                        "img": 'scene-1.png',
                        "alt": 'Préparation de commande',
                    },
                    {
                        "title": 'Créneaux',
                        "text": "Dès 8 h le matin, jusqu'à 20 h.",
                        "img": 'scene-2.png',
                        "alt": 'Créneaux horaires drive',
                    },
                    {
                        "title": 'Paiement',
                        "text": 'En ligne ou à la borne sur place.',
                        "img": 'scene-3.png',
                        "alt": 'Borne de paiement drive',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Emplacements',
                        "alt": 'Abris couverts été comme hiver',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Application',
                        "alt": 'Suivi commande en temps réel',
                    },
                ],
                "cta": {
                    "text": 'Première commande : frais de préparation offerts.',
                    "btn": 'Commander',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'contact.html',
                "title": 'Contact — Halles Thionville',
                "description": 'Horaires, accès et service client.',
                "hero": {
                    "h1": 'Une question ? On vous répond',
                    "lead": 'Rue du Mail, 57100 Thionville.',
                    "img": 'hero.png',
                    "alt": 'Accueil client supermarché',
                },
                "story": ('Service client', ['Lun–sam 8h–20h, dim 9h–12h30. service@halles-thionville.fr']),
                "cta": {
                    "text": 'Réclamation ou suggestion : formulaire dédié.',
                    "btn": 'Nous écrire',
                    "href": '#',
                },
            },
        ],
    },
    {
        "slug": 'comptable',
        "brand": 'Verlaine & Associés',
        "category": 'conseil',
        "layout": 'cabinet',
        "nav_cta": 'Prendre RDV',
        "synopsis": "Cabinet d'expertise comptable à Metz, partenaire des PME lorraines depuis 1986.",
        "nav": [
            {
                "file": 'index.html',
                "label": 'Accueil',
            },
            {
                "file": 'expertises.html',
                "label": 'Expertises',
            },
            {
                "file": 'methode.html',
                "label": 'Notre méthode',
            },
            {
                "file": 'contact.html',
                "label": 'Contact',
            },
        ],
        "pages": [
            {
                "file": 'index.html',
                "title": 'Verlaine & Associés — Accueil',
                "description": "Cabinet d'expertise comptable à Metz, partenaire des PME lorraines depuis 1986.…",
                "hero": {
                    "h1": 'Verlaine & Associés : bilan et conseil à Metz',
                    "lead": 'Accompagnement de dirigeants en Lorraine avec exigence et proximité.',
                    "img": 'hero.png',
                    "alt": "Vue d'ensemble Verlaine & Associés à Metz",
                },
                "story": ('Pourquoi Verlaine & Associés ?', ["Implanté à Metz, Verlaine & Associés connaît les réalités du terrain mosellan et les attentes d'une clientèle exigeante.", 'Notre équipe locale combine expertise métier et relation de confiance sur le long terme.']),
                "chapters": [
                    {
                        "title": 'Notre approche',
                        "text": 'Méthode éprouvée et transparence à chaque étape pour dirigeants.',
                        "img": 'scene-1.png',
                        "alt": 'Expertises chez Verlaine & Associés',
                    },
                    {
                        "title": 'Le quotidien',
                        "text": 'Scènes de travail authentiques dans nos locaux de Metz.',
                        "img": 'scene-2.png',
                        "alt": 'Équipe au travail à Metz',
                    },
                    {
                        "title": 'Nos engagements',
                        "text": 'Qualité, réactivité et ancrage Grand Est depuis des années.',
                        "img": 'scene-3.png',
                        "alt": 'Engagement Verlaine & Associés',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Moment de vie — Metz',
                        "alt": 'Scène Verlaine & Associés',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Rencontre avec nos clients',
                        "alt": 'Clientèle dirigeants',
                    },
                ],
                "cards": {
                    "title": 'Ce que nous proposons',
                    "items": [
                        {
                            "title": 'Offre essentielle',
                            "text": "Pack d'entrée adapté aux besoins courants de dirigeants.",
                            "img": 'card-1.png',
                            "alt": 'Offre Verlaine & Associés',
                        },
                        {
                            "title": 'Offre premium',
                            "text": 'Accompagnement renforcé et suivi personnalisé.',
                            "img": 'card-2.png',
                            "alt": 'Service premium Verlaine & Associés',
                        },
                        {
                            "title": 'Sur mesure',
                            "text": 'Projet spécifique ? Nous construisons la réponse ensemble.',
                            "img": 'card-3.png',
                            "alt": 'Projet sur mesure',
                        },
                    ],
                },
                "cta": {
                    "text": 'Parlons de votre projet à Metz.',
                    "btn": 'Prendre RDV',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'expertises.html',
                "title": 'Expertises — Verlaine & Associés',
                "description": 'Expertises : détails et expertises de Verlaine & Associés à Metz.',
                "hero": {
                    "h1": 'Expertises',
                    "lead": 'Découvrez notre offre expertises pour dirigeants.',
                    "img": 'hero.png',
                    "alt": 'Page Expertises Verlaine & Associés',
                },
                "story": ('Notre vision — Expertises', ['Chaque prestation est calibrée pour les réalités du marché lorrain et les objectifs de dirigeants.']),
                "cards": {
                    "title": 'Expertises',
                    "items": [
                        {
                            "title": 'Expertises — niveau 1',
                            "text": 'Formule accessible et complète.',
                            "img": 'card-1.png',
                            "alt": 'Détail Expertises',
                        },
                        {
                            "title": 'Expertises — niveau 2',
                            "text": 'Approfondissement et options avancées.',
                            "img": 'card-2.png',
                            "alt": 'Option avancée',
                        },
                        {
                            "title": 'Expertises — niveau 3',
                            "text": 'Solution intégrale clé en main.',
                            "img": 'card-3.png',
                            "alt": 'Solution intégrale',
                        },
                    ],
                },
                "chapters": [
                    {
                        "title": 'Coulisses Expertises',
                        "text": "L'équipe Verlaine & Associés en action sur le terrain.",
                        "img": 'scene-1.png',
                        "alt": 'Coulisses Verlaine & Associés',
                    },
                    {
                        "title": 'Résultats',
                        "text": 'Témoignages et cas concrets à Metz.',
                        "img": 'scene-2.png',
                        "alt": 'Résultats clients',
                    },
                    {
                        "title": 'Méthode',
                        "text": 'Processus structuré en trois temps.',
                        "img": 'scene-3.png',
                        "alt": 'Méthode Verlaine & Associés',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Focus Expertises',
                        "alt": 'Image Expertises',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Détail métier',
                        "alt": 'Détail Verlaine & Associés',
                    },
                ],
                "cta": {
                    "text": 'Une question sur cette offre ?',
                    "btn": 'Nous contacter',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'methode.html',
                "title": 'Notre méthode — Verlaine & Associés',
                "description": 'Notre méthode : approche et valeurs de Verlaine & Associés.',
                "hero": {
                    "h1": 'Notre méthode',
                    "lead": 'Comprendre notre démarche notre méthode.',
                    "img": 'hero.png',
                    "alt": 'Page Notre méthode Verlaine & Associés',
                },
                "timeline": [('2010', 'Création de Verlaine & Associés à Metz.'), ('2016', "Extension de l'équipe et nouveaux locaux."), ('2020', 'Certification qualité et partenariats régionaux.'), ('2024', 'Plus de 500 clients accompagnés en Grand Est.')],
                "chapters": [
                    {
                        "title": 'Étape 1 — Écoute',
                        "text": 'Diagnostic gratuit et définition des objectifs.',
                        "img": 'scene-1.png',
                        "alt": 'Écoute client Verlaine & Associés',
                    },
                    {
                        "title": 'Étape 2 — Action',
                        "text": "Mise en œuvre avec points d'étape réguliers.",
                        "img": 'scene-2.png',
                        "alt": 'Action terrain',
                    },
                    {
                        "title": 'Étape 3 — Suivi',
                        "text": 'Bilan et ajustements pour pérenniser les résultats.',
                        "img": 'scene-3.png',
                        "alt": 'Suivi Verlaine & Associés',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Équipe Verlaine & Associés',
                        "alt": "Photo d'équipe",
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Locaux Metz',
                        "alt": 'Bureaux à Metz',
                    },
                ],
                "cta": {
                    "text": 'Rencontrons-nous à Metz.',
                    "btn": 'Prendre RDV',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'contact.html',
                "title": 'Contact — Verlaine & Associés',
                "description": 'Contactez Verlaine & Associés à Metz.',
                "hero": {
                    "h1": 'Parlons de votre projet',
                    "lead": 'Metz, Grand Est — réponse sous 24 h ouvrées.',
                    "img": 'hero.png',
                    "alt": 'Contact Verlaine & Associés',
                },
                "story": ('Coordonnées', ['Du lundi au vendredi 9h–18h. Formulaire ci-dessous ou par téléphone.']),
                "cta": {
                    "text": 'Démonstration — aucune donnée transmise.',
                    "btn": 'Envoyer ma demande',
                    "href": '#',
                },
            },
        ],
    },
    {
        "slug": 'industrie',
        "brand": 'Précisite Usinage',
        "category": 'industrie',
        "layout": 'industrial',
        "nav_cta": 'Demander un devis',
        "synopsis": "Usinage de précision à Yutz pour l'automobile et l'aéronautique en Lorraine.",
        "nav": [
            {
                "file": 'index.html',
                "label": 'Accueil',
            },
            {
                "file": 'savoir-faire.html',
                "label": 'Savoir-faire',
            },
            {
                "file": 'qualite.html',
                "label": 'Qualité',
            },
            {
                "file": 'contact.html',
                "label": 'Contact',
            },
        ],
        "pages": [
            {
                "file": 'index.html',
                "title": 'Précisite Usinage — Accueil',
                "description": "Usinage de précision à Yutz pour l'automobile et l'aéronautique en Lorraine.…",
                "hero": {
                    "h1": 'Précisite Usinage : tolerances micron à Yutz',
                    "lead": "Accompagnement de donneurs d'ordre en Lorraine avec exigence et proximité.",
                    "img": 'hero.png',
                    "alt": "Vue d'ensemble Précisite Usinage à Yutz",
                },
                "story": ('Pourquoi Précisite Usinage ?', ["Implanté à Yutz, Précisite Usinage connaît les réalités du terrain mosellan et les attentes d'une clientèle exigeante.", 'Notre équipe locale combine expertise métier et relation de confiance sur le long terme.']),
                "chapters": [
                    {
                        "title": 'Notre approche',
                        "text": "Méthode éprouvée et transparence à chaque étape pour donneurs d'ordre.",
                        "img": 'scene-1.png',
                        "alt": 'Savoir-faire chez Précisite Usinage',
                    },
                    {
                        "title": 'Le quotidien',
                        "text": 'Scènes de travail authentiques dans nos locaux de Yutz.',
                        "img": 'scene-2.png',
                        "alt": 'Équipe au travail à Yutz',
                    },
                    {
                        "title": 'Nos engagements',
                        "text": 'Qualité, réactivité et ancrage Grand Est depuis des années.',
                        "img": 'scene-3.png',
                        "alt": 'Engagement Précisite Usinage',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Moment de vie — Yutz',
                        "alt": 'Scène Précisite Usinage',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Rencontre avec nos clients',
                        "alt": "Clientèle donneurs d'ordre",
                    },
                ],
                "cards": {
                    "title": 'Ce que nous proposons',
                    "items": [
                        {
                            "title": 'Offre essentielle',
                            "text": "Pack d'entrée adapté aux besoins courants de donneurs d'ordre.",
                            "img": 'card-1.png',
                            "alt": 'Offre Précisite Usinage',
                        },
                        {
                            "title": 'Offre premium',
                            "text": 'Accompagnement renforcé et suivi personnalisé.',
                            "img": 'card-2.png',
                            "alt": 'Service premium Précisite Usinage',
                        },
                        {
                            "title": 'Sur mesure',
                            "text": 'Projet spécifique ? Nous construisons la réponse ensemble.',
                            "img": 'card-3.png',
                            "alt": 'Projet sur mesure',
                        },
                    ],
                },
                "cta": {
                    "text": 'Parlons de votre projet à Yutz.',
                    "btn": 'Demander un devis',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'savoir-faire.html',
                "title": 'Savoir-faire — Précisite Usinage',
                "description": 'Savoir-faire : détails et expertises de Précisite Usinage à Yutz.',
                "hero": {
                    "h1": 'Savoir-faire',
                    "lead": "Découvrez notre offre savoir-faire pour donneurs d'ordre.",
                    "img": 'hero.png',
                    "alt": 'Page Savoir-faire Précisite Usinage',
                },
                "story": ('Notre vision — Savoir-faire', ["Chaque prestation est calibrée pour les réalités du marché lorrain et les objectifs de donneurs d'ordre."]),
                "cards": {
                    "title": 'Savoir-faire',
                    "items": [
                        {
                            "title": 'Savoir-faire — niveau 1',
                            "text": 'Formule accessible et complète.',
                            "img": 'card-1.png',
                            "alt": 'Détail Savoir-faire',
                        },
                        {
                            "title": 'Savoir-faire — niveau 2',
                            "text": 'Approfondissement et options avancées.',
                            "img": 'card-2.png',
                            "alt": 'Option avancée',
                        },
                        {
                            "title": 'Savoir-faire — niveau 3',
                            "text": 'Solution intégrale clé en main.',
                            "img": 'card-3.png',
                            "alt": 'Solution intégrale',
                        },
                    ],
                },
                "chapters": [
                    {
                        "title": 'Coulisses Savoir-faire',
                        "text": "L'équipe Précisite Usinage en action sur le terrain.",
                        "img": 'scene-1.png',
                        "alt": 'Coulisses Précisite Usinage',
                    },
                    {
                        "title": 'Résultats',
                        "text": 'Témoignages et cas concrets à Yutz.',
                        "img": 'scene-2.png',
                        "alt": 'Résultats clients',
                    },
                    {
                        "title": 'Méthode',
                        "text": 'Processus structuré en trois temps.',
                        "img": 'scene-3.png',
                        "alt": 'Méthode Précisite Usinage',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Focus Savoir-faire',
                        "alt": 'Image Savoir-faire',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Détail métier',
                        "alt": 'Détail Précisite Usinage',
                    },
                ],
                "cta": {
                    "text": 'Une question sur cette offre ?',
                    "btn": 'Nous contacter',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'qualite.html',
                "title": 'Qualité — Précisite Usinage',
                "description": 'Qualité : approche et valeurs de Précisite Usinage.',
                "hero": {
                    "h1": 'Qualité',
                    "lead": 'Comprendre notre démarche qualité.',
                    "img": 'hero.png',
                    "alt": 'Page Qualité Précisite Usinage',
                },
                "timeline": [('2010', 'Création de Précisite Usinage à Yutz.'), ('2016', "Extension de l'équipe et nouveaux locaux."), ('2020', 'Certification qualité et partenariats régionaux.'), ('2024', 'Plus de 500 clients accompagnés en Grand Est.')],
                "chapters": [
                    {
                        "title": 'Étape 1 — Écoute',
                        "text": 'Diagnostic gratuit et définition des objectifs.',
                        "img": 'scene-1.png',
                        "alt": 'Écoute client Précisite Usinage',
                    },
                    {
                        "title": 'Étape 2 — Action',
                        "text": "Mise en œuvre avec points d'étape réguliers.",
                        "img": 'scene-2.png',
                        "alt": 'Action terrain',
                    },
                    {
                        "title": 'Étape 3 — Suivi',
                        "text": 'Bilan et ajustements pour pérenniser les résultats.',
                        "img": 'scene-3.png',
                        "alt": 'Suivi Précisite Usinage',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Équipe Précisite Usinage',
                        "alt": "Photo d'équipe",
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Locaux Yutz',
                        "alt": 'Bureaux à Yutz',
                    },
                ],
                "cta": {
                    "text": 'Rencontrons-nous à Yutz.',
                    "btn": 'Demander un devis',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'contact.html',
                "title": 'Contact — Précisite Usinage',
                "description": 'Contactez Précisite Usinage à Yutz.',
                "hero": {
                    "h1": 'Parlons de votre projet',
                    "lead": 'Yutz, Grand Est — réponse sous 24 h ouvrées.',
                    "img": 'hero.png',
                    "alt": 'Contact Précisite Usinage',
                },
                "story": ('Coordonnées', ['Du lundi au vendredi 9h–18h. Formulaire ci-dessous ou par téléphone.']),
                "cta": {
                    "text": 'Démonstration — aucune donnée transmise.',
                    "btn": 'Envoyer ma demande',
                    "href": '#',
                },
            },
        ],
    },
    {
        "slug": 'immobilier',
        "brand": 'Patrimoine Lorraine',
        "category": 'immobilier',
        "layout": 'property',
        "nav_cta": 'Estimer mon bien',
        "synopsis": 'Agence immobilière à Nancy : vente, location et gestion sur le Grand Est.',
        "nav": [
            {
                "file": 'index.html',
                "label": 'Accueil',
            },
            {
                "file": 'biens.html',
                "label": 'Nos biens',
            },
            {
                "file": 'estimation.html',
                "label": 'Estimation',
            },
            {
                "file": 'contact.html',
                "label": 'Contact',
            },
        ],
        "pages": [
            {
                "file": 'index.html',
                "title": 'Patrimoine Lorraine — Accueil',
                "description": 'Agence immobilière à Nancy : vente, location et gestion sur le Grand Est.…',
                "hero": {
                    "h1": "Patrimoine Lorraine : biens d'exception à Nancy",
                    "lead": 'Accompagnement de acquéreurs en Lorraine avec exigence et proximité.',
                    "img": 'hero.png',
                    "alt": "Vue d'ensemble Patrimoine Lorraine à Nancy",
                },
                "story": ('Pourquoi Patrimoine Lorraine ?', ["Implanté à Nancy, Patrimoine Lorraine connaît les réalités du terrain mosellan et les attentes d'une clientèle exigeante.", 'Notre équipe locale combine expertise métier et relation de confiance sur le long terme.']),
                "chapters": [
                    {
                        "title": 'Notre approche',
                        "text": 'Méthode éprouvée et transparence à chaque étape pour acquéreurs.',
                        "img": 'scene-1.png',
                        "alt": 'Nos biens chez Patrimoine Lorraine',
                    },
                    {
                        "title": 'Le quotidien',
                        "text": 'Scènes de travail authentiques dans nos locaux de Nancy.',
                        "img": 'scene-2.png',
                        "alt": 'Équipe au travail à Nancy',
                    },
                    {
                        "title": 'Nos engagements',
                        "text": 'Qualité, réactivité et ancrage Grand Est depuis des années.',
                        "img": 'scene-3.png',
                        "alt": 'Engagement Patrimoine Lorraine',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Moment de vie — Nancy',
                        "alt": 'Scène Patrimoine Lorraine',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Rencontre avec nos clients',
                        "alt": 'Clientèle acquéreurs',
                    },
                ],
                "cards": {
                    "title": 'Ce que nous proposons',
                    "items": [
                        {
                            "title": 'Offre essentielle',
                            "text": "Pack d'entrée adapté aux besoins courants de acquéreurs.",
                            "img": 'card-1.png',
                            "alt": 'Offre Patrimoine Lorraine',
                        },
                        {
                            "title": 'Offre premium',
                            "text": 'Accompagnement renforcé et suivi personnalisé.',
                            "img": 'card-2.png',
                            "alt": 'Service premium Patrimoine Lorraine',
                        },
                        {
                            "title": 'Sur mesure',
                            "text": 'Projet spécifique ? Nous construisons la réponse ensemble.',
                            "img": 'card-3.png',
                            "alt": 'Projet sur mesure',
                        },
                    ],
                },
                "cta": {
                    "text": 'Parlons de votre projet à Nancy.',
                    "btn": 'Estimer mon bien',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'biens.html',
                "title": 'Nos biens — Patrimoine Lorraine',
                "description": 'Nos biens : détails et expertises de Patrimoine Lorraine à Nancy.',
                "hero": {
                    "h1": 'Nos biens',
                    "lead": 'Découvrez notre offre nos biens pour acquéreurs.',
                    "img": 'hero.png',
                    "alt": 'Page Nos biens Patrimoine Lorraine',
                },
                "story": ('Notre vision — Nos biens', ['Chaque prestation est calibrée pour les réalités du marché lorrain et les objectifs de acquéreurs.']),
                "cards": {
                    "title": 'Nos biens',
                    "items": [
                        {
                            "title": 'Nos biens — niveau 1',
                            "text": 'Formule accessible et complète.',
                            "img": 'card-1.png',
                            "alt": 'Détail Nos biens',
                        },
                        {
                            "title": 'Nos biens — niveau 2',
                            "text": 'Approfondissement et options avancées.',
                            "img": 'card-2.png',
                            "alt": 'Option avancée',
                        },
                        {
                            "title": 'Nos biens — niveau 3',
                            "text": 'Solution intégrale clé en main.',
                            "img": 'card-3.png',
                            "alt": 'Solution intégrale',
                        },
                    ],
                },
                "chapters": [
                    {
                        "title": 'Coulisses Nos biens',
                        "text": "L'équipe Patrimoine Lorraine en action sur le terrain.",
                        "img": 'scene-1.png',
                        "alt": 'Coulisses Patrimoine Lorraine',
                    },
                    {
                        "title": 'Résultats',
                        "text": 'Témoignages et cas concrets à Nancy.',
                        "img": 'scene-2.png',
                        "alt": 'Résultats clients',
                    },
                    {
                        "title": 'Méthode',
                        "text": 'Processus structuré en trois temps.',
                        "img": 'scene-3.png',
                        "alt": 'Méthode Patrimoine Lorraine',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Focus Nos biens',
                        "alt": 'Image Nos biens',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Détail métier',
                        "alt": 'Détail Patrimoine Lorraine',
                    },
                ],
                "cta": {
                    "text": 'Une question sur cette offre ?',
                    "btn": 'Nous contacter',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'estimation.html',
                "title": 'Estimation — Patrimoine Lorraine',
                "description": 'Estimation : approche et valeurs de Patrimoine Lorraine.',
                "hero": {
                    "h1": 'Estimation',
                    "lead": 'Comprendre notre démarche estimation.',
                    "img": 'hero.png',
                    "alt": 'Page Estimation Patrimoine Lorraine',
                },
                "timeline": [('2010', 'Création de Patrimoine Lorraine à Nancy.'), ('2016', "Extension de l'équipe et nouveaux locaux."), ('2020', 'Certification qualité et partenariats régionaux.'), ('2024', 'Plus de 500 clients accompagnés en Grand Est.')],
                "chapters": [
                    {
                        "title": 'Étape 1 — Écoute',
                        "text": 'Diagnostic gratuit et définition des objectifs.',
                        "img": 'scene-1.png',
                        "alt": 'Écoute client Patrimoine Lorraine',
                    },
                    {
                        "title": 'Étape 2 — Action',
                        "text": "Mise en œuvre avec points d'étape réguliers.",
                        "img": 'scene-2.png',
                        "alt": 'Action terrain',
                    },
                    {
                        "title": 'Étape 3 — Suivi',
                        "text": 'Bilan et ajustements pour pérenniser les résultats.',
                        "img": 'scene-3.png',
                        "alt": 'Suivi Patrimoine Lorraine',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Équipe Patrimoine Lorraine',
                        "alt": "Photo d'équipe",
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Locaux Nancy',
                        "alt": 'Bureaux à Nancy',
                    },
                ],
                "cta": {
                    "text": 'Rencontrons-nous à Nancy.',
                    "btn": 'Estimer mon bien',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'contact.html',
                "title": 'Contact — Patrimoine Lorraine',
                "description": 'Contactez Patrimoine Lorraine à Nancy.',
                "hero": {
                    "h1": 'Parlons de votre projet',
                    "lead": 'Nancy, Grand Est — réponse sous 24 h ouvrées.',
                    "img": 'hero.png',
                    "alt": 'Contact Patrimoine Lorraine',
                },
                "story": ('Coordonnées', ['Du lundi au vendredi 9h–18h. Formulaire ci-dessous ou par téléphone.']),
                "cta": {
                    "text": 'Démonstration — aucune donnée transmise.',
                    "btn": 'Envoyer ma demande',
                    "href": '#',
                },
            },
        ],
    },
    {
        "slug": 'juridique',
        "brand": 'Rivière & Partenaires',
        "category": 'juridique',
        "layout": 'legal',
        "nav_cta": 'Consultation',
        "synopsis": "Cabinet d'avocats à Metz : droit des affaires, social et contentieux pour PME.",
        "nav": [
            {
                "file": 'index.html',
                "label": 'Accueil',
            },
            {
                "file": 'expertises.html',
                "label": 'Expertises',
            },
            {
                "file": 'accompagnement.html',
                "label": 'Accompagnement',
            },
            {
                "file": 'contact.html',
                "label": 'Contact',
            },
        ],
        "pages": [
            {
                "file": 'index.html',
                "title": 'Rivière & Partenaires — Accueil',
                "description": "Cabinet d'avocats à Metz : droit des affaires, social et contentieux pour PME.…",
                "hero": {
                    "h1": 'Rivière & Partenaires : conseil stratégique à Metz',
                    "lead": 'Accompagnement de dirigeants en Lorraine avec exigence et proximité.',
                    "img": 'hero.png',
                    "alt": "Vue d'ensemble Rivière & Partenaires à Metz",
                },
                "story": ('Pourquoi Rivière & Partenaires ?', ["Implanté à Metz, Rivière & Partenaires connaît les réalités du terrain mosellan et les attentes d'une clientèle exigeante.", 'Notre équipe locale combine expertise métier et relation de confiance sur le long terme.']),
                "chapters": [
                    {
                        "title": 'Notre approche',
                        "text": 'Méthode éprouvée et transparence à chaque étape pour dirigeants.',
                        "img": 'scene-1.png',
                        "alt": 'Expertises chez Rivière & Partenaires',
                    },
                    {
                        "title": 'Le quotidien',
                        "text": 'Scènes de travail authentiques dans nos locaux de Metz.',
                        "img": 'scene-2.png',
                        "alt": 'Équipe au travail à Metz',
                    },
                    {
                        "title": 'Nos engagements',
                        "text": 'Qualité, réactivité et ancrage Grand Est depuis des années.',
                        "img": 'scene-3.png',
                        "alt": 'Engagement Rivière & Partenaires',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Moment de vie — Metz',
                        "alt": 'Scène Rivière & Partenaires',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Rencontre avec nos clients',
                        "alt": 'Clientèle dirigeants',
                    },
                ],
                "cards": {
                    "title": 'Ce que nous proposons',
                    "items": [
                        {
                            "title": 'Offre essentielle',
                            "text": "Pack d'entrée adapté aux besoins courants de dirigeants.",
                            "img": 'card-1.png',
                            "alt": 'Offre Rivière & Partenaires',
                        },
                        {
                            "title": 'Offre premium',
                            "text": 'Accompagnement renforcé et suivi personnalisé.',
                            "img": 'card-2.png',
                            "alt": 'Service premium Rivière & Partenaires',
                        },
                        {
                            "title": 'Sur mesure',
                            "text": 'Projet spécifique ? Nous construisons la réponse ensemble.',
                            "img": 'card-3.png',
                            "alt": 'Projet sur mesure',
                        },
                    ],
                },
                "cta": {
                    "text": 'Parlons de votre projet à Metz.',
                    "btn": 'Consultation',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'expertises.html',
                "title": 'Expertises — Rivière & Partenaires',
                "description": 'Expertises : détails et expertises de Rivière & Partenaires à Metz.',
                "hero": {
                    "h1": 'Expertises',
                    "lead": 'Découvrez notre offre expertises pour dirigeants.',
                    "img": 'hero.png',
                    "alt": 'Page Expertises Rivière & Partenaires',
                },
                "story": ('Notre vision — Expertises', ['Chaque prestation est calibrée pour les réalités du marché lorrain et les objectifs de dirigeants.']),
                "cards": {
                    "title": 'Expertises',
                    "items": [
                        {
                            "title": 'Expertises — niveau 1',
                            "text": 'Formule accessible et complète.',
                            "img": 'card-1.png',
                            "alt": 'Détail Expertises',
                        },
                        {
                            "title": 'Expertises — niveau 2',
                            "text": 'Approfondissement et options avancées.',
                            "img": 'card-2.png',
                            "alt": 'Option avancée',
                        },
                        {
                            "title": 'Expertises — niveau 3',
                            "text": 'Solution intégrale clé en main.',
                            "img": 'card-3.png',
                            "alt": 'Solution intégrale',
                        },
                    ],
                },
                "chapters": [
                    {
                        "title": 'Coulisses Expertises',
                        "text": "L'équipe Rivière & Partenaires en action sur le terrain.",
                        "img": 'scene-1.png',
                        "alt": 'Coulisses Rivière & Partenaires',
                    },
                    {
                        "title": 'Résultats',
                        "text": 'Témoignages et cas concrets à Metz.',
                        "img": 'scene-2.png',
                        "alt": 'Résultats clients',
                    },
                    {
                        "title": 'Méthode',
                        "text": 'Processus structuré en trois temps.',
                        "img": 'scene-3.png',
                        "alt": 'Méthode Rivière & Partenaires',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Focus Expertises',
                        "alt": 'Image Expertises',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Détail métier',
                        "alt": 'Détail Rivière & Partenaires',
                    },
                ],
                "cta": {
                    "text": 'Une question sur cette offre ?',
                    "btn": 'Nous contacter',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'accompagnement.html',
                "title": 'Accompagnement — Rivière & Partenaires',
                "description": 'Accompagnement : approche et valeurs de Rivière & Partenaires.',
                "hero": {
                    "h1": 'Accompagnement',
                    "lead": 'Comprendre notre démarche accompagnement.',
                    "img": 'hero.png',
                    "alt": 'Page Accompagnement Rivière & Partenaires',
                },
                "timeline": [('2010', 'Création de Rivière & Partenaires à Metz.'), ('2016', "Extension de l'équipe et nouveaux locaux."), ('2020', 'Certification qualité et partenariats régionaux.'), ('2024', 'Plus de 500 clients accompagnés en Grand Est.')],
                "chapters": [
                    {
                        "title": 'Étape 1 — Écoute',
                        "text": 'Diagnostic gratuit et définition des objectifs.',
                        "img": 'scene-1.png',
                        "alt": 'Écoute client Rivière & Partenaires',
                    },
                    {
                        "title": 'Étape 2 — Action',
                        "text": "Mise en œuvre avec points d'étape réguliers.",
                        "img": 'scene-2.png',
                        "alt": 'Action terrain',
                    },
                    {
                        "title": 'Étape 3 — Suivi',
                        "text": 'Bilan et ajustements pour pérenniser les résultats.',
                        "img": 'scene-3.png',
                        "alt": 'Suivi Rivière & Partenaires',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Équipe Rivière & Partenaires',
                        "alt": "Photo d'équipe",
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Locaux Metz',
                        "alt": 'Bureaux à Metz',
                    },
                ],
                "cta": {
                    "text": 'Rencontrons-nous à Metz.',
                    "btn": 'Consultation',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'contact.html',
                "title": 'Contact — Rivière & Partenaires',
                "description": 'Contactez Rivière & Partenaires à Metz.',
                "hero": {
                    "h1": 'Parlons de votre projet',
                    "lead": 'Metz, Grand Est — réponse sous 24 h ouvrées.',
                    "img": 'hero.png',
                    "alt": 'Contact Rivière & Partenaires',
                },
                "story": ('Coordonnées', ['Du lundi au vendredi 9h–18h. Formulaire ci-dessous ou par téléphone.']),
                "cta": {
                    "text": 'Démonstration — aucune donnée transmise.',
                    "btn": 'Envoyer ma demande',
                    "href": '#',
                },
            },
        ],
    },
    {
        "slug": 'architecture',
        "brand": 'Atelier Nord-Est',
        "category": 'architecture',
        "layout": 'architecture',
        "nav_cta": 'Brief projet',
        "synopsis": "Agence d'architecture à Metz : réhabilitation, logements et équipements publics.",
        "nav": [
            {
                "file": 'index.html',
                "label": 'Accueil',
            },
            {
                "file": 'projets.html',
                "label": 'Projets',
            },
            {
                "file": 'methode.html',
                "label": 'Méthode',
            },
            {
                "file": 'contact.html',
                "label": 'Contact',
            },
        ],
        "pages": [
            {
                "file": 'index.html',
                "title": 'Atelier Nord-Est — Accueil',
                "description": "Agence d'architecture à Metz : réhabilitation, logements et équipements publics.…",
                "hero": {
                    "h1": 'Atelier Nord-Est : conception durable à Metz',
                    "lead": "Accompagnement de maîtres d'ouvrage en Lorraine avec exigence et proximité.",
                    "img": 'hero.png',
                    "alt": "Vue d'ensemble Atelier Nord-Est à Metz",
                },
                "story": ('Pourquoi Atelier Nord-Est ?', ["Implanté à Metz, Atelier Nord-Est connaît les réalités du terrain mosellan et les attentes d'une clientèle exigeante.", 'Notre équipe locale combine expertise métier et relation de confiance sur le long terme.']),
                "chapters": [
                    {
                        "title": 'Notre approche',
                        "text": "Méthode éprouvée et transparence à chaque étape pour maîtres d'ouvrage.",
                        "img": 'scene-1.png',
                        "alt": 'Projets chez Atelier Nord-Est',
                    },
                    {
                        "title": 'Le quotidien',
                        "text": 'Scènes de travail authentiques dans nos locaux de Metz.',
                        "img": 'scene-2.png',
                        "alt": 'Équipe au travail à Metz',
                    },
                    {
                        "title": 'Nos engagements',
                        "text": 'Qualité, réactivité et ancrage Grand Est depuis des années.',
                        "img": 'scene-3.png',
                        "alt": 'Engagement Atelier Nord-Est',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Moment de vie — Metz',
                        "alt": 'Scène Atelier Nord-Est',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Rencontre avec nos clients',
                        "alt": "Clientèle maîtres d'ouvrage",
                    },
                ],
                "cards": {
                    "title": 'Ce que nous proposons',
                    "items": [
                        {
                            "title": 'Offre essentielle',
                            "text": "Pack d'entrée adapté aux besoins courants de maîtres d'ouvrage.",
                            "img": 'card-1.png',
                            "alt": 'Offre Atelier Nord-Est',
                        },
                        {
                            "title": 'Offre premium',
                            "text": 'Accompagnement renforcé et suivi personnalisé.',
                            "img": 'card-2.png',
                            "alt": 'Service premium Atelier Nord-Est',
                        },
                        {
                            "title": 'Sur mesure',
                            "text": 'Projet spécifique ? Nous construisons la réponse ensemble.',
                            "img": 'card-3.png',
                            "alt": 'Projet sur mesure',
                        },
                    ],
                },
                "cta": {
                    "text": 'Parlons de votre projet à Metz.',
                    "btn": 'Brief projet',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'projets.html',
                "title": 'Projets — Atelier Nord-Est',
                "description": 'Projets : détails et expertises de Atelier Nord-Est à Metz.',
                "hero": {
                    "h1": 'Projets',
                    "lead": "Découvrez notre offre projets pour maîtres d'ouvrage.",
                    "img": 'hero.png',
                    "alt": 'Page Projets Atelier Nord-Est',
                },
                "story": ('Notre vision — Projets', ["Chaque prestation est calibrée pour les réalités du marché lorrain et les objectifs de maîtres d'ouvrage."]),
                "cards": {
                    "title": 'Projets',
                    "items": [
                        {
                            "title": 'Projets — niveau 1',
                            "text": 'Formule accessible et complète.',
                            "img": 'card-1.png',
                            "alt": 'Détail Projets',
                        },
                        {
                            "title": 'Projets — niveau 2',
                            "text": 'Approfondissement et options avancées.',
                            "img": 'card-2.png',
                            "alt": 'Option avancée',
                        },
                        {
                            "title": 'Projets — niveau 3',
                            "text": 'Solution intégrale clé en main.',
                            "img": 'card-3.png',
                            "alt": 'Solution intégrale',
                        },
                    ],
                },
                "chapters": [
                    {
                        "title": 'Coulisses Projets',
                        "text": "L'équipe Atelier Nord-Est en action sur le terrain.",
                        "img": 'scene-1.png',
                        "alt": 'Coulisses Atelier Nord-Est',
                    },
                    {
                        "title": 'Résultats',
                        "text": 'Témoignages et cas concrets à Metz.',
                        "img": 'scene-2.png',
                        "alt": 'Résultats clients',
                    },
                    {
                        "title": 'Méthode',
                        "text": 'Processus structuré en trois temps.',
                        "img": 'scene-3.png',
                        "alt": 'Méthode Atelier Nord-Est',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Focus Projets',
                        "alt": 'Image Projets',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Détail métier',
                        "alt": 'Détail Atelier Nord-Est',
                    },
                ],
                "cta": {
                    "text": 'Une question sur cette offre ?',
                    "btn": 'Nous contacter',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'methode.html',
                "title": 'Méthode — Atelier Nord-Est',
                "description": 'Méthode : approche et valeurs de Atelier Nord-Est.',
                "hero": {
                    "h1": 'Méthode',
                    "lead": 'Comprendre notre démarche méthode.',
                    "img": 'hero.png',
                    "alt": 'Page Méthode Atelier Nord-Est',
                },
                "timeline": [('2010', 'Création de Atelier Nord-Est à Metz.'), ('2016', "Extension de l'équipe et nouveaux locaux."), ('2020', 'Certification qualité et partenariats régionaux.'), ('2024', 'Plus de 500 clients accompagnés en Grand Est.')],
                "chapters": [
                    {
                        "title": 'Étape 1 — Écoute',
                        "text": 'Diagnostic gratuit et définition des objectifs.',
                        "img": 'scene-1.png',
                        "alt": 'Écoute client Atelier Nord-Est',
                    },
                    {
                        "title": 'Étape 2 — Action',
                        "text": "Mise en œuvre avec points d'étape réguliers.",
                        "img": 'scene-2.png',
                        "alt": 'Action terrain',
                    },
                    {
                        "title": 'Étape 3 — Suivi',
                        "text": 'Bilan et ajustements pour pérenniser les résultats.',
                        "img": 'scene-3.png',
                        "alt": 'Suivi Atelier Nord-Est',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Équipe Atelier Nord-Est',
                        "alt": "Photo d'équipe",
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Locaux Metz',
                        "alt": 'Bureaux à Metz',
                    },
                ],
                "cta": {
                    "text": 'Rencontrons-nous à Metz.',
                    "btn": 'Brief projet',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'contact.html',
                "title": 'Contact — Atelier Nord-Est',
                "description": 'Contactez Atelier Nord-Est à Metz.',
                "hero": {
                    "h1": 'Parlons de votre projet',
                    "lead": 'Metz, Grand Est — réponse sous 24 h ouvrées.',
                    "img": 'hero.png',
                    "alt": 'Contact Atelier Nord-Est',
                },
                "story": ('Coordonnées', ['Du lundi au vendredi 9h–18h. Formulaire ci-dessous ou par téléphone.']),
                "cta": {
                    "text": 'Démonstration — aucune donnée transmise.',
                    "btn": 'Envoyer ma demande',
                    "href": '#',
                },
            },
        ],
    },
    {
        "slug": 'fitness',
        "brand": 'Pulse Fitness Metz',
        "category": 'sport',
        "layout": 'fitness',
        "nav_cta": 'Essai gratuit',
        "synopsis": 'Salle de sport à Metz : cours collectifs, musculation et coaching personnalisé.',
        "nav": [
            {
                "file": 'index.html',
                "label": 'Accueil',
            },
            {
                "file": 'cours.html',
                "label": 'Cours',
            },
            {
                "file": 'tarifs.html',
                "label": 'Tarifs',
            },
            {
                "file": 'contact.html',
                "label": 'Contact',
            },
        ],
        "pages": [
            {
                "file": 'index.html',
                "title": 'Pulse Fitness Metz — Accueil',
                "description": 'Salle de sport à Metz : cours collectifs, musculation et coaching personnalisé.…',
                "hero": {
                    "h1": 'Pulse Fitness Metz : cours collectifs à Metz',
                    "lead": 'Accompagnement de sportifs en Lorraine avec exigence et proximité.',
                    "img": 'hero.png',
                    "alt": "Vue d'ensemble Pulse Fitness Metz à Metz",
                },
                "story": ('Pourquoi Pulse Fitness Metz ?', ["Implanté à Metz, Pulse Fitness Metz connaît les réalités du terrain mosellan et les attentes d'une clientèle exigeante.", 'Notre équipe locale combine expertise métier et relation de confiance sur le long terme.']),
                "chapters": [
                    {
                        "title": 'Notre approche',
                        "text": 'Méthode éprouvée et transparence à chaque étape pour sportifs.',
                        "img": 'scene-1.png',
                        "alt": 'Cours chez Pulse Fitness Metz',
                    },
                    {
                        "title": 'Le quotidien',
                        "text": 'Scènes de travail authentiques dans nos locaux de Metz.',
                        "img": 'scene-2.png',
                        "alt": 'Équipe au travail à Metz',
                    },
                    {
                        "title": 'Nos engagements',
                        "text": 'Qualité, réactivité et ancrage Grand Est depuis des années.',
                        "img": 'scene-3.png',
                        "alt": 'Engagement Pulse Fitness Metz',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Moment de vie — Metz',
                        "alt": 'Scène Pulse Fitness Metz',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Rencontre avec nos clients',
                        "alt": 'Clientèle sportifs',
                    },
                ],
                "cards": {
                    "title": 'Ce que nous proposons',
                    "items": [
                        {
                            "title": 'Offre essentielle',
                            "text": "Pack d'entrée adapté aux besoins courants de sportifs.",
                            "img": 'card-1.png',
                            "alt": 'Offre Pulse Fitness Metz',
                        },
                        {
                            "title": 'Offre premium',
                            "text": 'Accompagnement renforcé et suivi personnalisé.',
                            "img": 'card-2.png',
                            "alt": 'Service premium Pulse Fitness Metz',
                        },
                        {
                            "title": 'Sur mesure',
                            "text": 'Projet spécifique ? Nous construisons la réponse ensemble.',
                            "img": 'card-3.png',
                            "alt": 'Projet sur mesure',
                        },
                    ],
                },
                "cta": {
                    "text": 'Parlons de votre projet à Metz.',
                    "btn": 'Essai gratuit',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'cours.html',
                "title": 'Cours — Pulse Fitness Metz',
                "description": 'Cours : détails et expertises de Pulse Fitness Metz à Metz.',
                "hero": {
                    "h1": 'Cours',
                    "lead": 'Découvrez notre offre cours pour sportifs.',
                    "img": 'hero.png',
                    "alt": 'Page Cours Pulse Fitness Metz',
                },
                "story": ('Notre vision — Cours', ['Chaque prestation est calibrée pour les réalités du marché lorrain et les objectifs de sportifs.']),
                "cards": {
                    "title": 'Cours',
                    "items": [
                        {
                            "title": 'Cours — niveau 1',
                            "text": 'Formule accessible et complète.',
                            "img": 'card-1.png',
                            "alt": 'Détail Cours',
                        },
                        {
                            "title": 'Cours — niveau 2',
                            "text": 'Approfondissement et options avancées.',
                            "img": 'card-2.png',
                            "alt": 'Option avancée',
                        },
                        {
                            "title": 'Cours — niveau 3',
                            "text": 'Solution intégrale clé en main.',
                            "img": 'card-3.png',
                            "alt": 'Solution intégrale',
                        },
                    ],
                },
                "chapters": [
                    {
                        "title": 'Coulisses Cours',
                        "text": "L'équipe Pulse Fitness Metz en action sur le terrain.",
                        "img": 'scene-1.png',
                        "alt": 'Coulisses Pulse Fitness Metz',
                    },
                    {
                        "title": 'Résultats',
                        "text": 'Témoignages et cas concrets à Metz.',
                        "img": 'scene-2.png',
                        "alt": 'Résultats clients',
                    },
                    {
                        "title": 'Méthode',
                        "text": 'Processus structuré en trois temps.',
                        "img": 'scene-3.png',
                        "alt": 'Méthode Pulse Fitness Metz',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Focus Cours',
                        "alt": 'Image Cours',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Détail métier',
                        "alt": 'Détail Pulse Fitness Metz',
                    },
                ],
                "cta": {
                    "text": 'Une question sur cette offre ?',
                    "btn": 'Nous contacter',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'tarifs.html',
                "title": 'Tarifs — Pulse Fitness Metz',
                "description": 'Tarifs : approche et valeurs de Pulse Fitness Metz.',
                "hero": {
                    "h1": 'Tarifs',
                    "lead": 'Comprendre notre démarche tarifs.',
                    "img": 'hero.png',
                    "alt": 'Page Tarifs Pulse Fitness Metz',
                },
                "timeline": [('2010', 'Création de Pulse Fitness Metz à Metz.'), ('2016', "Extension de l'équipe et nouveaux locaux."), ('2020', 'Certification qualité et partenariats régionaux.'), ('2024', 'Plus de 500 clients accompagnés en Grand Est.')],
                "chapters": [
                    {
                        "title": 'Étape 1 — Écoute',
                        "text": 'Diagnostic gratuit et définition des objectifs.',
                        "img": 'scene-1.png',
                        "alt": 'Écoute client Pulse Fitness Metz',
                    },
                    {
                        "title": 'Étape 2 — Action',
                        "text": "Mise en œuvre avec points d'étape réguliers.",
                        "img": 'scene-2.png',
                        "alt": 'Action terrain',
                    },
                    {
                        "title": 'Étape 3 — Suivi',
                        "text": 'Bilan et ajustements pour pérenniser les résultats.',
                        "img": 'scene-3.png',
                        "alt": 'Suivi Pulse Fitness Metz',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Équipe Pulse Fitness Metz',
                        "alt": "Photo d'équipe",
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Locaux Metz',
                        "alt": 'Bureaux à Metz',
                    },
                ],
                "cta": {
                    "text": 'Rencontrons-nous à Metz.',
                    "btn": 'Essai gratuit',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'contact.html',
                "title": 'Contact — Pulse Fitness Metz',
                "description": 'Contactez Pulse Fitness Metz à Metz.',
                "hero": {
                    "h1": 'Parlons de votre projet',
                    "lead": 'Metz, Grand Est — réponse sous 24 h ouvrées.',
                    "img": 'hero.png',
                    "alt": 'Contact Pulse Fitness Metz',
                },
                "story": ('Coordonnées', ['Du lundi au vendredi 9h–18h. Formulaire ci-dessous ou par téléphone.']),
                "cta": {
                    "text": 'Démonstration — aucune donnée transmise.',
                    "btn": 'Envoyer ma demande',
                    "href": '#',
                },
            },
        ],
    },
    {
        "slug": 'photographie',
        "brand": 'Studio Lumière Grise',
        "category": 'creatif',
        "layout": 'photo',
        "nav_cta": 'Demander un devis',
        "synopsis": 'Photographe mariage et corporate à Nancy : reportages et portraits.',
        "nav": [
            {
                "file": 'index.html',
                "label": 'Accueil',
            },
            {
                "file": 'portfolio.html',
                "label": 'Portfolio',
            },
            {
                "file": 'prestations.html',
                "label": 'Prestations',
            },
            {
                "file": 'contact.html',
                "label": 'Contact',
            },
        ],
        "pages": [
            {
                "file": 'index.html',
                "title": 'Studio Lumière Grise — Accueil',
                "description": 'Photographe mariage et corporate à Nancy : reportages et portraits.…',
                "hero": {
                    "h1": 'Studio Lumière Grise : reportages authentiques à Nancy',
                    "lead": 'Accompagnement de couples en Lorraine avec exigence et proximité.',
                    "img": 'hero.png',
                    "alt": "Vue d'ensemble Studio Lumière Grise à Nancy",
                },
                "story": ('Pourquoi Studio Lumière Grise ?', ["Implanté à Nancy, Studio Lumière Grise connaît les réalités du terrain mosellan et les attentes d'une clientèle exigeante.", 'Notre équipe locale combine expertise métier et relation de confiance sur le long terme.']),
                "chapters": [
                    {
                        "title": 'Notre approche',
                        "text": 'Méthode éprouvée et transparence à chaque étape pour couples.',
                        "img": 'scene-1.png',
                        "alt": 'Portfolio chez Studio Lumière Grise',
                    },
                    {
                        "title": 'Le quotidien',
                        "text": 'Scènes de travail authentiques dans nos locaux de Nancy.',
                        "img": 'scene-2.png',
                        "alt": 'Équipe au travail à Nancy',
                    },
                    {
                        "title": 'Nos engagements',
                        "text": 'Qualité, réactivité et ancrage Grand Est depuis des années.',
                        "img": 'scene-3.png',
                        "alt": 'Engagement Studio Lumière Grise',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Moment de vie — Nancy',
                        "alt": 'Scène Studio Lumière Grise',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Rencontre avec nos clients',
                        "alt": 'Clientèle couples',
                    },
                ],
                "cards": {
                    "title": 'Ce que nous proposons',
                    "items": [
                        {
                            "title": 'Offre essentielle',
                            "text": "Pack d'entrée adapté aux besoins courants de couples.",
                            "img": 'card-1.png',
                            "alt": 'Offre Studio Lumière Grise',
                        },
                        {
                            "title": 'Offre premium',
                            "text": 'Accompagnement renforcé et suivi personnalisé.',
                            "img": 'card-2.png',
                            "alt": 'Service premium Studio Lumière Grise',
                        },
                        {
                            "title": 'Sur mesure',
                            "text": 'Projet spécifique ? Nous construisons la réponse ensemble.',
                            "img": 'card-3.png',
                            "alt": 'Projet sur mesure',
                        },
                    ],
                },
                "cta": {
                    "text": 'Parlons de votre projet à Nancy.',
                    "btn": 'Demander un devis',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'portfolio.html',
                "title": 'Portfolio — Studio Lumière Grise',
                "description": 'Portfolio : détails et expertises de Studio Lumière Grise à Nancy.',
                "hero": {
                    "h1": 'Portfolio',
                    "lead": 'Découvrez notre offre portfolio pour couples.',
                    "img": 'hero.png',
                    "alt": 'Page Portfolio Studio Lumière Grise',
                },
                "story": ('Notre vision — Portfolio', ['Chaque prestation est calibrée pour les réalités du marché lorrain et les objectifs de couples.']),
                "cards": {
                    "title": 'Portfolio',
                    "items": [
                        {
                            "title": 'Portfolio — niveau 1',
                            "text": 'Formule accessible et complète.',
                            "img": 'card-1.png',
                            "alt": 'Détail Portfolio',
                        },
                        {
                            "title": 'Portfolio — niveau 2',
                            "text": 'Approfondissement et options avancées.',
                            "img": 'card-2.png',
                            "alt": 'Option avancée',
                        },
                        {
                            "title": 'Portfolio — niveau 3',
                            "text": 'Solution intégrale clé en main.',
                            "img": 'card-3.png',
                            "alt": 'Solution intégrale',
                        },
                    ],
                },
                "chapters": [
                    {
                        "title": 'Coulisses Portfolio',
                        "text": "L'équipe Studio Lumière Grise en action sur le terrain.",
                        "img": 'scene-1.png',
                        "alt": 'Coulisses Studio Lumière Grise',
                    },
                    {
                        "title": 'Résultats',
                        "text": 'Témoignages et cas concrets à Nancy.',
                        "img": 'scene-2.png',
                        "alt": 'Résultats clients',
                    },
                    {
                        "title": 'Méthode',
                        "text": 'Processus structuré en trois temps.',
                        "img": 'scene-3.png',
                        "alt": 'Méthode Studio Lumière Grise',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Focus Portfolio',
                        "alt": 'Image Portfolio',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Détail métier',
                        "alt": 'Détail Studio Lumière Grise',
                    },
                ],
                "cta": {
                    "text": 'Une question sur cette offre ?',
                    "btn": 'Nous contacter',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'prestations.html',
                "title": 'Prestations — Studio Lumière Grise',
                "description": 'Prestations : approche et valeurs de Studio Lumière Grise.',
                "hero": {
                    "h1": 'Prestations',
                    "lead": 'Comprendre notre démarche prestations.',
                    "img": 'hero.png',
                    "alt": 'Page Prestations Studio Lumière Grise',
                },
                "timeline": [('2010', 'Création de Studio Lumière Grise à Nancy.'), ('2016', "Extension de l'équipe et nouveaux locaux."), ('2020', 'Certification qualité et partenariats régionaux.'), ('2024', 'Plus de 500 clients accompagnés en Grand Est.')],
                "chapters": [
                    {
                        "title": 'Étape 1 — Écoute',
                        "text": 'Diagnostic gratuit et définition des objectifs.',
                        "img": 'scene-1.png',
                        "alt": 'Écoute client Studio Lumière Grise',
                    },
                    {
                        "title": 'Étape 2 — Action',
                        "text": "Mise en œuvre avec points d'étape réguliers.",
                        "img": 'scene-2.png',
                        "alt": 'Action terrain',
                    },
                    {
                        "title": 'Étape 3 — Suivi',
                        "text": 'Bilan et ajustements pour pérenniser les résultats.',
                        "img": 'scene-3.png',
                        "alt": 'Suivi Studio Lumière Grise',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Équipe Studio Lumière Grise',
                        "alt": "Photo d'équipe",
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Locaux Nancy',
                        "alt": 'Bureaux à Nancy',
                    },
                ],
                "cta": {
                    "text": 'Rencontrons-nous à Nancy.',
                    "btn": 'Demander un devis',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'contact.html',
                "title": 'Contact — Studio Lumière Grise',
                "description": 'Contactez Studio Lumière Grise à Nancy.',
                "hero": {
                    "h1": 'Parlons de votre projet',
                    "lead": 'Nancy, Grand Est — réponse sous 24 h ouvrées.',
                    "img": 'hero.png',
                    "alt": 'Contact Studio Lumière Grise',
                },
                "story": ('Coordonnées', ['Du lundi au vendredi 9h–18h. Formulaire ci-dessous ou par téléphone.']),
                "cta": {
                    "text": 'Démonstration — aucune donnée transmise.',
                    "btn": 'Envoyer ma demande',
                    "href": '#',
                },
            },
        ],
    },
    {
        "slug": 'association',
        "brand": 'Solidarités Metz Métropole',
        "category": 'ess',
        "layout": 'association',
        "nav_cta": 'Faire un don',
        "synopsis": "Association d'utilité publique à Metz : aide alimentaire, insertion et bénévolat.",
        "nav": [
            {
                "file": 'index.html',
                "label": 'Accueil',
            },
            {
                "file": 'actions.html',
                "label": 'Nos actions',
            },
            {
                "file": 'benevolat.html',
                "label": 'Bénévolat',
            },
            {
                "file": 'contact.html',
                "label": 'Contact',
            },
        ],
        "pages": [
            {
                "file": 'index.html',
                "title": 'Solidarités Metz Métropole — Accueil',
                "description": "Association d'utilité publique à Metz : aide alimentaire, insertion et bénévolat…",
                "hero": {
                    "h1": 'Solidarités Metz Métropole : solidarité locale à Metz',
                    "lead": 'Accompagnement de bénévoles en Lorraine avec exigence et proximité.',
                    "img": 'hero.png',
                    "alt": "Vue d'ensemble Solidarités Metz Métropole à Metz",
                },
                "story": ('Pourquoi Solidarités Metz Métropole ?', ["Implanté à Metz, Solidarités Metz Métropole connaît les réalités du terrain mosellan et les attentes d'une clientèle exigeante.", 'Notre équipe locale combine expertise métier et relation de confiance sur le long terme.']),
                "chapters": [
                    {
                        "title": 'Notre approche',
                        "text": 'Méthode éprouvée et transparence à chaque étape pour bénévoles.',
                        "img": 'scene-1.png',
                        "alt": 'Nos actions chez Solidarités Metz Métropole',
                    },
                    {
                        "title": 'Le quotidien',
                        "text": 'Scènes de travail authentiques dans nos locaux de Metz.',
                        "img": 'scene-2.png',
                        "alt": 'Équipe au travail à Metz',
                    },
                    {
                        "title": 'Nos engagements',
                        "text": 'Qualité, réactivité et ancrage Grand Est depuis des années.',
                        "img": 'scene-3.png',
                        "alt": 'Engagement Solidarités Metz Métropole',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Moment de vie — Metz',
                        "alt": 'Scène Solidarités Metz Métropole',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Rencontre avec nos clients',
                        "alt": 'Clientèle bénévoles',
                    },
                ],
                "cards": {
                    "title": 'Ce que nous proposons',
                    "items": [
                        {
                            "title": 'Offre essentielle',
                            "text": "Pack d'entrée adapté aux besoins courants de bénévoles.",
                            "img": 'card-1.png',
                            "alt": 'Offre Solidarités Metz Métropole',
                        },
                        {
                            "title": 'Offre premium',
                            "text": 'Accompagnement renforcé et suivi personnalisé.',
                            "img": 'card-2.png',
                            "alt": 'Service premium Solidarités Metz Métropole',
                        },
                        {
                            "title": 'Sur mesure',
                            "text": 'Projet spécifique ? Nous construisons la réponse ensemble.',
                            "img": 'card-3.png',
                            "alt": 'Projet sur mesure',
                        },
                    ],
                },
                "cta": {
                    "text": 'Parlons de votre projet à Metz.',
                    "btn": 'Faire un don',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'actions.html',
                "title": 'Nos actions — Solidarités Metz Métropole',
                "description": 'Nos actions : détails et expertises de Solidarités Metz Métropole à Metz.',
                "hero": {
                    "h1": 'Nos actions',
                    "lead": 'Découvrez notre offre nos actions pour bénévoles.',
                    "img": 'hero.png',
                    "alt": 'Page Nos actions Solidarités Metz Métropole',
                },
                "story": ('Notre vision — Nos actions', ['Chaque prestation est calibrée pour les réalités du marché lorrain et les objectifs de bénévoles.']),
                "cards": {
                    "title": 'Nos actions',
                    "items": [
                        {
                            "title": 'Nos actions — niveau 1',
                            "text": 'Formule accessible et complète.',
                            "img": 'card-1.png',
                            "alt": 'Détail Nos actions',
                        },
                        {
                            "title": 'Nos actions — niveau 2',
                            "text": 'Approfondissement et options avancées.',
                            "img": 'card-2.png',
                            "alt": 'Option avancée',
                        },
                        {
                            "title": 'Nos actions — niveau 3',
                            "text": 'Solution intégrale clé en main.',
                            "img": 'card-3.png',
                            "alt": 'Solution intégrale',
                        },
                    ],
                },
                "chapters": [
                    {
                        "title": 'Coulisses Nos actions',
                        "text": "L'équipe Solidarités Metz Métropole en action sur le terrain.",
                        "img": 'scene-1.png',
                        "alt": 'Coulisses Solidarités Metz Métropole',
                    },
                    {
                        "title": 'Résultats',
                        "text": 'Témoignages et cas concrets à Metz.',
                        "img": 'scene-2.png',
                        "alt": 'Résultats clients',
                    },
                    {
                        "title": 'Méthode',
                        "text": 'Processus structuré en trois temps.',
                        "img": 'scene-3.png',
                        "alt": 'Méthode Solidarités Metz Métropole',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Focus Nos actions',
                        "alt": 'Image Nos actions',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Détail métier',
                        "alt": 'Détail Solidarités Metz Métropole',
                    },
                ],
                "cta": {
                    "text": 'Une question sur cette offre ?',
                    "btn": 'Nous contacter',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'benevolat.html',
                "title": 'Bénévolat — Solidarités Metz Métropole',
                "description": 'Bénévolat : approche et valeurs de Solidarités Metz Métropole.',
                "hero": {
                    "h1": 'Bénévolat',
                    "lead": 'Comprendre notre démarche bénévolat.',
                    "img": 'hero.png',
                    "alt": 'Page Bénévolat Solidarités Metz Métropole',
                },
                "timeline": [('2010', 'Création de Solidarités Metz Métropole à Metz.'), ('2016', "Extension de l'équipe et nouveaux locaux."), ('2020', 'Certification qualité et partenariats régionaux.'), ('2024', 'Plus de 500 clients accompagnés en Grand Est.')],
                "chapters": [
                    {
                        "title": 'Étape 1 — Écoute',
                        "text": 'Diagnostic gratuit et définition des objectifs.',
                        "img": 'scene-1.png',
                        "alt": 'Écoute client Solidarités Metz Métropole',
                    },
                    {
                        "title": 'Étape 2 — Action',
                        "text": "Mise en œuvre avec points d'étape réguliers.",
                        "img": 'scene-2.png',
                        "alt": 'Action terrain',
                    },
                    {
                        "title": 'Étape 3 — Suivi',
                        "text": 'Bilan et ajustements pour pérenniser les résultats.',
                        "img": 'scene-3.png',
                        "alt": 'Suivi Solidarités Metz Métropole',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Équipe Solidarités Metz Métropole',
                        "alt": "Photo d'équipe",
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Locaux Metz',
                        "alt": 'Bureaux à Metz',
                    },
                ],
                "cta": {
                    "text": 'Rencontrons-nous à Metz.',
                    "btn": 'Faire un don',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'contact.html',
                "title": 'Contact — Solidarités Metz Métropole',
                "description": 'Contactez Solidarités Metz Métropole à Metz.',
                "hero": {
                    "h1": 'Parlons de votre projet',
                    "lead": 'Metz, Grand Est — réponse sous 24 h ouvrées.',
                    "img": 'hero.png',
                    "alt": 'Contact Solidarités Metz Métropole',
                },
                "story": ('Coordonnées', ['Du lundi au vendredi 9h–18h. Formulaire ci-dessous ou par téléphone.']),
                "cta": {
                    "text": 'Démonstration — aucune donnée transmise.',
                    "btn": 'Envoyer ma demande',
                    "href": '#',
                },
            },
        ],
    },
    {
        "slug": 'education',
        "brand": 'Institut Mercure',
        "category": 'formation',
        "layout": 'education',
        "nav_cta": "S'inscrire",
        "synopsis": 'Centre de formation professionnelle à Thionville : alternance et reconversion.',
        "nav": [
            {
                "file": 'index.html',
                "label": 'Accueil',
            },
            {
                "file": 'parcours.html',
                "label": 'Parcours',
            },
            {
                "file": 'campus.html',
                "label": 'Campus',
            },
            {
                "file": 'contact.html',
                "label": 'Contact',
            },
        ],
        "pages": [
            {
                "file": 'index.html',
                "title": 'Institut Mercure — Accueil',
                "description": 'Centre de formation professionnelle à Thionville : alternance et reconversion.…',
                "hero": {
                    "h1": 'Institut Mercure : compétences métiers à Thionville',
                    "lead": 'Accompagnement de apprenants en Lorraine avec exigence et proximité.',
                    "img": 'hero.png',
                    "alt": "Vue d'ensemble Institut Mercure à Thionville",
                },
                "story": ('Pourquoi Institut Mercure ?', ["Implanté à Thionville, Institut Mercure connaît les réalités du terrain mosellan et les attentes d'une clientèle exigeante.", 'Notre équipe locale combine expertise métier et relation de confiance sur le long terme.']),
                "chapters": [
                    {
                        "title": 'Notre approche',
                        "text": 'Méthode éprouvée et transparence à chaque étape pour apprenants.',
                        "img": 'scene-1.png',
                        "alt": 'Parcours chez Institut Mercure',
                    },
                    {
                        "title": 'Le quotidien',
                        "text": 'Scènes de travail authentiques dans nos locaux de Thionville.',
                        "img": 'scene-2.png',
                        "alt": 'Équipe au travail à Thionville',
                    },
                    {
                        "title": 'Nos engagements',
                        "text": 'Qualité, réactivité et ancrage Grand Est depuis des années.',
                        "img": 'scene-3.png',
                        "alt": 'Engagement Institut Mercure',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Moment de vie — Thionville',
                        "alt": 'Scène Institut Mercure',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Rencontre avec nos clients',
                        "alt": 'Clientèle apprenants',
                    },
                ],
                "cards": {
                    "title": 'Ce que nous proposons',
                    "items": [
                        {
                            "title": 'Offre essentielle',
                            "text": "Pack d'entrée adapté aux besoins courants de apprenants.",
                            "img": 'card-1.png',
                            "alt": 'Offre Institut Mercure',
                        },
                        {
                            "title": 'Offre premium',
                            "text": 'Accompagnement renforcé et suivi personnalisé.',
                            "img": 'card-2.png',
                            "alt": 'Service premium Institut Mercure',
                        },
                        {
                            "title": 'Sur mesure',
                            "text": 'Projet spécifique ? Nous construisons la réponse ensemble.',
                            "img": 'card-3.png',
                            "alt": 'Projet sur mesure',
                        },
                    ],
                },
                "cta": {
                    "text": 'Parlons de votre projet à Thionville.',
                    "btn": "S'inscrire",
                    "href": 'contact.html',
                },
            },
            {
                "file": 'parcours.html',
                "title": 'Parcours — Institut Mercure',
                "description": 'Parcours : détails et expertises de Institut Mercure à Thionville.',
                "hero": {
                    "h1": 'Parcours',
                    "lead": 'Découvrez notre offre parcours pour apprenants.',
                    "img": 'hero.png',
                    "alt": 'Page Parcours Institut Mercure',
                },
                "story": ('Notre vision — Parcours', ['Chaque prestation est calibrée pour les réalités du marché lorrain et les objectifs de apprenants.']),
                "cards": {
                    "title": 'Parcours',
                    "items": [
                        {
                            "title": 'Parcours — niveau 1',
                            "text": 'Formule accessible et complète.',
                            "img": 'card-1.png',
                            "alt": 'Détail Parcours',
                        },
                        {
                            "title": 'Parcours — niveau 2',
                            "text": 'Approfondissement et options avancées.',
                            "img": 'card-2.png',
                            "alt": 'Option avancée',
                        },
                        {
                            "title": 'Parcours — niveau 3',
                            "text": 'Solution intégrale clé en main.',
                            "img": 'card-3.png',
                            "alt": 'Solution intégrale',
                        },
                    ],
                },
                "chapters": [
                    {
                        "title": 'Coulisses Parcours',
                        "text": "L'équipe Institut Mercure en action sur le terrain.",
                        "img": 'scene-1.png',
                        "alt": 'Coulisses Institut Mercure',
                    },
                    {
                        "title": 'Résultats',
                        "text": 'Témoignages et cas concrets à Thionville.',
                        "img": 'scene-2.png',
                        "alt": 'Résultats clients',
                    },
                    {
                        "title": 'Méthode',
                        "text": 'Processus structuré en trois temps.',
                        "img": 'scene-3.png',
                        "alt": 'Méthode Institut Mercure',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Focus Parcours',
                        "alt": 'Image Parcours',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Détail métier',
                        "alt": 'Détail Institut Mercure',
                    },
                ],
                "cta": {
                    "text": 'Une question sur cette offre ?',
                    "btn": 'Nous contacter',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'campus.html',
                "title": 'Campus — Institut Mercure',
                "description": 'Campus : approche et valeurs de Institut Mercure.',
                "hero": {
                    "h1": 'Campus',
                    "lead": 'Comprendre notre démarche campus.',
                    "img": 'hero.png',
                    "alt": 'Page Campus Institut Mercure',
                },
                "timeline": [('2010', 'Création de Institut Mercure à Thionville.'), ('2016', "Extension de l'équipe et nouveaux locaux."), ('2020', 'Certification qualité et partenariats régionaux.'), ('2024', 'Plus de 500 clients accompagnés en Grand Est.')],
                "chapters": [
                    {
                        "title": 'Étape 1 — Écoute',
                        "text": 'Diagnostic gratuit et définition des objectifs.',
                        "img": 'scene-1.png',
                        "alt": 'Écoute client Institut Mercure',
                    },
                    {
                        "title": 'Étape 2 — Action',
                        "text": "Mise en œuvre avec points d'étape réguliers.",
                        "img": 'scene-2.png',
                        "alt": 'Action terrain',
                    },
                    {
                        "title": 'Étape 3 — Suivi',
                        "text": 'Bilan et ajustements pour pérenniser les résultats.',
                        "img": 'scene-3.png',
                        "alt": 'Suivi Institut Mercure',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Équipe Institut Mercure',
                        "alt": "Photo d'équipe",
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Locaux Thionville',
                        "alt": 'Bureaux à Thionville',
                    },
                ],
                "cta": {
                    "text": 'Rencontrons-nous à Thionville.',
                    "btn": "S'inscrire",
                    "href": 'contact.html',
                },
            },
            {
                "file": 'contact.html',
                "title": 'Contact — Institut Mercure',
                "description": 'Contactez Institut Mercure à Thionville.',
                "hero": {
                    "h1": 'Parlons de votre projet',
                    "lead": 'Thionville, Grand Est — réponse sous 24 h ouvrées.',
                    "img": 'hero.png',
                    "alt": 'Contact Institut Mercure',
                },
                "story": ('Coordonnées', ['Du lundi au vendredi 9h–18h. Formulaire ci-dessous ou par téléphone.']),
                "cta": {
                    "text": 'Démonstration — aucune donnée transmise.',
                    "btn": 'Envoyer ma demande',
                    "href": '#',
                },
            },
        ],
    },
    {
        "slug": 'services',
        "brand": 'Proprio Facility',
        "category": 'services',
        "layout": 'facility',
        "nav_cta": 'Demander un devis',
        "synopsis": 'Facility management et conciergerie pour immeubles tertiaires en Lorraine.',
        "nav": [
            {
                "file": 'index.html',
                "label": 'Accueil',
            },
            {
                "file": 'offres.html',
                "label": 'Offres',
            },
            {
                "file": 'secteurs.html',
                "label": 'Secteurs',
            },
            {
                "file": 'contact.html',
                "label": 'Contact',
            },
        ],
        "pages": [
            {
                "file": 'index.html',
                "title": 'Proprio Facility — Accueil',
                "description": 'Facility management et conciergerie pour immeubles tertiaires en Lorraine.…',
                "hero": {
                    "h1": 'Proprio Facility : services sur mesure à Metz',
                    "lead": 'Accompagnement de gestionnaires en Lorraine avec exigence et proximité.',
                    "img": 'hero.png',
                    "alt": "Vue d'ensemble Proprio Facility à Metz",
                },
                "story": ('Pourquoi Proprio Facility ?', ["Implanté à Metz, Proprio Facility connaît les réalités du terrain mosellan et les attentes d'une clientèle exigeante.", 'Notre équipe locale combine expertise métier et relation de confiance sur le long terme.']),
                "chapters": [
                    {
                        "title": 'Notre approche',
                        "text": 'Méthode éprouvée et transparence à chaque étape pour gestionnaires.',
                        "img": 'scene-1.png',
                        "alt": 'Offres chez Proprio Facility',
                    },
                    {
                        "title": 'Le quotidien',
                        "text": 'Scènes de travail authentiques dans nos locaux de Metz.',
                        "img": 'scene-2.png',
                        "alt": 'Équipe au travail à Metz',
                    },
                    {
                        "title": 'Nos engagements',
                        "text": 'Qualité, réactivité et ancrage Grand Est depuis des années.',
                        "img": 'scene-3.png',
                        "alt": 'Engagement Proprio Facility',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Moment de vie — Metz',
                        "alt": 'Scène Proprio Facility',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Rencontre avec nos clients',
                        "alt": 'Clientèle gestionnaires',
                    },
                ],
                "cards": {
                    "title": 'Ce que nous proposons',
                    "items": [
                        {
                            "title": 'Offre essentielle',
                            "text": "Pack d'entrée adapté aux besoins courants de gestionnaires.",
                            "img": 'card-1.png',
                            "alt": 'Offre Proprio Facility',
                        },
                        {
                            "title": 'Offre premium',
                            "text": 'Accompagnement renforcé et suivi personnalisé.',
                            "img": 'card-2.png',
                            "alt": 'Service premium Proprio Facility',
                        },
                        {
                            "title": 'Sur mesure',
                            "text": 'Projet spécifique ? Nous construisons la réponse ensemble.',
                            "img": 'card-3.png',
                            "alt": 'Projet sur mesure',
                        },
                    ],
                },
                "cta": {
                    "text": 'Parlons de votre projet à Metz.',
                    "btn": 'Demander un devis',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'offres.html',
                "title": 'Offres — Proprio Facility',
                "description": 'Offres : détails et expertises de Proprio Facility à Metz.',
                "hero": {
                    "h1": 'Offres',
                    "lead": 'Découvrez notre offre offres pour gestionnaires.',
                    "img": 'hero.png',
                    "alt": 'Page Offres Proprio Facility',
                },
                "story": ('Notre vision — Offres', ['Chaque prestation est calibrée pour les réalités du marché lorrain et les objectifs de gestionnaires.']),
                "cards": {
                    "title": 'Offres',
                    "items": [
                        {
                            "title": 'Offres — niveau 1',
                            "text": 'Formule accessible et complète.',
                            "img": 'card-1.png',
                            "alt": 'Détail Offres',
                        },
                        {
                            "title": 'Offres — niveau 2',
                            "text": 'Approfondissement et options avancées.',
                            "img": 'card-2.png',
                            "alt": 'Option avancée',
                        },
                        {
                            "title": 'Offres — niveau 3',
                            "text": 'Solution intégrale clé en main.',
                            "img": 'card-3.png',
                            "alt": 'Solution intégrale',
                        },
                    ],
                },
                "chapters": [
                    {
                        "title": 'Coulisses Offres',
                        "text": "L'équipe Proprio Facility en action sur le terrain.",
                        "img": 'scene-1.png',
                        "alt": 'Coulisses Proprio Facility',
                    },
                    {
                        "title": 'Résultats',
                        "text": 'Témoignages et cas concrets à Metz.',
                        "img": 'scene-2.png',
                        "alt": 'Résultats clients',
                    },
                    {
                        "title": 'Méthode',
                        "text": 'Processus structuré en trois temps.',
                        "img": 'scene-3.png',
                        "alt": 'Méthode Proprio Facility',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Focus Offres',
                        "alt": 'Image Offres',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Détail métier',
                        "alt": 'Détail Proprio Facility',
                    },
                ],
                "cta": {
                    "text": 'Une question sur cette offre ?',
                    "btn": 'Nous contacter',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'secteurs.html',
                "title": 'Secteurs — Proprio Facility',
                "description": 'Secteurs : approche et valeurs de Proprio Facility.',
                "hero": {
                    "h1": 'Secteurs',
                    "lead": 'Comprendre notre démarche secteurs.',
                    "img": 'hero.png',
                    "alt": 'Page Secteurs Proprio Facility',
                },
                "timeline": [('2010', 'Création de Proprio Facility à Metz.'), ('2016', "Extension de l'équipe et nouveaux locaux."), ('2020', 'Certification qualité et partenariats régionaux.'), ('2024', 'Plus de 500 clients accompagnés en Grand Est.')],
                "chapters": [
                    {
                        "title": 'Étape 1 — Écoute',
                        "text": 'Diagnostic gratuit et définition des objectifs.',
                        "img": 'scene-1.png',
                        "alt": 'Écoute client Proprio Facility',
                    },
                    {
                        "title": 'Étape 2 — Action',
                        "text": "Mise en œuvre avec points d'étape réguliers.",
                        "img": 'scene-2.png',
                        "alt": 'Action terrain',
                    },
                    {
                        "title": 'Étape 3 — Suivi',
                        "text": 'Bilan et ajustements pour pérenniser les résultats.',
                        "img": 'scene-3.png',
                        "alt": 'Suivi Proprio Facility',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Équipe Proprio Facility',
                        "alt": "Photo d'équipe",
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Locaux Metz',
                        "alt": 'Bureaux à Metz',
                    },
                ],
                "cta": {
                    "text": 'Rencontrons-nous à Metz.',
                    "btn": 'Demander un devis',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'contact.html',
                "title": 'Contact — Proprio Facility',
                "description": 'Contactez Proprio Facility à Metz.',
                "hero": {
                    "h1": 'Parlons de votre projet',
                    "lead": 'Metz, Grand Est — réponse sous 24 h ouvrées.',
                    "img": 'hero.png',
                    "alt": 'Contact Proprio Facility',
                },
                "story": ('Coordonnées', ['Du lundi au vendredi 9h–18h. Formulaire ci-dessous ou par téléphone.']),
                "cta": {
                    "text": 'Démonstration — aucune donnée transmise.',
                    "btn": 'Envoyer ma demande',
                    "href": '#',
                },
            },
        ],
    },
    {
        "slug": 'etablissement',
        "brand": 'Hôtel Stanislas Collection',
        "category": 'hotel',
        "layout": 'hotel',
        "nav_cta": 'Réserver',
        "synopsis": 'Hôtel 4 étoiles à Nancy : chambres, spa et séminaires place Stanislas.',
        "nav": [
            {
                "file": 'index.html',
                "label": 'Accueil',
            },
            {
                "file": 'chambres.html',
                "label": 'Chambres',
            },
            {
                "file": 'seminaires.html',
                "label": 'Séminaires',
            },
            {
                "file": 'contact.html',
                "label": 'Contact',
            },
        ],
        "pages": [
            {
                "file": 'index.html',
                "title": 'Hôtel Stanislas Collection — Accueil',
                "description": 'Hôtel 4 étoiles à Nancy : chambres, spa et séminaires place Stanislas.…',
                "hero": {
                    "h1": 'Hôtel Stanislas Collection : hospitalité premium à Nancy',
                    "lead": 'Accompagnement de voyageurs en Lorraine avec exigence et proximité.',
                    "img": 'hero.png',
                    "alt": "Vue d'ensemble Hôtel Stanislas Collection à Nancy",
                },
                "story": ('Pourquoi Hôtel Stanislas Collection ?', ["Implanté à Nancy, Hôtel Stanislas Collection connaît les réalités du terrain mosellan et les attentes d'une clientèle exigeante.", 'Notre équipe locale combine expertise métier et relation de confiance sur le long terme.']),
                "chapters": [
                    {
                        "title": 'Notre approche',
                        "text": 'Méthode éprouvée et transparence à chaque étape pour voyageurs.',
                        "img": 'scene-1.png',
                        "alt": 'Chambres chez Hôtel Stanislas Collection',
                    },
                    {
                        "title": 'Le quotidien',
                        "text": 'Scènes de travail authentiques dans nos locaux de Nancy.',
                        "img": 'scene-2.png',
                        "alt": 'Équipe au travail à Nancy',
                    },
                    {
                        "title": 'Nos engagements',
                        "text": 'Qualité, réactivité et ancrage Grand Est depuis des années.',
                        "img": 'scene-3.png',
                        "alt": 'Engagement Hôtel Stanislas Collection',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Moment de vie — Nancy',
                        "alt": 'Scène Hôtel Stanislas Collection',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Rencontre avec nos clients',
                        "alt": 'Clientèle voyageurs',
                    },
                ],
                "cards": {
                    "title": 'Ce que nous proposons',
                    "items": [
                        {
                            "title": 'Offre essentielle',
                            "text": "Pack d'entrée adapté aux besoins courants de voyageurs.",
                            "img": 'card-1.png',
                            "alt": 'Offre Hôtel Stanislas Collection',
                        },
                        {
                            "title": 'Offre premium',
                            "text": 'Accompagnement renforcé et suivi personnalisé.',
                            "img": 'card-2.png',
                            "alt": 'Service premium Hôtel Stanislas Collection',
                        },
                        {
                            "title": 'Sur mesure',
                            "text": 'Projet spécifique ? Nous construisons la réponse ensemble.',
                            "img": 'card-3.png',
                            "alt": 'Projet sur mesure',
                        },
                    ],
                },
                "cta": {
                    "text": 'Parlons de votre projet à Nancy.',
                    "btn": 'Réserver',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'chambres.html',
                "title": 'Chambres — Hôtel Stanislas Collection',
                "description": 'Chambres : détails et expertises de Hôtel Stanislas Collection à Nancy.',
                "hero": {
                    "h1": 'Chambres',
                    "lead": 'Découvrez notre offre chambres pour voyageurs.',
                    "img": 'hero.png',
                    "alt": 'Page Chambres Hôtel Stanislas Collection',
                },
                "story": ('Notre vision — Chambres', ['Chaque prestation est calibrée pour les réalités du marché lorrain et les objectifs de voyageurs.']),
                "cards": {
                    "title": 'Chambres',
                    "items": [
                        {
                            "title": 'Chambres — niveau 1',
                            "text": 'Formule accessible et complète.',
                            "img": 'card-1.png',
                            "alt": 'Détail Chambres',
                        },
                        {
                            "title": 'Chambres — niveau 2',
                            "text": 'Approfondissement et options avancées.',
                            "img": 'card-2.png',
                            "alt": 'Option avancée',
                        },
                        {
                            "title": 'Chambres — niveau 3',
                            "text": 'Solution intégrale clé en main.',
                            "img": 'card-3.png',
                            "alt": 'Solution intégrale',
                        },
                    ],
                },
                "chapters": [
                    {
                        "title": 'Coulisses Chambres',
                        "text": "L'équipe Hôtel Stanislas Collection en action sur le terrain.",
                        "img": 'scene-1.png',
                        "alt": 'Coulisses Hôtel Stanislas Collection',
                    },
                    {
                        "title": 'Résultats',
                        "text": 'Témoignages et cas concrets à Nancy.',
                        "img": 'scene-2.png',
                        "alt": 'Résultats clients',
                    },
                    {
                        "title": 'Méthode',
                        "text": 'Processus structuré en trois temps.',
                        "img": 'scene-3.png',
                        "alt": 'Méthode Hôtel Stanislas Collection',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Focus Chambres',
                        "alt": 'Image Chambres',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Détail métier',
                        "alt": 'Détail Hôtel Stanislas Collection',
                    },
                ],
                "cta": {
                    "text": 'Une question sur cette offre ?',
                    "btn": 'Nous contacter',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'seminaires.html',
                "title": 'Séminaires — Hôtel Stanislas Collection',
                "description": 'Séminaires : approche et valeurs de Hôtel Stanislas Collection.',
                "hero": {
                    "h1": 'Séminaires',
                    "lead": 'Comprendre notre démarche séminaires.',
                    "img": 'hero.png',
                    "alt": 'Page Séminaires Hôtel Stanislas Collection',
                },
                "timeline": [('2010', 'Création de Hôtel Stanislas Collection à Nancy.'), ('2016', "Extension de l'équipe et nouveaux locaux."), ('2020', 'Certification qualité et partenariats régionaux.'), ('2024', 'Plus de 500 clients accompagnés en Grand Est.')],
                "chapters": [
                    {
                        "title": 'Étape 1 — Écoute',
                        "text": 'Diagnostic gratuit et définition des objectifs.',
                        "img": 'scene-1.png',
                        "alt": 'Écoute client Hôtel Stanislas Collection',
                    },
                    {
                        "title": 'Étape 2 — Action',
                        "text": "Mise en œuvre avec points d'étape réguliers.",
                        "img": 'scene-2.png',
                        "alt": 'Action terrain',
                    },
                    {
                        "title": 'Étape 3 — Suivi',
                        "text": 'Bilan et ajustements pour pérenniser les résultats.',
                        "img": 'scene-3.png',
                        "alt": 'Suivi Hôtel Stanislas Collection',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Équipe Hôtel Stanislas Collection',
                        "alt": "Photo d'équipe",
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Locaux Nancy',
                        "alt": 'Bureaux à Nancy',
                    },
                ],
                "cta": {
                    "text": 'Rencontrons-nous à Nancy.',
                    "btn": 'Réserver',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'contact.html',
                "title": 'Contact — Hôtel Stanislas Collection',
                "description": 'Contactez Hôtel Stanislas Collection à Nancy.',
                "hero": {
                    "h1": 'Parlons de votre projet',
                    "lead": 'Nancy, Grand Est — réponse sous 24 h ouvrées.',
                    "img": 'hero.png',
                    "alt": 'Contact Hôtel Stanislas Collection',
                },
                "story": ('Coordonnées', ['Du lundi au vendredi 9h–18h. Formulaire ci-dessous ou par téléphone.']),
                "cta": {
                    "text": 'Démonstration — aucune donnée transmise.',
                    "btn": 'Envoyer ma demande',
                    "href": '#',
                },
            },
        ],
    },
    {
        "slug": 'technologie',
        "brand": 'Synapse Lorraine',
        "category": 'tech',
        "layout": 'tech',
        "nav_cta": 'Demander une démo',
        "synopsis": 'Éditeur logiciel B2B à Metz : solutions data pour industriels du Grand Est.',
        "nav": [
            {
                "file": 'index.html',
                "label": 'Accueil',
            },
            {
                "file": 'produit.html',
                "label": 'Produit',
            },
            {
                "file": 'clients.html',
                "label": 'Clients',
            },
            {
                "file": 'contact.html',
                "label": 'Contact',
            },
        ],
        "pages": [
            {
                "file": 'index.html',
                "title": 'Synapse Lorraine — Accueil',
                "description": 'Éditeur logiciel B2B à Metz : solutions data pour industriels du Grand Est.…',
                "hero": {
                    "h1": 'Synapse Lorraine : plateforme data à Metz',
                    "lead": 'Accompagnement de DSI en Lorraine avec exigence et proximité.',
                    "img": 'hero.png',
                    "alt": "Vue d'ensemble Synapse Lorraine à Metz",
                },
                "story": ('Pourquoi Synapse Lorraine ?', ["Implanté à Metz, Synapse Lorraine connaît les réalités du terrain mosellan et les attentes d'une clientèle exigeante.", 'Notre équipe locale combine expertise métier et relation de confiance sur le long terme.']),
                "chapters": [
                    {
                        "title": 'Notre approche',
                        "text": 'Méthode éprouvée et transparence à chaque étape pour DSI.',
                        "img": 'scene-1.png',
                        "alt": 'Produit chez Synapse Lorraine',
                    },
                    {
                        "title": 'Le quotidien',
                        "text": 'Scènes de travail authentiques dans nos locaux de Metz.',
                        "img": 'scene-2.png',
                        "alt": 'Équipe au travail à Metz',
                    },
                    {
                        "title": 'Nos engagements',
                        "text": 'Qualité, réactivité et ancrage Grand Est depuis des années.',
                        "img": 'scene-3.png',
                        "alt": 'Engagement Synapse Lorraine',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Moment de vie — Metz',
                        "alt": 'Scène Synapse Lorraine',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Rencontre avec nos clients',
                        "alt": 'Clientèle DSI',
                    },
                ],
                "cards": {
                    "title": 'Ce que nous proposons',
                    "items": [
                        {
                            "title": 'Offre essentielle',
                            "text": "Pack d'entrée adapté aux besoins courants de DSI.",
                            "img": 'card-1.png',
                            "alt": 'Offre Synapse Lorraine',
                        },
                        {
                            "title": 'Offre premium',
                            "text": 'Accompagnement renforcé et suivi personnalisé.',
                            "img": 'card-2.png',
                            "alt": 'Service premium Synapse Lorraine',
                        },
                        {
                            "title": 'Sur mesure',
                            "text": 'Projet spécifique ? Nous construisons la réponse ensemble.',
                            "img": 'card-3.png',
                            "alt": 'Projet sur mesure',
                        },
                    ],
                },
                "cta": {
                    "text": 'Parlons de votre projet à Metz.',
                    "btn": 'Demander une démo',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'produit.html',
                "title": 'Produit — Synapse Lorraine',
                "description": 'Produit : détails et expertises de Synapse Lorraine à Metz.',
                "hero": {
                    "h1": 'Produit',
                    "lead": 'Découvrez notre offre produit pour DSI.',
                    "img": 'hero.png',
                    "alt": 'Page Produit Synapse Lorraine',
                },
                "story": ('Notre vision — Produit', ['Chaque prestation est calibrée pour les réalités du marché lorrain et les objectifs de DSI.']),
                "cards": {
                    "title": 'Produit',
                    "items": [
                        {
                            "title": 'Produit — niveau 1',
                            "text": 'Formule accessible et complète.',
                            "img": 'card-1.png',
                            "alt": 'Détail Produit',
                        },
                        {
                            "title": 'Produit — niveau 2',
                            "text": 'Approfondissement et options avancées.',
                            "img": 'card-2.png',
                            "alt": 'Option avancée',
                        },
                        {
                            "title": 'Produit — niveau 3',
                            "text": 'Solution intégrale clé en main.',
                            "img": 'card-3.png',
                            "alt": 'Solution intégrale',
                        },
                    ],
                },
                "chapters": [
                    {
                        "title": 'Coulisses Produit',
                        "text": "L'équipe Synapse Lorraine en action sur le terrain.",
                        "img": 'scene-1.png',
                        "alt": 'Coulisses Synapse Lorraine',
                    },
                    {
                        "title": 'Résultats',
                        "text": 'Témoignages et cas concrets à Metz.',
                        "img": 'scene-2.png',
                        "alt": 'Résultats clients',
                    },
                    {
                        "title": 'Méthode',
                        "text": 'Processus structuré en trois temps.',
                        "img": 'scene-3.png',
                        "alt": 'Méthode Synapse Lorraine',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Focus Produit',
                        "alt": 'Image Produit',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Détail métier',
                        "alt": 'Détail Synapse Lorraine',
                    },
                ],
                "cta": {
                    "text": 'Une question sur cette offre ?',
                    "btn": 'Nous contacter',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'clients.html',
                "title": 'Clients — Synapse Lorraine',
                "description": 'Clients : approche et valeurs de Synapse Lorraine.',
                "hero": {
                    "h1": 'Clients',
                    "lead": 'Comprendre notre démarche clients.',
                    "img": 'hero.png',
                    "alt": 'Page Clients Synapse Lorraine',
                },
                "timeline": [('2010', 'Création de Synapse Lorraine à Metz.'), ('2016', "Extension de l'équipe et nouveaux locaux."), ('2020', 'Certification qualité et partenariats régionaux.'), ('2024', 'Plus de 500 clients accompagnés en Grand Est.')],
                "chapters": [
                    {
                        "title": 'Étape 1 — Écoute',
                        "text": 'Diagnostic gratuit et définition des objectifs.',
                        "img": 'scene-1.png',
                        "alt": 'Écoute client Synapse Lorraine',
                    },
                    {
                        "title": 'Étape 2 — Action',
                        "text": "Mise en œuvre avec points d'étape réguliers.",
                        "img": 'scene-2.png',
                        "alt": 'Action terrain',
                    },
                    {
                        "title": 'Étape 3 — Suivi',
                        "text": 'Bilan et ajustements pour pérenniser les résultats.',
                        "img": 'scene-3.png',
                        "alt": 'Suivi Synapse Lorraine',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Équipe Synapse Lorraine',
                        "alt": "Photo d'équipe",
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Locaux Metz',
                        "alt": 'Bureaux à Metz',
                    },
                ],
                "cta": {
                    "text": 'Rencontrons-nous à Metz.',
                    "btn": 'Demander une démo',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'contact.html',
                "title": 'Contact — Synapse Lorraine',
                "description": 'Contactez Synapse Lorraine à Metz.',
                "hero": {
                    "h1": 'Parlons de votre projet',
                    "lead": 'Metz, Grand Est — réponse sous 24 h ouvrées.',
                    "img": 'hero.png',
                    "alt": 'Contact Synapse Lorraine',
                },
                "story": ('Coordonnées', ['Du lundi au vendredi 9h–18h. Formulaire ci-dessous ou par téléphone.']),
                "cta": {
                    "text": 'Démonstration — aucune donnée transmise.',
                    "btn": 'Envoyer ma demande',
                    "href": '#',
                },
            },
        ],
    },
    {
        "slug": 'saas-landing',
        "brand": 'FlowMetrics',
        "category": 'saas',
        "layout": 'saas',
        "nav_cta": 'Essai gratuit',
        "synopsis": 'Transformez vos données en décisions : hero conversion, pricing contrasté et preuves sociales.',
        "nav": [
            {
                "file": 'index.html',
                "label": 'Accueil',
            },
            {
                "file": 'fonctionnalites.html',
                "label": 'Fonctionnalités',
            },
            {
                "file": 'tarifs.html',
                "label": 'Tarifs',
            },
            {
                "file": 'contact.html',
                "label": 'Contact',
            },
        ],
        "pages": [
            {
                "file": 'index.html',
                "title": 'FlowMetrics — Landing SaaS analytics pour équipes produit.',
                "description": 'Transformez vos données en décisions : hero conversion, pricing contrasté et preuves sociales.',
                "hero": {
                    "h1": 'FlowMetrics : Landing SaaS analytics pour équipes produit.',
                    "lead": 'Transformez vos données en décisions : hero conversion, pricing contrasté et preuves sociales.',
                    "img": 'hero.png',
                    "alt": "Interface FlowMetrics — écran d'accueil produit",
                },
                "story": ('Le problème que nous résolvons', ['Les équipes produit perdent du temps sur des outils fragmentés et des tableaux Excel obsolètes.', "FlowMetrics centralise l'essentiel dans une interface claire, pensée pour le Grand Est et au-delà."]),
                "chapters": [
                    {
                        "title": 'Interface principale',
                        "text": 'Design épuré, hiérarchie visuelle et CTA visibles.',
                        "img": 'scene-1.png',
                        "alt": 'UI FlowMetrics — dashboard',
                    },
                    {
                        "title": 'Workflow clé',
                        "text": 'Parcours utilisateur optimisé en trois clics.',
                        "img": 'scene-2.png',
                        "alt": 'Workflow FlowMetrics',
                    },
                    {
                        "title": 'Intégrations',
                        "text": 'API REST, webhooks et connecteurs métier.',
                        "img": 'scene-3.png',
                        "alt": 'Intégrations FlowMetrics',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Capture produit',
                        "alt": 'Écran FlowMetrics',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Vue mobile',
                        "alt": 'App mobile FlowMetrics',
                    },
                ],
                "cards": {
                    "title": 'Fonctionnalités clés',
                    "items": [
                        {
                            "title": 'Analytics',
                            "text": 'Tableaux de bord temps réel et exports.',
                            "img": 'card-1.png',
                            "alt": 'Analytics FlowMetrics',
                        },
                        {
                            "title": 'Collaboration',
                            "text": 'Équipes synchronisées et commentaires.',
                            "img": 'card-2.png',
                            "alt": 'Collab FlowMetrics',
                        },
                        {
                            "title": 'Sécurité',
                            "text": 'RGPD, SSO et chiffrement bout en bout.',
                            "img": 'card-3.png',
                            "alt": 'Sécurité FlowMetrics',
                        },
                    ],
                },
                "cta": {
                    "text": "14 jours d'essai gratuit, sans carte bancaire.",
                    "btn": "Démarrer l'essai",
                    "href": 'contact.html',
                },
            },
            {
                "file": 'fonctionnalites.html',
                "title": 'Fonctionnalités — FlowMetrics',
                "description": 'Détail des fonctionnalités FlowMetrics.',
                "hero": {
                    "h1": 'Fonctionnalités',
                    "lead": 'Tout ce dont votre équipe a besoin.',
                    "img": 'hero.png',
                    "alt": 'Écran fonctionnalités FlowMetrics',
                },
                "story": ("Conçu pour l'adoption", ["Réduction de l'effort cognitif, copy orienté bénéfice et feedback immédiat."]),
                "chapters": [
                    {
                        "title": 'Étape / Module 1',
                        "text": 'Configuration initiale guidée.',
                        "img": 'scene-1.png',
                        "alt": 'Module 1 FlowMetrics',
                    },
                    {
                        "title": 'Étape / Module 2',
                        "text": 'Import et synchronisation des données.',
                        "img": 'scene-2.png',
                        "alt": 'Module 2 FlowMetrics',
                    },
                    {
                        "title": 'Étape / Module 3',
                        "text": "Premiers insights et partage d'équipe.",
                        "img": 'scene-3.png',
                        "alt": 'Module 3 FlowMetrics',
                    },
                ],
                "cards": {
                    "title": 'Avant / Après',
                    "items": [
                        {
                            "title": 'Avant',
                            "text": 'Données éparpillées, décisions lentes.',
                            "img": 'card-1.png',
                            "alt": 'Avant FlowMetrics',
                        },
                        {
                            "title": 'Transition',
                            "text": 'Migration assistée en 48 h.',
                            "img": 'card-2.png',
                            "alt": 'Migration FlowMetrics',
                        },
                        {
                            "title": 'Après',
                            "text": 'Une source de vérité partagée.',
                            "img": 'card-3.png',
                            "alt": 'Après FlowMetrics',
                        },
                    ],
                },
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Détail UI',
                        "alt": 'Composant FlowMetrics',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Comparatif',
                        "alt": 'Tableau comparatif',
                    },
                ],
                "cta": {
                    "text": 'Voir une démo personnalisée.',
                    "btn": 'Réserver une démo',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'tarifs.html',
                "title": 'Tarifs — FlowMetrics',
                "description": 'Grille tarifaire FlowMetrics.',
                "hero": {
                    "h1": 'Tarifs transparents',
                    "lead": 'Plan recommandé mis en avant, sans frais cachés.',
                    "img": 'hero.png',
                    "alt": 'Page tarifs FlowMetrics',
                },
                "cards": {
                    "title": 'Nos offres',
                    "items": [
                        {
                            "title": 'Starter',
                            "text": "Pour les petites équipes — jusqu'à 5 utilisateurs.",
                            "img": 'card-1.png',
                            "alt": 'Plan Starter FlowMetrics',
                        },
                        {
                            "title": 'Pro',
                            "text": 'Le plus populaire — illimité et support prioritaire.',
                            "img": 'card-2.png',
                            "alt": 'Plan Pro FlowMetrics',
                        },
                        {
                            "title": 'Enterprise',
                            "text": 'SSO, SLA et account manager dédié.',
                            "img": 'card-3.png',
                            "alt": 'Plan Enterprise FlowMetrics',
                        },
                    ],
                },
                "chapters": [
                    {
                        "title": 'Comparatif',
                        "text": 'Tableau features par plan.',
                        "img": 'scene-1.png',
                        "alt": 'Comparatif FlowMetrics',
                    },
                    {
                        "title": 'FAQ pricing',
                        "text": 'Questions fréquentes sur la facturation.',
                        "img": 'scene-2.png',
                        "alt": 'FAQ FlowMetrics',
                    },
                    {
                        "title": 'ROI',
                        "text": 'Calculateur de retour sur investissement.',
                        "img": 'scene-3.png',
                        "alt": 'ROI FlowMetrics',
                    },
                ],
                "cta": {
                    "text": 'Remise -20% pour les startups Grand Est.',
                    "btn": 'Choisir un plan',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'contact.html',
                "title": 'Contact — FlowMetrics',
                "description": 'Essai gratuit et démo FlowMetrics.',
                "hero": {
                    "h1": 'Démarrer avec FlowMetrics',
                    "lead": 'Formulaire de contact — réponse sous 24 h.',
                    "img": 'hero.png',
                    "alt": 'Contact FlowMetrics',
                },
                "story": ('Nous contacter', ['Support en français, hébergement UE, conformité RGPD.']),
                "cta": {
                    "text": 'Démo — aucune donnée transmise.',
                    "btn": 'Envoyer',
                    "href": '#',
                },
            },
        ],
    },
    {
        "slug": 'saas-onboarding',
        "brand": 'TalentLoop',
        "category": 'saas',
        "layout": 'saas',
        "nav_cta": 'Essai gratuit',
        "synopsis": "Réduisez l'abandon à l'inscription : copy orienté valeur et aha moment visible.",
        "nav": [
            {
                "file": 'index.html',
                "label": 'Accueil',
            },
            {
                "file": 'parcours.html',
                "label": 'Parcours',
            },
            {
                "file": 'fonctionnalites.html',
                "label": 'Fonctionnalités',
            },
            {
                "file": 'contact.html',
                "label": 'Contact',
            },
        ],
        "pages": [
            {
                "file": 'index.html',
                "title": 'TalentLoop — Onboarding RH en 4 étapes avec barre de progression.',
                "description": "Réduisez l'abandon à l'inscription : copy orienté valeur et aha moment visible.",
                "hero": {
                    "h1": 'TalentLoop : Onboarding RH en 4 étapes avec barre de progression.',
                    "lead": "Réduisez l'abandon à l'inscription : copy orienté valeur et aha moment visible.",
                    "img": 'hero.png',
                    "alt": "Interface TalentLoop — écran d'accueil produit",
                },
                "story": ('Le problème que nous résolvons', ['Les équipes produit perdent du temps sur des outils fragmentés et des tableaux Excel obsolètes.', "TalentLoop centralise l'essentiel dans une interface claire, pensée pour le Grand Est et au-delà."]),
                "chapters": [
                    {
                        "title": 'Interface principale',
                        "text": 'Design épuré, hiérarchie visuelle et CTA visibles.',
                        "img": 'scene-1.png',
                        "alt": 'UI TalentLoop — dashboard',
                    },
                    {
                        "title": 'Workflow clé',
                        "text": 'Parcours utilisateur optimisé en trois clics.',
                        "img": 'scene-2.png',
                        "alt": 'Workflow TalentLoop',
                    },
                    {
                        "title": 'Intégrations',
                        "text": 'API REST, webhooks et connecteurs métier.',
                        "img": 'scene-3.png',
                        "alt": 'Intégrations TalentLoop',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Capture produit',
                        "alt": 'Écran TalentLoop',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Vue mobile',
                        "alt": 'App mobile TalentLoop',
                    },
                ],
                "cards": {
                    "title": 'Fonctionnalités clés',
                    "items": [
                        {
                            "title": 'Analytics',
                            "text": 'Tableaux de bord temps réel et exports.',
                            "img": 'card-1.png',
                            "alt": 'Analytics TalentLoop',
                        },
                        {
                            "title": 'Collaboration',
                            "text": 'Équipes synchronisées et commentaires.',
                            "img": 'card-2.png',
                            "alt": 'Collab TalentLoop',
                        },
                        {
                            "title": 'Sécurité',
                            "text": 'RGPD, SSO et chiffrement bout en bout.',
                            "img": 'card-3.png',
                            "alt": 'Sécurité TalentLoop',
                        },
                    ],
                },
                "cta": {
                    "text": "14 jours d'essai gratuit, sans carte bancaire.",
                    "btn": "Démarrer l'essai",
                    "href": 'contact.html',
                },
            },
            {
                "file": 'parcours.html',
                "title": 'Parcours — TalentLoop',
                "description": 'Détail des étapes d onboarding TalentLoop.',
                "hero": {
                    "h1": 'Parcours en 4 étapes',
                    "lead": 'Chaque écran = une intention claire.',
                    "img": 'hero.png',
                    "alt": 'Écran fonctionnalités TalentLoop',
                },
                "story": ("Conçu pour l'adoption", ["Réduction de l'effort cognitif, copy orienté bénéfice et feedback immédiat."]),
                "chapters": [
                    {
                        "title": 'Étape / Module 1',
                        "text": 'Configuration initiale guidée.',
                        "img": 'scene-1.png',
                        "alt": 'Module 1 TalentLoop',
                    },
                    {
                        "title": 'Étape / Module 2',
                        "text": 'Import et synchronisation des données.',
                        "img": 'scene-2.png',
                        "alt": 'Module 2 TalentLoop',
                    },
                    {
                        "title": 'Étape / Module 3',
                        "text": "Premiers insights et partage d'équipe.",
                        "img": 'scene-3.png',
                        "alt": 'Module 3 TalentLoop',
                    },
                ],
                "cards": {
                    "title": 'Avant / Après',
                    "items": [
                        {
                            "title": 'Avant',
                            "text": 'Données éparpillées, décisions lentes.',
                            "img": 'card-1.png',
                            "alt": 'Avant TalentLoop',
                        },
                        {
                            "title": 'Transition',
                            "text": 'Migration assistée en 48 h.',
                            "img": 'card-2.png',
                            "alt": 'Migration TalentLoop',
                        },
                        {
                            "title": 'Après',
                            "text": 'Une source de vérité partagée.',
                            "img": 'card-3.png',
                            "alt": 'Après TalentLoop',
                        },
                    ],
                },
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Détail UI',
                        "alt": 'Composant TalentLoop',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Comparatif',
                        "alt": 'Tableau comparatif',
                    },
                ],
                "cta": {
                    "text": 'Voir une démo personnalisée.',
                    "btn": 'Réserver une démo',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'fonctionnalites.html',
                "title": 'Fonctionnalités — TalentLoop',
                "description": 'Modules TalentLoop.',
                "hero": {
                    "h1": 'Toutes les fonctionnalités',
                    "lead": 'API, webhooks et rôles avancés.',
                    "img": 'hero.png',
                    "alt": 'Page tarifs TalentLoop',
                },
                "cards": {
                    "title": 'Modules',
                    "items": [
                        {
                            "title": 'Starter',
                            "text": "Pour les petites équipes — jusqu'à 5 utilisateurs.",
                            "img": 'card-1.png',
                            "alt": 'Plan Starter TalentLoop',
                        },
                        {
                            "title": 'Pro',
                            "text": 'Le plus populaire — illimité et support prioritaire.',
                            "img": 'card-2.png',
                            "alt": 'Plan Pro TalentLoop',
                        },
                        {
                            "title": 'Enterprise',
                            "text": 'SSO, SLA et account manager dédié.',
                            "img": 'card-3.png',
                            "alt": 'Plan Enterprise TalentLoop',
                        },
                    ],
                },
                "chapters": [
                    {
                        "title": 'Comparatif',
                        "text": 'Tableau features par plan.',
                        "img": 'scene-1.png',
                        "alt": 'Comparatif TalentLoop',
                    },
                    {
                        "title": 'FAQ pricing',
                        "text": 'Questions fréquentes sur la facturation.',
                        "img": 'scene-2.png',
                        "alt": 'FAQ TalentLoop',
                    },
                    {
                        "title": 'ROI',
                        "text": 'Calculateur de retour sur investissement.',
                        "img": 'scene-3.png',
                        "alt": 'ROI TalentLoop',
                    },
                ],
                "cta": {
                    "text": 'Remise -20% pour les startups Grand Est.',
                    "btn": 'Choisir un plan',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'contact.html',
                "title": 'Contact — TalentLoop',
                "description": 'Essai gratuit et démo TalentLoop.',
                "hero": {
                    "h1": 'Démarrer avec TalentLoop',
                    "lead": 'Formulaire de contact — réponse sous 24 h.',
                    "img": 'hero.png',
                    "alt": 'Contact TalentLoop',
                },
                "story": ('Nous contacter', ['Support en français, hébergement UE, conformité RGPD.']),
                "cta": {
                    "text": 'Démo — aucune donnée transmise.',
                    "btn": 'Envoyer',
                    "href": '#',
                },
            },
        ],
    },
    {
        "slug": 'saas-dashboard',
        "brand": 'MetricPulse',
        "category": 'saas',
        "layout": 'saas',
        "nav_cta": 'Essai gratuit',
        "synopsis": "KPIs time-to-value, churn et événements récents en un coup d'œil.",
        "nav": [
            {
                "file": 'index.html',
                "label": 'Accueil',
            },
            {
                "file": 'fonctionnalites.html',
                "label": 'Fonctionnalités',
            },
            {
                "file": 'tarifs.html',
                "label": 'Tarifs',
            },
            {
                "file": 'contact.html',
                "label": 'Contact',
            },
        ],
        "pages": [
            {
                "file": 'index.html',
                "title": 'MetricPulse — Dashboard activation et funnel onboarding.',
                "description": "KPIs time-to-value, churn et événements récents en un coup d'œil.",
                "hero": {
                    "h1": 'MetricPulse : Dashboard activation et funnel onboarding.',
                    "lead": "KPIs time-to-value, churn et événements récents en un coup d'œil.",
                    "img": 'hero.png',
                    "alt": "Interface MetricPulse — écran d'accueil produit",
                },
                "story": ('Le problème que nous résolvons', ['Les équipes produit perdent du temps sur des outils fragmentés et des tableaux Excel obsolètes.', "MetricPulse centralise l'essentiel dans une interface claire, pensée pour le Grand Est et au-delà."]),
                "chapters": [
                    {
                        "title": 'Interface principale',
                        "text": 'Design épuré, hiérarchie visuelle et CTA visibles.',
                        "img": 'scene-1.png',
                        "alt": 'UI MetricPulse — dashboard',
                    },
                    {
                        "title": 'Workflow clé',
                        "text": 'Parcours utilisateur optimisé en trois clics.',
                        "img": 'scene-2.png',
                        "alt": 'Workflow MetricPulse',
                    },
                    {
                        "title": 'Intégrations',
                        "text": 'API REST, webhooks et connecteurs métier.',
                        "img": 'scene-3.png',
                        "alt": 'Intégrations MetricPulse',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Capture produit',
                        "alt": 'Écran MetricPulse',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Vue mobile',
                        "alt": 'App mobile MetricPulse',
                    },
                ],
                "cards": {
                    "title": 'Fonctionnalités clés',
                    "items": [
                        {
                            "title": 'Analytics',
                            "text": 'Tableaux de bord temps réel et exports.',
                            "img": 'card-1.png',
                            "alt": 'Analytics MetricPulse',
                        },
                        {
                            "title": 'Collaboration',
                            "text": 'Équipes synchronisées et commentaires.',
                            "img": 'card-2.png',
                            "alt": 'Collab MetricPulse',
                        },
                        {
                            "title": 'Sécurité',
                            "text": 'RGPD, SSO et chiffrement bout en bout.',
                            "img": 'card-3.png',
                            "alt": 'Sécurité MetricPulse',
                        },
                    ],
                },
                "cta": {
                    "text": "14 jours d'essai gratuit, sans carte bancaire.",
                    "btn": "Démarrer l'essai",
                    "href": 'contact.html',
                },
            },
            {
                "file": 'fonctionnalites.html',
                "title": 'Fonctionnalités — MetricPulse',
                "description": 'Détail des fonctionnalités MetricPulse.',
                "hero": {
                    "h1": 'Fonctionnalités',
                    "lead": 'Tout ce dont votre équipe a besoin.',
                    "img": 'hero.png',
                    "alt": 'Écran fonctionnalités MetricPulse',
                },
                "story": ("Conçu pour l'adoption", ["Réduction de l'effort cognitif, copy orienté bénéfice et feedback immédiat."]),
                "chapters": [
                    {
                        "title": 'Étape / Module 1',
                        "text": 'Configuration initiale guidée.',
                        "img": 'scene-1.png',
                        "alt": 'Module 1 MetricPulse',
                    },
                    {
                        "title": 'Étape / Module 2',
                        "text": 'Import et synchronisation des données.',
                        "img": 'scene-2.png',
                        "alt": 'Module 2 MetricPulse',
                    },
                    {
                        "title": 'Étape / Module 3',
                        "text": "Premiers insights et partage d'équipe.",
                        "img": 'scene-3.png',
                        "alt": 'Module 3 MetricPulse',
                    },
                ],
                "cards": {
                    "title": 'Avant / Après',
                    "items": [
                        {
                            "title": 'Avant',
                            "text": 'Données éparpillées, décisions lentes.',
                            "img": 'card-1.png',
                            "alt": 'Avant MetricPulse',
                        },
                        {
                            "title": 'Transition',
                            "text": 'Migration assistée en 48 h.',
                            "img": 'card-2.png',
                            "alt": 'Migration MetricPulse',
                        },
                        {
                            "title": 'Après',
                            "text": 'Une source de vérité partagée.',
                            "img": 'card-3.png',
                            "alt": 'Après MetricPulse',
                        },
                    ],
                },
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Détail UI',
                        "alt": 'Composant MetricPulse',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Comparatif',
                        "alt": 'Tableau comparatif',
                    },
                ],
                "cta": {
                    "text": 'Voir une démo personnalisée.',
                    "btn": 'Réserver une démo',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'tarifs.html',
                "title": 'Tarifs — MetricPulse',
                "description": 'Grille tarifaire MetricPulse.',
                "hero": {
                    "h1": 'Tarifs transparents',
                    "lead": 'Plan recommandé mis en avant, sans frais cachés.',
                    "img": 'hero.png',
                    "alt": 'Page tarifs MetricPulse',
                },
                "cards": {
                    "title": 'Nos offres',
                    "items": [
                        {
                            "title": 'Starter',
                            "text": "Pour les petites équipes — jusqu'à 5 utilisateurs.",
                            "img": 'card-1.png',
                            "alt": 'Plan Starter MetricPulse',
                        },
                        {
                            "title": 'Pro',
                            "text": 'Le plus populaire — illimité et support prioritaire.',
                            "img": 'card-2.png',
                            "alt": 'Plan Pro MetricPulse',
                        },
                        {
                            "title": 'Enterprise',
                            "text": 'SSO, SLA et account manager dédié.',
                            "img": 'card-3.png',
                            "alt": 'Plan Enterprise MetricPulse',
                        },
                    ],
                },
                "chapters": [
                    {
                        "title": 'Comparatif',
                        "text": 'Tableau features par plan.',
                        "img": 'scene-1.png',
                        "alt": 'Comparatif MetricPulse',
                    },
                    {
                        "title": 'FAQ pricing',
                        "text": 'Questions fréquentes sur la facturation.',
                        "img": 'scene-2.png',
                        "alt": 'FAQ MetricPulse',
                    },
                    {
                        "title": 'ROI',
                        "text": 'Calculateur de retour sur investissement.',
                        "img": 'scene-3.png',
                        "alt": 'ROI MetricPulse',
                    },
                ],
                "cta": {
                    "text": 'Remise -20% pour les startups Grand Est.',
                    "btn": 'Choisir un plan',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'contact.html',
                "title": 'Contact — MetricPulse',
                "description": 'Essai gratuit et démo MetricPulse.',
                "hero": {
                    "h1": 'Démarrer avec MetricPulse',
                    "lead": 'Formulaire de contact — réponse sous 24 h.',
                    "img": 'hero.png',
                    "alt": 'Contact MetricPulse',
                },
                "story": ('Nous contacter', ['Support en français, hébergement UE, conformité RGPD.']),
                "cta": {
                    "text": 'Démo — aucune donnée transmise.',
                    "btn": 'Envoyer',
                    "href": '#',
                },
            },
        ],
    },
    {
        "slug": 'saas-empty',
        "brand": 'QueryBase',
        "category": 'saas',
        "layout": 'saas',
        "nav_cta": 'Essai gratuit',
        "synopsis": "Suggestions, vote roadmap et correcteur d'intention — zéro impasse utilisateur.",
        "nav": [
            {
                "file": 'index.html',
                "label": 'Accueil',
            },
            {
                "file": 'fonctionnalites.html',
                "label": 'Fonctionnalités',
            },
            {
                "file": 'tarifs.html',
                "label": 'Tarifs',
            },
            {
                "file": 'contact.html',
                "label": 'Contact',
            },
        ],
        "pages": [
            {
                "file": 'index.html',
                "title": 'QueryBase — États vides et recherche sans résultat orientés action.',
                "description": "Suggestions, vote roadmap et correcteur d'intention — zéro impasse utilisateur.",
                "hero": {
                    "h1": 'QueryBase : États vides et recherche sans résultat orientés action.',
                    "lead": "Suggestions, vote roadmap et correcteur d'intention — zéro impasse utilisateur.",
                    "img": 'hero.png',
                    "alt": "Interface QueryBase — écran d'accueil produit",
                },
                "story": ('Le problème que nous résolvons', ['Les équipes produit perdent du temps sur des outils fragmentés et des tableaux Excel obsolètes.', "QueryBase centralise l'essentiel dans une interface claire, pensée pour le Grand Est et au-delà."]),
                "chapters": [
                    {
                        "title": 'Interface principale',
                        "text": 'Design épuré, hiérarchie visuelle et CTA visibles.',
                        "img": 'scene-1.png',
                        "alt": 'UI QueryBase — dashboard',
                    },
                    {
                        "title": 'Workflow clé',
                        "text": 'Parcours utilisateur optimisé en trois clics.',
                        "img": 'scene-2.png',
                        "alt": 'Workflow QueryBase',
                    },
                    {
                        "title": 'Intégrations',
                        "text": 'API REST, webhooks et connecteurs métier.',
                        "img": 'scene-3.png',
                        "alt": 'Intégrations QueryBase',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Capture produit',
                        "alt": 'Écran QueryBase',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Vue mobile',
                        "alt": 'App mobile QueryBase',
                    },
                ],
                "cards": {
                    "title": 'Fonctionnalités clés',
                    "items": [
                        {
                            "title": 'Analytics',
                            "text": 'Tableaux de bord temps réel et exports.',
                            "img": 'card-1.png',
                            "alt": 'Analytics QueryBase',
                        },
                        {
                            "title": 'Collaboration',
                            "text": 'Équipes synchronisées et commentaires.',
                            "img": 'card-2.png',
                            "alt": 'Collab QueryBase',
                        },
                        {
                            "title": 'Sécurité',
                            "text": 'RGPD, SSO et chiffrement bout en bout.',
                            "img": 'card-3.png',
                            "alt": 'Sécurité QueryBase',
                        },
                    ],
                },
                "cta": {
                    "text": "14 jours d'essai gratuit, sans carte bancaire.",
                    "btn": "Démarrer l'essai",
                    "href": 'contact.html',
                },
            },
            {
                "file": 'fonctionnalites.html',
                "title": 'Fonctionnalités — QueryBase',
                "description": 'Détail des fonctionnalités QueryBase.',
                "hero": {
                    "h1": 'Fonctionnalités',
                    "lead": 'Tout ce dont votre équipe a besoin.',
                    "img": 'hero.png',
                    "alt": 'Écran fonctionnalités QueryBase',
                },
                "story": ("Conçu pour l'adoption", ["Réduction de l'effort cognitif, copy orienté bénéfice et feedback immédiat."]),
                "chapters": [
                    {
                        "title": 'Étape / Module 1',
                        "text": 'Configuration initiale guidée.',
                        "img": 'scene-1.png',
                        "alt": 'Module 1 QueryBase',
                    },
                    {
                        "title": 'Étape / Module 2',
                        "text": 'Import et synchronisation des données.',
                        "img": 'scene-2.png',
                        "alt": 'Module 2 QueryBase',
                    },
                    {
                        "title": 'Étape / Module 3',
                        "text": "Premiers insights et partage d'équipe.",
                        "img": 'scene-3.png',
                        "alt": 'Module 3 QueryBase',
                    },
                ],
                "cards": {
                    "title": 'Avant / Après',
                    "items": [
                        {
                            "title": 'Avant',
                            "text": 'Données éparpillées, décisions lentes.',
                            "img": 'card-1.png',
                            "alt": 'Avant QueryBase',
                        },
                        {
                            "title": 'Transition',
                            "text": 'Migration assistée en 48 h.',
                            "img": 'card-2.png',
                            "alt": 'Migration QueryBase',
                        },
                        {
                            "title": 'Après',
                            "text": 'Une source de vérité partagée.',
                            "img": 'card-3.png',
                            "alt": 'Après QueryBase',
                        },
                    ],
                },
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Détail UI',
                        "alt": 'Composant QueryBase',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Comparatif',
                        "alt": 'Tableau comparatif',
                    },
                ],
                "cta": {
                    "text": 'Voir une démo personnalisée.',
                    "btn": 'Réserver une démo',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'tarifs.html',
                "title": 'Tarifs — QueryBase',
                "description": 'Grille tarifaire QueryBase.',
                "hero": {
                    "h1": 'Tarifs transparents',
                    "lead": 'Plan recommandé mis en avant, sans frais cachés.',
                    "img": 'hero.png',
                    "alt": 'Page tarifs QueryBase',
                },
                "cards": {
                    "title": 'Nos offres',
                    "items": [
                        {
                            "title": 'Starter',
                            "text": "Pour les petites équipes — jusqu'à 5 utilisateurs.",
                            "img": 'card-1.png',
                            "alt": 'Plan Starter QueryBase',
                        },
                        {
                            "title": 'Pro',
                            "text": 'Le plus populaire — illimité et support prioritaire.',
                            "img": 'card-2.png',
                            "alt": 'Plan Pro QueryBase',
                        },
                        {
                            "title": 'Enterprise',
                            "text": 'SSO, SLA et account manager dédié.',
                            "img": 'card-3.png',
                            "alt": 'Plan Enterprise QueryBase',
                        },
                    ],
                },
                "chapters": [
                    {
                        "title": 'Comparatif',
                        "text": 'Tableau features par plan.',
                        "img": 'scene-1.png',
                        "alt": 'Comparatif QueryBase',
                    },
                    {
                        "title": 'FAQ pricing',
                        "text": 'Questions fréquentes sur la facturation.',
                        "img": 'scene-2.png',
                        "alt": 'FAQ QueryBase',
                    },
                    {
                        "title": 'ROI',
                        "text": 'Calculateur de retour sur investissement.',
                        "img": 'scene-3.png',
                        "alt": 'ROI QueryBase',
                    },
                ],
                "cta": {
                    "text": 'Remise -20% pour les startups Grand Est.',
                    "btn": 'Choisir un plan',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'contact.html',
                "title": 'Contact — QueryBase',
                "description": 'Essai gratuit et démo QueryBase.',
                "hero": {
                    "h1": 'Démarrer avec QueryBase',
                    "lead": 'Formulaire de contact — réponse sous 24 h.',
                    "img": 'hero.png',
                    "alt": 'Contact QueryBase',
                },
                "story": ('Nous contacter', ['Support en français, hébergement UE, conformité RGPD.']),
                "cta": {
                    "text": 'Démo — aucune donnée transmise.',
                    "btn": 'Envoyer',
                    "href": '#',
                },
            },
        ],
    },
    {
        "slug": 'saas-notifications',
        "brand": 'PingFlow',
        "category": 'saas',
        "layout": 'saas',
        "nav_cta": 'Essai gratuit',
        "synopsis": 'Actions requises, filtres granulaires et préférences anti-spam.',
        "nav": [
            {
                "file": 'index.html',
                "label": 'Accueil',
            },
            {
                "file": 'fonctionnalites.html',
                "label": 'Fonctionnalités',
            },
            {
                "file": 'tarifs.html',
                "label": 'Tarifs',
            },
            {
                "file": 'contact.html',
                "label": 'Contact',
            },
        ],
        "pages": [
            {
                "file": 'index.html',
                "title": 'PingFlow — Centre de notifications in-app hiérarchisé.',
                "description": 'Actions requises, filtres granulaires et préférences anti-spam.',
                "hero": {
                    "h1": 'PingFlow : Centre de notifications in-app hiérarchisé.',
                    "lead": 'Actions requises, filtres granulaires et préférences anti-spam.',
                    "img": 'hero.png',
                    "alt": "Interface PingFlow — écran d'accueil produit",
                },
                "story": ('Le problème que nous résolvons', ['Les équipes produit perdent du temps sur des outils fragmentés et des tableaux Excel obsolètes.', "PingFlow centralise l'essentiel dans une interface claire, pensée pour le Grand Est et au-delà."]),
                "chapters": [
                    {
                        "title": 'Interface principale',
                        "text": 'Design épuré, hiérarchie visuelle et CTA visibles.',
                        "img": 'scene-1.png',
                        "alt": 'UI PingFlow — dashboard',
                    },
                    {
                        "title": 'Workflow clé',
                        "text": 'Parcours utilisateur optimisé en trois clics.',
                        "img": 'scene-2.png',
                        "alt": 'Workflow PingFlow',
                    },
                    {
                        "title": 'Intégrations',
                        "text": 'API REST, webhooks et connecteurs métier.',
                        "img": 'scene-3.png',
                        "alt": 'Intégrations PingFlow',
                    },
                ],
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Capture produit',
                        "alt": 'Écran PingFlow',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Vue mobile',
                        "alt": 'App mobile PingFlow',
                    },
                ],
                "cards": {
                    "title": 'Fonctionnalités clés',
                    "items": [
                        {
                            "title": 'Analytics',
                            "text": 'Tableaux de bord temps réel et exports.',
                            "img": 'card-1.png',
                            "alt": 'Analytics PingFlow',
                        },
                        {
                            "title": 'Collaboration',
                            "text": 'Équipes synchronisées et commentaires.',
                            "img": 'card-2.png',
                            "alt": 'Collab PingFlow',
                        },
                        {
                            "title": 'Sécurité',
                            "text": 'RGPD, SSO et chiffrement bout en bout.',
                            "img": 'card-3.png',
                            "alt": 'Sécurité PingFlow',
                        },
                    ],
                },
                "cta": {
                    "text": "14 jours d'essai gratuit, sans carte bancaire.",
                    "btn": "Démarrer l'essai",
                    "href": 'contact.html',
                },
            },
            {
                "file": 'fonctionnalites.html',
                "title": 'Fonctionnalités — PingFlow',
                "description": 'Détail des fonctionnalités PingFlow.',
                "hero": {
                    "h1": 'Fonctionnalités',
                    "lead": 'Tout ce dont votre équipe a besoin.',
                    "img": 'hero.png',
                    "alt": 'Écran fonctionnalités PingFlow',
                },
                "story": ("Conçu pour l'adoption", ["Réduction de l'effort cognitif, copy orienté bénéfice et feedback immédiat."]),
                "chapters": [
                    {
                        "title": 'Étape / Module 1',
                        "text": 'Configuration initiale guidée.',
                        "img": 'scene-1.png',
                        "alt": 'Module 1 PingFlow',
                    },
                    {
                        "title": 'Étape / Module 2',
                        "text": 'Import et synchronisation des données.',
                        "img": 'scene-2.png',
                        "alt": 'Module 2 PingFlow',
                    },
                    {
                        "title": 'Étape / Module 3',
                        "text": "Premiers insights et partage d'équipe.",
                        "img": 'scene-3.png',
                        "alt": 'Module 3 PingFlow',
                    },
                ],
                "cards": {
                    "title": 'Avant / Après',
                    "items": [
                        {
                            "title": 'Avant',
                            "text": 'Données éparpillées, décisions lentes.',
                            "img": 'card-1.png',
                            "alt": 'Avant PingFlow',
                        },
                        {
                            "title": 'Transition',
                            "text": 'Migration assistée en 48 h.',
                            "img": 'card-2.png',
                            "alt": 'Migration PingFlow',
                        },
                        {
                            "title": 'Après',
                            "text": 'Une source de vérité partagée.',
                            "img": 'card-3.png',
                            "alt": 'Après PingFlow',
                        },
                    ],
                },
                "gallery": [
                    {
                        "img": 'gallery-1.png',
                        "caption": 'Détail UI',
                        "alt": 'Composant PingFlow',
                    },
                    {
                        "img": 'gallery-2.png',
                        "caption": 'Comparatif',
                        "alt": 'Tableau comparatif',
                    },
                ],
                "cta": {
                    "text": 'Voir une démo personnalisée.',
                    "btn": 'Réserver une démo',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'tarifs.html',
                "title": 'Tarifs — PingFlow',
                "description": 'Grille tarifaire PingFlow.',
                "hero": {
                    "h1": 'Tarifs transparents',
                    "lead": 'Plan recommandé mis en avant, sans frais cachés.',
                    "img": 'hero.png',
                    "alt": 'Page tarifs PingFlow',
                },
                "cards": {
                    "title": 'Nos offres',
                    "items": [
                        {
                            "title": 'Starter',
                            "text": "Pour les petites équipes — jusqu'à 5 utilisateurs.",
                            "img": 'card-1.png',
                            "alt": 'Plan Starter PingFlow',
                        },
                        {
                            "title": 'Pro',
                            "text": 'Le plus populaire — illimité et support prioritaire.',
                            "img": 'card-2.png',
                            "alt": 'Plan Pro PingFlow',
                        },
                        {
                            "title": 'Enterprise',
                            "text": 'SSO, SLA et account manager dédié.',
                            "img": 'card-3.png',
                            "alt": 'Plan Enterprise PingFlow',
                        },
                    ],
                },
                "chapters": [
                    {
                        "title": 'Comparatif',
                        "text": 'Tableau features par plan.',
                        "img": 'scene-1.png',
                        "alt": 'Comparatif PingFlow',
                    },
                    {
                        "title": 'FAQ pricing',
                        "text": 'Questions fréquentes sur la facturation.',
                        "img": 'scene-2.png',
                        "alt": 'FAQ PingFlow',
                    },
                    {
                        "title": 'ROI',
                        "text": 'Calculateur de retour sur investissement.',
                        "img": 'scene-3.png',
                        "alt": 'ROI PingFlow',
                    },
                ],
                "cta": {
                    "text": 'Remise -20% pour les startups Grand Est.',
                    "btn": 'Choisir un plan',
                    "href": 'contact.html',
                },
            },
            {
                "file": 'contact.html',
                "title": 'Contact — PingFlow',
                "description": 'Essai gratuit et démo PingFlow.',
                "hero": {
                    "h1": 'Démarrer avec PingFlow',
                    "lead": 'Formulaire de contact — réponse sous 24 h.',
                    "img": 'hero.png',
                    "alt": 'Contact PingFlow',
                },
                "story": ('Nous contacter', ['Support en français, hébergement UE, conformité RGPD.']),
                "cta": {
                    "text": 'Démo — aucune donnée transmise.',
                    "btn": 'Envoyer',
                    "href": '#',
                },
            },
        ],
    },
]


def _scene_type(filename: str, default: str) -> str:
    if filename == "hero.png":
        return "hero"
    if filename.startswith("card-"):
        return "card"
    if filename.startswith("gallery-"):
        return "gallery"
    if filename.startswith("scene-"):
        return default
    return default


def _collect_images(sc: dict) -> list[tuple[str, str, str]]:
    """Retourne (filename, label, scene_type) en fusionnant tous les contextes multi-pages."""
    default = SCENE_TYPE_BY_SLUG.get(sc["slug"], "interior")
    acc: dict[str, list[str]] = {}

    def note(filename: str, *texts: str) -> None:
        if not filename:
            return
        bucket = acc.setdefault(filename, [])
        for text in texts:
            t = (text or "").strip()
            if t and t not in bucket:
                bucket.append(t)

    for page in sc.get("pages", []):
        hero = page.get("hero")
        if hero and hero.get("img"):
            note(hero["img"], hero.get("alt"), hero.get("h1"), hero.get("lead"))
        for ch in page.get("chapters") or []:
            note(ch.get("img", ""), ch.get("alt"), ch.get("title"), ch.get("text"))
        for g in page.get("gallery") or []:
            note(g.get("img", ""), g.get("alt"), g.get("caption"))
        cards = page.get("cards")
        if cards:
            for item in cards.get("items") or []:
                note(item.get("img", ""), item.get("alt"), item.get("title"), item.get("text"))

    out: list[tuple[str, str, str]] = []
    for filename, parts in acc.items():
        out.append((filename, ". ".join(parts), _scene_type(filename, default)))
    return out


def image_specs() -> list[tuple[str, str, str, str, str]]:
    """(slug, filename, label, scene_type, category) pour génération d images."""
    specs: list[tuple[str, str, str, str, str]] = []
    global_seen: set[tuple[str, str]] = set()
    for sc in SCENARIOS:
        slug = sc["slug"]
        category = sc["category"]
        for filename, label, scene_type in _collect_images(sc):
            key = (slug, filename)
            if key in global_seen:
                continue
            global_seen.add(key)
            specs.append((slug, filename, label, scene_type, category))
    return specs
