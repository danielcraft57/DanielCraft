/* ========================================
   GITHUB PROJECTS DATA - Tous les repositories
   ======================================== */

const GitHubProjects = {
    projects: [
        // @loupix - Projets 2025
        {
            id: 'dispy-cluster',
            title: 'DispyCluster',
            description: 'Système de clustering distribué pour le traitement de données.',
            category: 'tools',
            featured: true,
            technologies: ['Python'],
            year: 2025,
            lastUpdate: 'Novembre 2025',
            account: 'loupix',
            status: 'active',
            imageUrl: 'assets/images/projets/DispyCluster.jpg'
        },
        {
            id: 'duel-de-dame-loupix',
            title: 'DuelDeDame',
            description: 'Jeu de dame développé avec des patterns designs. Pour l\'apprentissage.',
            category: 'web',
            featured: true,
            technologies: ['TypeScript'],
            year: 2025,
            lastUpdate: 'Septembre 2025',
            account: 'loupix',
            status: 'active',
            licence: 'MIT',
            imageUrl: 'assets/images/projets/DuelDeDame.jpg'
        },
        {
            id: 'crypto-spread-edge',
            title: 'CryptoSpreadEdge',
            description: 'Système de trading crypto haute fréquence avec IA et déploiement Docker Swarm.',
            category: 'specialized',
            featured: true,
            technologies: ['Python', 'IA', 'Docker Swarm'],
            year: 2025,
            lastUpdate: 'Septembre 2025',
            account: 'loupix',
            status: 'active',
            imageUrl: 'assets/images/projets/CryptoSpreadEdge.jpg'
        },
        {
            id: 'ticket-caisse',
            title: 'TicketCaisse',
            description: 'Application mobile de gestion de caisse et tickets.',
            category: 'mobile',
            featured: true,
            technologies: ['Dart', 'Flutter'],
            year: 2025,
            lastUpdate: 'Septembre 2025',
            account: 'loupix',
            status: 'active',
            imageUrl: 'assets/images/projets/TicketCaisse.jpg'
        },
        {
            id: 'intelli-reply',
            title: 'IntelliReply',
            description: 'Système intelligent de réponse automatique.',
            category: 'tools',
            featured: false,
            technologies: ['Python', 'IA'],
            year: 2025,
            lastUpdate: 'Septembre 2025',
            account: 'loupix',
            status: 'active',
            imageUrl: 'assets/images/projets/IntelliReply.jpg'
        },
        {
            id: 'torrent-sphere-app',
            title: 'TorrentSphere App',
            description: 'Application de téléchargement de torrents.',
            category: 'tools',
            featured: false,
            technologies: [],
            year: 2025,
            lastUpdate: 'Septembre 2025',
            account: 'loupix',
            status: 'active'
        },
        {
            id: 'torrent-sphere-platform',
            title: 'TorrentSphere Platform',
            description: 'Plateforme de téléchargement de torrents avec scraping automatique.',
            category: 'specialized',
            featured: false,
            technologies: [],
            year: 2025,
            lastUpdate: 'Septembre 2025',
            account: 'loupix',
            status: 'active'
        },
        {
            id: 'call-attendant',
            title: 'Call Attendant',
            description: 'Système automatisé de réception d\'appels, blocage et messagerie vocale fonctionnant sur Raspberry Pi.',
            category: 'iot',
            featured: true,
            technologies: ['Python', 'Raspberry Pi'],
            year: 2025,
            lastUpdate: 'Août 2025',
            account: 'loupix',
            status: 'active',
            licence: 'MIT',
            isFork: true,
            imageUrl: 'assets/images/projets/CallAttendant.jpg'
        },
        
        // @loupix57 - Depots GitHub (clone script + integration V6)
        { id: 'callattendant-l57', title: 'CallAttendant', description: 'Repondeur et blocage d\'appels sur Raspberry Pi (modem USR 5637). Python.', category: 'iot', featured: true, technologies: ['Python', 'Raspberry Pi'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', licence: 'MIT', imageUrl: 'assets/images/projets/CallAttendant.jpg' },
        { id: 'clientcrm-l57', title: 'ClientCRM', description: 'CRM simple pour PME : contacts, opportunites, suivi. Next.js React TypeScript.', category: 'web', featured: true, technologies: ['Next.js', 'React', 'TypeScript'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/ClientCRM.jpg' },
        { id: 'clipforge-l57', title: 'ClipForge', description: 'Creation de shorts viraux en local : ingest, STT, TTS, montage, TikTok. API NestJS, workers Python, dashboard Next.js.', category: 'specialized', featured: true, technologies: ['NestJS', 'Python', 'Next.js'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/ClipForge.jpg' },
        { id: 'cryptocluster-l57', title: 'CryptoCluster', description: 'Plateforme distribuee de collecte et d\'analyse de donnees crypto : RedisTimeSeries, InfluxDB, Dispy, CCXT. API FastAPI, web et mobile.', category: 'specialized', featured: true, technologies: ['Python', 'FastAPI', 'Redis', 'InfluxDB'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/CryptoCluster.jpg' },
        { id: 'cryptospreadedge-l57', title: 'CryptoSpreadEdge', description: 'Trading crypto haute frequence avec IA. Docker Swarm, multi-plateformes, FastAPI Python.', category: 'specialized', featured: true, technologies: ['Python', 'FastAPI', 'Docker Swarm', 'IA'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/CryptoSpreadEdge.jpg' },
        { id: 'cvletterassistant-l57', title: 'CvLetterAssistant', description: 'Demo lettre de motivation et tips CV avec LLM local (Ollama). Express.', category: 'tools', featured: true, technologies: ['Node.js', 'Express', 'Ollama', 'LLM'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/CvLetterAssistant.jpg' },
        { id: 'datawhisper-l57', title: 'DataWhisper', description: 'Plateforme OSINT centralisee : collecte, analyse et visualisation de donnees multi-sources. FastAPI, React, Docker.', category: 'specialized', featured: true, technologies: ['Python', 'FastAPI', 'React', 'Docker'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/DataWhisper.jpg' },
        { id: 'deliverytrack-l57', title: 'DeliveryTrack', description: 'Suivi de livraisons pour PME logistique : tableau de bord, colis, chauffeurs. Next.js TypeScript.', category: 'web', featured: true, technologies: ['Next.js', 'TypeScript'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/DeliveryTrack.jpg' },
        { id: 'design-patterns-l57', title: 'Design-Patterns', description: 'Exemples de design patterns en Java, Go, Python, TypeScript, PHP, C#, Ruby, C++.', category: 'learning', featured: false, technologies: ['Java', 'Go', 'Python', 'TypeScript', 'PHP'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/Design-Patterns.jpg' },
        { id: 'dispycluster-l57', title: 'DispyCluster', description: 'Cluster de calcul distribue Raspberry Pi : scraping, monitoring, API, Dispy.', category: 'tools', featured: true, technologies: ['Python', 'Raspberry Pi', 'Dispy'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/DispyCluster.jpg' },
        { id: 'distributionjournaux-l57', title: 'DistributionJournaux', description: 'Application distribution de journaux. Node.js MongoDB, zones et seed.', category: 'web', featured: false, technologies: ['Node.js', 'MongoDB'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/DistributionJournaux.jpg' },
        { id: 'dueldedame-l57', title: 'DuelDeDame', description: 'Jeu de dames en ligne temps reel. Next.js et NestJS, design patterns (Strategy, Factory).', category: 'web', featured: true, technologies: ['Next.js', 'NestJS', 'TypeScript'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/DuelDeDame.jpg' },
        { id: 'dueldedame-legacy-l57', title: 'DuelDeDame-Legacy', description: 'Version initiale du jeu de dames (loupix) - code source historique.', category: 'web', featured: false, technologies: ['TypeScript'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/DuelDeDame-Legacy.jpg' },
        { id: 'ecodatahub-l57', title: 'EcoDataHub', description: 'Plateforme multi-sources pour donnees economiques (Eurostat, INSEE, BdF, OCDE, Banque mondiale). FastAPI, ML, econometrie, rapports LLM.', category: 'specialized', featured: true, technologies: ['Python', 'FastAPI', 'ML', 'LLM'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/EcoDataHub.jpg' },
        { id: 'educonnect-l57', title: 'EduConnect', description: 'Plateforme educative simple pour enseignants. Next.js React TypeScript Tailwind.', category: 'web', featured: true, technologies: ['Next.js', 'React', 'TypeScript', 'Tailwind'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/EduConnect.jpg' },
        { id: 'gestionnaireevenements-l57', title: 'GestionnaireEvenements', description: 'Gestionnaire d\'evenements. PHP, Bower, interface de gestion.', category: 'web', featured: false, technologies: ['PHP'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/GestionnaireEvenements.jpg' },
        { id: 'intellireply-l57', title: 'IntelliReply', description: 'Repondeur intelligent modem 56K. Flask, filtrage, messages, pilote USR5637.', category: 'iot', featured: false, technologies: ['Python', 'Flask'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/IntelliReply.jpg' },
        { id: 'jobhunter-l57', title: 'JobHunter', description: 'Scraping intelligent d\'offres d\'emploi et interim (Indeed, HelloWork, LinkedIn, France Travail, Actual). FastAPI, Celery, Raspberry Pi.', category: 'tools', featured: true, technologies: ['Python', 'FastAPI', 'Celery'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/JobHunter.jpg' },
        { id: 'journauxgestion-l57', title: 'JournauxGestion', description: 'Gestion donnees journaux. Backend Django Python, frontend Angular 12, mobile Flutter.', category: 'web', featured: false, technologies: ['Python', 'Django', 'Angular', 'Flutter'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/JournauxGestion.jpg' },
        { id: 'latelierdusavoir-l57', title: 'LAtelierDuSavoir', description: 'Echange et vente de cours, formations et tests en ligne. Plateforme educative.', category: 'web', featured: true, technologies: ['JavaScript'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/LAtelierDuSavoir.jpg' },
        { id: 'nftcrypto-l57', title: 'NftCrypto', description: 'Recherche sur contrats virtuels et NFT. Exploration crypto.', category: 'specialized', featured: true, technologies: ['TypeScript', 'Blockchain', 'NFT'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/NftCrypto.jpg' },
        { id: 'photosshare-l57', title: 'PhotosShare', description: 'Partage de photos privees. Albums ou selection. React.js.', category: 'web', featured: false, technologies: ['React', 'JavaScript'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/PhotosShare.jpg' },
        { id: 'quickbill-l57', title: 'QuickBill', description: 'SaaS gestion factures freelances : scan OCR Tesseract, dashboard, Prisma SQLite, Next.js.', category: 'web', featured: true, technologies: ['Next.js', 'Prisma', 'OCR'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/QuickBill.jpg' },
        { id: 'restaurationrapide-l57', title: 'RestaurationRapide', description: 'Plateforme restauration entierement configurable NoCode. Node.js MongoDB.', category: 'web', featured: true, technologies: ['Node.js', 'MongoDB'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/RestaurationRapide.jpg' },
        { id: 'scalpel-numerique-l57', title: 'scalpel-numerique', description: 'Pipeline visage MediaPipe et apps Kivy. Extraction, morphologie, rendu video. Simulation chirurgie esthetique.', category: 'specialized', featured: true, technologies: ['Python', 'MediaPipe', 'Kivy'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/scalpel-numerique.jpg' },
        { id: 'socialcare-hub-l57', title: 'SocialCare-Hub', description: 'Plateforme SaaS travail social. Microservices, digitalisation, React TypeScript, API Gateway.', category: 'web', featured: true, technologies: ['React', 'TypeScript'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/SocialCare-Hub.jpg' },
        { id: 'taptapcar-l57', title: 'TapTapCar', description: 'Logiciel de covoiturage. PHP Twig.', category: 'web', featured: false, technologies: ['PHP'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/TapTapCar.jpg' },
        { id: 'ticketcaisse-l57', title: 'TicketCaisse', description: 'App Flutter : scan tickets de caisse, OCR multi-moteurs, categorisation, export CSV/PDF.', category: 'mobile', featured: true, technologies: ['Dart', 'Flutter', 'OCR'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/TicketCaisse.jpg' },
        { id: 'turfrace-l57', title: 'turfrace', description: 'Analyse et prediction des courses hippiques. Collecte multi-sources, stats, modeles ML, API FastAPI.', category: 'specialized', featured: true, technologies: ['Python', 'FastAPI', 'ML'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/turfrace.jpg' },
        { id: 'youtubedownloader-l57', title: 'YoutubeDownloader', description: 'Plateforme telechargement videos YouTube, Dailymotion. Python AngularJS.', category: 'tools', featured: false, technologies: ['Python', 'AngularJS'], year: 2026, lastUpdate: 'Fevrier 2026', account: 'loupix57', status: 'active', imageUrl: 'assets/images/projets/YoutubeDownloader.jpg' },
        
        // @loupix - Projets 2024
        {
            id: 'journaux-gestion',
            title: 'Journaux Gestion',
            description: 'Système de gestion de journaux.',
            category: 'web',
            featured: false,
            technologies: [],
            year: 2024,
            lastUpdate: 'Avril 2024',
            account: 'loupix',
            status: 'archived'
        },
        {
            id: 'nft-et-crypto',
            title: 'NFT & Crypto',
            description: 'Recherche en Contrat virtuel / NFT.',
            category: 'specialized',
            featured: true,
            technologies: ['TypeScript', 'Blockchain', 'NFT'],
            year: 2024,
            lastUpdate: 'Avril 2024',
            account: 'loupix',
            status: 'archived'
        },
        {
            id: 'design-patterns',
            title: 'Design Patterns',
            description: 'Implémentation de patterns de conception en PHP.',
            category: 'learning',
            featured: false,
            technologies: ['PHP'],
            year: 2024,
            lastUpdate: 'Avril 2024',
            account: 'loupix',
            status: 'archived'
        },
        {
            id: 'restauration',
            title: 'Plateforme de Restauration',
            description: 'Plateforme de restauration entièrement configurable / NoCode.',
            category: 'web',
            featured: true,
            technologies: ['JavaScript'],
            year: 2024,
            lastUpdate: 'Avril 2024',
            account: 'loupix',
            status: 'archived'
        },
        {
            id: 'photos-share',
            title: 'Partage de Photos',
            description: 'Partage de photos développé en ReactJs.',
            category: 'web',
            featured: true,
            technologies: ['JavaScript', 'React'],
            year: 2024,
            lastUpdate: 'Avril 2024',
            account: 'loupix',
            status: 'archived'
        },
        {
            id: 'youtube-downloader',
            title: 'YouTube Downloader',
            description: 'Plateforme de téléchargement de vidéo.',
            category: 'tools',
            featured: false,
            technologies: ['Python'],
            year: 2024,
            lastUpdate: 'Avril 2024',
            account: 'loupix',
            status: 'archived'
        },
        {
            id: 'taptapcar',
            title: 'TapTapCar',
            description: 'Logiciel de covoiturage.',
            category: 'web',
            featured: false,
            technologies: ['PHP'],
            year: 2024,
            lastUpdate: 'Avril 2024',
            account: 'loupix',
            status: 'archived'
        },
        {
            id: 'distribution-journaux',
            title: 'Distribution de Journaux',
            description: 'Distribution de journaux dans le grand duché.',
            category: 'web',
            featured: false,
            technologies: ['JavaScript'],
            year: 2024,
            lastUpdate: 'Avril 2024',
            account: 'loupix',
            status: 'archived'
        },
        {
            id: 'gestionnaire-evenements',
            title: 'Gestionnaire d\'Événements',
            description: 'Gestionnaire d\'événement.',
            category: 'web',
            featured: false,
            technologies: ['PHP'],
            year: 2024,
            lastUpdate: 'Avril 2024',
            account: 'loupix',
            status: 'archived'
        },
        
        // @likedevGit - Tous 2025
        {
            id: 'edu-connect',
            title: 'EduConnect',
            description: 'Plateforme éducative moderne pour enseignants - Gestion de classes, devoirs, ressources et plus encore.',
            category: 'web',
            featured: true,
            technologies: ['TypeScript', 'Next.js'],
            year: 2025,
            lastUpdate: 'Septembre 2025',
            account: 'likedevGit',
            status: 'active',
            licence: 'MIT'
        },
        {
            id: 'cv-letter-assistant',
            title: 'CV & Letter Assistant',
            description: 'Assistant pour la création de CV et lettres de motivation.',
            category: 'tools',
            featured: false,
            technologies: ['HTML', 'CSS', 'JavaScript'],
            year: 2025,
            lastUpdate: 'Septembre 2025',
            account: 'likedevGit',
            status: 'active'
        },
        {
            id: 'delivery-track',
            title: 'DeliveryTrack',
            description: 'Application de suivi de livraisons avec thème Speed & Efficiency - Interface moderne, graphiques interactifs et animations avancées.',
            category: 'web',
            featured: true,
            technologies: ['TypeScript'],
            year: 2025,
            lastUpdate: 'Août 2025',
            account: 'likedevGit',
            status: 'active'
        },
        {
            id: 'client-crm',
            title: 'ClientCRM',
            description: 'CRM simple et modulaire pour PME - Next.js, TypeScript, Tailwind.',
            category: 'web',
            featured: true,
            technologies: ['TypeScript', 'Next.js', 'Tailwind CSS'],
            year: 2025,
            lastUpdate: 'Août 2025',
            account: 'likedevGit',
            status: 'active'
        },
        {
            id: 'duel-de-dame-likedev',
            title: 'DuelDeDame',
            description: 'Jeu de dame développé avec des patterns designs. Pour l\'apprentissage.',
            category: 'web',
            featured: true,
            technologies: ['TypeScript'],
            year: 2025,
            lastUpdate: 'Août 2025',
            account: 'likedevGit',
            status: 'active',
            licence: 'MIT'
        },
        {
            id: 'l-atelier-du-savoir',
            title: 'L\'Atelier du Savoir',
            description: 'Échange et vente de cours, formations et tests en ligne.',
            category: 'web',
            featured: true,
            technologies: ['JavaScript'],
            year: 2025,
            lastUpdate: 'Août 2025',
            account: 'likedevGit',
            status: 'active'
        },
        {
            id: 'quick-bill',
            title: 'QuickBill',
            description: 'Gestionnaire de factures scannés, de rapports et analyses.',
            category: 'web',
            featured: true,
            technologies: ['TypeScript'],
            year: 2025,
            lastUpdate: 'Août 2025',
            account: 'likedevGit',
            status: 'active'
        },
        {
            id: 'social-care-hub',
            title: 'SocialCare Hub',
            description: 'Regroupement de services sociaux sur une seule plate-forme.',
            category: 'web',
            featured: true,
            technologies: ['TypeScript'],
            year: 2025,
            lastUpdate: 'Août 2025',
            account: 'likedevGit',
            status: 'active'
        }
    ],

    getProjectById(id) {
        return this.projects.find(project => project.id === id);
    },

    getProjectsByCategory(category) {
        if (category === 'all') return this.projects;
        return this.projects.filter(project => project.category === category);
    },

    getProjectsByYear(year) {
        return this.projects.filter(project => project.year === year);
    },

    getProjectsByStatus(status) {
        return this.projects.filter(project => project.status === status);
    },

    getFeaturedProjects() {
        return this.projects.filter(project => project.featured);
    },

    getProjectsByAccount(account) {
        return this.projects.filter(project => project.account === account);
    },

    getTechnologies() {
        const allTechs = this.projects.flatMap(project => project.technologies);
        return [...new Set(allTechs)].filter(tech => tech);
    }
};

// Export pour utilisation globale
window.GitHubProjects = GitHubProjects;

