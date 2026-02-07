/* ========================================
   PORTFOLIO DATA - Projets réels
   ======================================== */

const PortfolioData = {
    projects: [
        {
            id: 'quickbill',
            title: 'QuickBill - Gestionnaire de factures scannées',
            description: 'Application web Next.js pour centraliser des factures scannées, extraire automatiquement les données (OCR) et générer des rapports clairs pour la comptabilité.',
            category: 'web',
            featured: true,
            technologies: ['Next.js', 'TypeScript', 'Tailwind CSS', 'Prisma', 'PostgreSQL', 'OCR', 'Docker'],
            features: [
                'Import de factures scannées et PDF',
                'Extraction automatique des montants et fournisseurs',
                'Tableaux de bord et filtres avancés',
                'Architecture modulaire et typée (TypeScript)',
                'Déploiement containerisé avec Docker'
            ],
            year: 2025,
            duration: '3 mois',
            team: 'Solo'
        },
        {
            id: 'cryptospreadedge',
            title: 'CryptoSpreadEdge - Trading crypto avec IA',
            description: 'Système de trading crypto haute fréquence basé sur l\'analyse de données de marché et des modèles de machine learning.',
            category: 'web',
            featured: true,
            technologies: ['Python', 'Pandas', 'NumPy', 'scikit-learn', 'Docker Swarm', 'Redis'],
            features: [
                'Ingestion continue de données de marché',
                'Stratégies de trading basées sur des modèles ML',
                'Architecture distribuée avec Docker Swarm',
                'Monitoring des positions et des performances',
                'Backtests et simulations'
            ],
            year: 2025,
            duration: '4 mois',
            team: 'Solo'
        },
        {
            id: 'educonnect',
            title: 'EduConnect - Plateforme éducative',
            description: 'Plateforme pour enseignants et établissements: gestion de classes, devoirs, ressources pédagogiques et suivi des élèves.',
            category: 'web',
            featured: true,
            technologies: ['Next.js', 'TypeScript', 'Tailwind CSS', 'Node.js', 'PostgreSQL'],
            features: [
                'Gestion des classes, devoirs et ressources',
                'Espace enseignant et espace élève',
                'Interface moderne et responsive',
                'Architecture orientée modules',
                'Tests et CI de base'
            ],
            year: 2025,
            duration: '3 mois',
            team: 'Solo'
        },
        {
            id: 'socialcare-hub',
            title: 'SocialCare Hub - Plateforme de services sociaux',
            description: 'Plateforme centralisée pour regrouper des services sociaux, faciliter l’orientation et le suivi des bénéficiaires.',
            category: 'web',
            featured: true,
            technologies: ['Next.js', 'TypeScript', 'Tailwind CSS', 'API REST', 'PostgreSQL'],
            features: [
                'Catalogue de services sociaux filtrable',
                'Fiches détaillées et critères d’éligibilité',
                'Gestion de comptes et rôles',
                'Intégration d’APIs externes',
                'Interface accessible et responsive'
            ],
            year: 2025,
            duration: '2 mois',
            team: 'Solo'
        },
        {
            id: 'photos-share',
            title: 'Photos Share - Partage de photos privées',
            description: 'Application React pour partager des photos en privé avec un contrôle fin des accès et de la confidentialité.',
            category: 'web',
            featured: false,
            technologies: ['React', 'JavaScript', 'Node.js', 'Express', 'MongoDB'],
            features: [
                'Gestion d’albums privés',
                'Invitations et partage sécurisé',
                'Interface utilisateur moderne',
                'API REST pour la gestion des médias',
                'Déploiement sur infrastructure cloud'
            ],
            year: 2024,
            duration: '2 mois',
            team: 'Solo'
        },
        {
            id: 'duel-de-dame',
            title: 'DuelDeDame - Jeu de dames en ligne',
            description: 'Jeu de dames en TypeScript conçu pour l’apprentissage des design patterns et la mise en pratique d’architectures propres.',
            category: 'web',
            featured: false,
            technologies: ['TypeScript', 'Next.js', 'Socket.io', 'Design Patterns'],
            features: [
                'Logique métier modélisée avec des patterns de conception',
                'Parties en temps réel avec Socket.io',
                'Interface claire et responsive',
                'Tests unitaires sur la logique de jeu',
                'Projet vitrine pour la qualité de code'
            ],
            year: 2025,
            duration: '1 mois',
            team: 'Solo'
        },
        {
            id: 'youtube-downloader',
            title: 'YouTube Downloader - Plateforme de téléchargement vidéo',
            description: 'Outil en Python pour télécharger et convertir des vidéos YouTube avec interface simple.',
            category: 'desktop',
            featured: false,
            technologies: ['Python', 'Requests', 'FFmpeg', 'Tkinter'],
            features: [
                'Téléchargement de vidéos et audio',
                'Conversion dans plusieurs formats',
                'Interface desktop simple',
                'Gestion de file d’attente',
                'Logs et gestion des erreurs'
            ],
            year: 2024,
            duration: '1 mois',
            team: 'Solo'
        }
    ],

    getProjectById(id) {
        return this.projects.find(project => project.id === id);
    },

    getProjectsByCategory(category) {
        if (category === 'all') return this.projects;
        return this.projects.filter(project => project.category === category);
    },

    getFeaturedProjects() {
        return this.projects.filter(project => project.featured);
    }
};

// Rendu du portfolio
function renderPortfolio(filter = 'all') {
    const grid = document.getElementById('portfolioGrid');
    if (!grid) return;

    const projects = PortfolioData.getProjectsByCategory(filter);
    
    grid.innerHTML = projects.map(project => `
        <div class="portfolio-item" data-category="${project.category}">
            <div class="portfolio-image">
                <div class="portfolio-overlay">
                    <div class="portfolio-actions">
                        <button class="portfolio-btn" onclick="showProjectDetails('${project.id}')">
                            <i class="fas fa-eye"></i>
                            Voir les détails
                        </button>
                    </div>
                </div>
            </div>
            <div class="portfolio-content">
                <h3 class="portfolio-title">${project.title}</h3>
                <p class="portfolio-description">${project.description}</p>
                <div class="portfolio-tech">
                    ${project.technologies.map(tech => `<span class="tech-tag">${tech}</span>`).join('')}
                </div>
                <div class="portfolio-meta">
                    <span class="portfolio-year">${project.year}</span>
                    <span class="portfolio-duration">${project.duration}</span>
                </div>
            </div>
        </div>
    `).join('');
}

// Initialisation
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        renderPortfolio('all');
    });
} else {
    renderPortfolio('all');
}

// Export pour utilisation globale
window.PortfolioData = PortfolioData;
window.renderPortfolio = renderPortfolio;

