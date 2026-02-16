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
            team: 'Solo',
            imageUrl: 'assets/images/projets/QuickBill.jpg'
        },
        {
            id: 'cryptospreadedge',
            title: 'CryptoSpreadEdge - Trading crypto avec IA',
            description: 'Système de trading crypto haute fréquence basé sur l\'analyse de données de marché et des modèles de machine learning.',
            category: 'specialized',
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
            team: 'Solo',
            imageUrl: 'assets/images/projets/CryptoSpreadEdge.jpg'
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
            team: 'Solo',
            imageUrl: 'assets/images/projets/EduConnect.jpg'
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
            team: 'Solo',
            imageUrl: 'assets/images/projets/SocialCare-Hub.jpg'
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
            team: 'Solo',
            imageUrl: 'assets/images/projets/PhotosShare.jpg'
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
            team: 'Solo',
            imageUrl: 'assets/images/projets/DuelDeDame.jpg'
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
            team: 'Solo',
            imageUrl: 'assets/images/projets/YoutubeDownloader.jpg'
        },
        {
            id: 'clipforge-l57',
            title: 'ClipForge - Shorts viraux en local',
            description: 'Création de shorts viraux en local : ingest, STT, TTS, montage, export TikTok. API NestJS, workers Python, dashboard Next.js.',
            category: 'specialized',
            featured: true,
            technologies: ['NestJS', 'Python', 'Next.js', 'TTS', 'STT'],
            features: [
                'Ingest vidéo et transcription (STT)',
                'Synthèse vocale (TTS) et montage',
                'Export TikTok et réseaux',
                'API NestJS et workers Python',
                'Dashboard Next.js'
            ],
            year: 2026,
            duration: 'En cours',
            team: 'Solo',
            imageUrl: 'assets/images/projets/ClipForge.jpg'
        },
        {
            id: 'cryptocluster-l57',
            title: 'CryptoCluster - Données crypto distribuées',
            description: 'Plateforme distribuée de collecte et d\'analyse de données crypto : RedisTimeSeries, InfluxDB, Dispy, CCXT. API FastAPI, web et mobile.',
            category: 'specialized',
            featured: true,
            technologies: ['Python', 'FastAPI', 'Redis', 'InfluxDB', 'Dispy'],
            features: [
                'Collecte multi-sources (CCXT)',
                'Stockage RedisTimeSeries et InfluxDB',
                'Calcul distribué Dispy',
                'API FastAPI et interfaces web/mobile',
                'Analyses et tableaux de bord'
            ],
            year: 2026,
            duration: 'En cours',
            team: 'Solo',
            imageUrl: 'assets/images/projets/CryptoCluster.jpg'
        },
        {
            id: 'jobhunter-l57',
            title: 'JobHunter - Scraping offres d\'emploi',
            description: 'Système de scraping intelligent d\'offres d\'emploi et d\'intérim (Indeed, HelloWork, LinkedIn, France Travail). FastAPI, Celery, optimisé Raspberry Pi.',
            category: 'tools',
            featured: true,
            technologies: ['Python', 'FastAPI', 'Celery', 'Scraping'],
            features: [
                'Agrégation multi-sources (Indeed, HelloWork, etc.)',
                'Tâches asynchrones Celery',
                'API FastAPI et filtres',
                'Déploiement léger type Raspberry Pi',
                'Dédoublonnage et normalisation'
            ],
            year: 2026,
            duration: 'En cours',
            team: 'Solo',
            imageUrl: 'assets/images/projets/JobHunter.jpg'
        },
        {
            id: 'ecodatahub-l57',
            title: 'EcoDataHub - Données économiques',
            description: 'Plateforme multi-sources pour l\'accès aux données économiques (Eurostat, INSEE, BdF, OCDE, Banque mondiale). FastAPI, ML, économétrie, rapports LLM.',
            category: 'specialized',
            featured: true,
            technologies: ['Python', 'FastAPI', 'ML', 'LLM', 'Économétrie'],
            features: [
                'Agrégation Eurostat, INSEE, BdF, OCDE',
                'Analyses et modèles ML',
                'Rapports générés par LLM',
                'API FastAPI documentée',
                'Visualisations et exports'
            ],
            year: 2026,
            duration: 'En cours',
            team: 'Solo',
            imageUrl: 'assets/images/projets/EcoDataHub.jpg'
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

/** Délai en ms entre chaque chargement d'image (étalement des requêtes). */
const PORTFOLIO_IMAGE_STAGGER_MS = 80;

/** Nombre d'images à charger immédiatement (premier écran). */
const PORTFOLIO_IMAGE_EAGER_COUNT = 3;

/**
 * Programme le chargement des images avec des délais décalés pour limiter les requêtes simultanées.
 * Utilise le système ImageLoader pour charger les WebP avec fallback et cache.
 * @param {HTMLElement} container - Conteneur des .portfolio-item (ou .project-card)
 * @param {string} imgSelector - Sélecteur des img (ex: '.portfolio-image-img' ou '.project-card-image img')
 * @param {number} staggerMs - Délai en ms entre chaque image
 * @param {number} eagerCount - Nombre d'images à charger sans délai
 */
function scheduleStaggeredImageLoad(container, imgSelector, staggerMs, eagerCount) {
    if (!container) return;
    const imgs = container.querySelectorAll(imgSelector);
    
    // Utilise ImageLoader si disponible, sinon fallback sur l'ancien système
    if (window.imageLoader) {
        window.imageLoader.loadImagesStaggered(imgs, {
            staggerMs,
            eagerCount,
            useWebP: true,
            useCache: true
        });
    } else {
        // Fallback : ancien système sans WebP
        imgs.forEach((img, index) => {
            const src = img.getAttribute('data-src');
            if (!src) return;
            const delay = index < eagerCount ? 0 : (index - eagerCount) * staggerMs;
            setTimeout(() => {
                img.src = src;
                img.removeAttribute('data-src');
                img.onload = () => img.classList.add('loaded');
            }, delay);
        });
    }
}

// Rendu du portfolio
function renderPortfolio(filter = 'all') {
    const grid = document.getElementById('portfolioGrid');
    if (!grid) return;

    const projects = PortfolioData.getProjectsByCategory(filter);
    
    grid.innerHTML = projects.map(project => {
        let imageContent = '';
        if (project.imageUrl) {
            // Utilise picture avec source WebP si ImageLoader est disponible
            if (window.imageLoader) {
                const webpUrl = project.imageUrl.replace(/\.(jpg|jpeg|png)$/i, '.webp');
                imageContent = `
                    <picture>
                        <source data-src="${webpUrl}" type="image/webp">
                        <img data-src="${project.imageUrl}" alt="" class="portfolio-image-img" loading="lazy" decoding="async">
                    </picture>`;
            } else {
                imageContent = `<img data-src="${project.imageUrl}" alt="" class="portfolio-image-img" loading="lazy" decoding="async">`;
            }
        }
        return `
        <div class="portfolio-item" data-category="${project.category}">
            <div class="portfolio-image">
                ${imageContent}
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
    `;
    }).join('');

    // Charge les images avec WebP et cache
    scheduleStaggeredImageLoad(grid, '.portfolio-image-img', PORTFOLIO_IMAGE_STAGGER_MS, PORTFOLIO_IMAGE_EAGER_COUNT);
    
    // Charge aussi les sources WebP (uniquement si data-src present, evite srcset="null")
    if (window.imageLoader) {
        const pictureSources = grid.querySelectorAll('picture source[data-src]');
        pictureSources.forEach((source, index) => {
            const dataSrc = source.getAttribute('data-src');
            if (!dataSrc) return;
            const delay = index < PORTFOLIO_IMAGE_EAGER_COUNT ? 0 : (index - PORTFOLIO_IMAGE_EAGER_COUNT) * PORTFOLIO_IMAGE_STAGGER_MS;
            setTimeout(() => {
                source.srcset = dataSrc;
                source.removeAttribute('data-src');
            }, delay);
        });
    }
}

// Initialisation
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        renderPortfolio('all');
    });
} else {
    renderPortfolio('all');
}

/** URL du JSON des depots loupix57 (genere par scripts/generate-repos-loupix57.ps1) */
const REPOS_JSON_URL = 'assets/data/repos-loupix57.json';

/** Cache des donnees repos apres premier chargement */
let reposCache = null;

/**
 * Charge le JSON des repos loupix57 (une seule fois).
 * @returns {Promise<Array>} Tableau des depots
 */
function loadReposJson() {
    if (reposCache) return Promise.resolve(reposCache);
    return fetch(REPOS_JSON_URL)
        .then(r => r.ok ? r.json() : [])
        .then(data => {
            reposCache = Array.isArray(data) ? data : [];
            return reposCache;
        })
        .catch(() => []);
}

/**
 * Retourne le nom du depot pour faire la liaison avec le projet (titre ou id).
 * @param {Object} project - Projet depuis PortfolioData ou GitHubProjects
 * @returns {string} Nom du repo (ex: QuickBill, DuelDeDame)
 */
function getRepoNameFromProject(project) {
    if (!project) return '';
    const fromTitle = (project.title || '').split(' - ')[0].trim().split(' | ')[0].trim();
    if (fromTitle) return fromTitle;
    const fromId = (project.id || '').replace(/-l57$/, '').replace(/-/g, '');
    return fromId ? fromId.charAt(0).toUpperCase() + fromId.slice(1) : '';
}

/**
 * Trouve un depot dans la liste par nom (insensible a la casse, tirets/espaces).
 * @param {Array} repos - Liste des depots
 * @param {string} name - Nom affiche du projet
 * @returns {Object|null} Depot ou null
 */
function findRepoByName(repos, name) {
    if (!name || !repos.length) return null;
    const norm = s => String(s).toLowerCase().replace(/[\s-]/g, '');
    const n = norm(name);
    return repos.find(r => norm(r.name) === n) || repos.find(r => r.name === name) || null;
}

/**
 * Ouvre la modale "Details du projet" avec les infos du projet et du depot GitHub.
 * @param {string} projectId - Id du projet (portfolio ou github-projects)
 */
function showProjectDetails(projectId) {
    const modal = document.getElementById('modalProjet');
    const backdrop = document.getElementById('modalProjetBackdrop');
    const closeBtn = document.getElementById('modalProjetClose');
    const loadingEl = document.getElementById('modalProjetLoading');
    const contentEl = document.getElementById('modalProjetContent');
    const errorEl = document.getElementById('modalProjetError');
    if (!modal || !contentEl) return;

    const focusReturn = typeof document.activeElement !== 'undefined' && document.activeElement && document.activeElement !== document.body
        ? document.activeElement
        : null;

    loadingEl.style.display = 'block';
    contentEl.style.display = 'none';
    errorEl.style.display = 'none';
    modal.classList.add('modal-projet-open');
    modal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    if (closeBtn) closeBtn.focus();

    const closeModal = () => {
        if (modal.contains(document.activeElement)) {
            if (focusReturn && typeof focusReturn.focus === 'function') {
                focusReturn.focus();
            } else if (closeBtn) {
                closeBtn.blur();
            }
        }
        modal.classList.remove('modal-projet-open');
        modal.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
    };

    const showError = () => {
        loadingEl.style.display = 'none';
        contentEl.style.display = 'none';
        errorEl.style.display = 'block';
    };

    const project = (window.PortfolioData && PortfolioData.getProjectById(projectId))
        || (window.GitHubProjects && GitHubProjects.getProjectById(projectId));
    const repoName = getRepoNameFromProject(project);

    loadReposJson().then(repos => {
        loadingEl.style.display = 'none';
        const repo = findRepoByName(repos, repoName);
        if (!repo) {
            showError();
            return;
        }
        const titleEl = document.getElementById('modalProjetTitle');
        const descEl = document.getElementById('modalProjetDesc');
        const metaEl = document.getElementById('modalProjetMeta');
        const techEl = document.getElementById('modalProjetTech');
        const topicsEl = document.getElementById('modalProjetTopics');
        const linkEl = document.getElementById('modalProjetLink');
        const imageWrap = document.getElementById('modalProjetImageWrap');

        if (titleEl) titleEl.textContent = repo.name;
        if (descEl) descEl.textContent = repo.description || (project && project.description) || '';
        if (linkEl) {
            linkEl.href = repo.html_url;
            linkEl.style.display = 'inline-flex';
        }

        const imageUrl = (project && project.imageUrl) || `assets/images/projets/${repo.name}.jpg`;
        if (imageWrap) {
            // Utilise ImageLoader pour charger avec WebP et cache
            if (window.imageLoader) {
                const img = document.createElement('img');
                img.alt = '';
                img.loading = 'lazy';
                img.decoding = 'async';
                imageWrap.innerHTML = '';
                imageWrap.appendChild(img);
                window.imageLoader.loadImage(img, imageUrl, {
                    useWebP: true,
                    useCache: true,
                    priority: 'high'
                }).catch(() => {
                    // Fallback si erreur
                    img.src = imageUrl;
                });
            } else {
                imageWrap.innerHTML = `<img src="${imageUrl}" alt="" loading="lazy">`;
            }
        }

        const meta = [];
        if (repo.language) meta.push(['Langage', repo.language]);
        if (repo.updated_at) meta.push(['Derniere maj', new Date(repo.updated_at).toLocaleDateString('fr-FR')]);
        if (repo.created_at) meta.push(['Cree le', new Date(repo.created_at).toLocaleDateString('fr-FR')]);
        if (repo.stargazers_count != null) meta.push(['Etoiles', repo.stargazers_count]);
        if (repo.forks_count != null) meta.push(['Forks', repo.forks_count]);
        if (repo.default_branch) meta.push(['Branche', repo.default_branch]);
        if (repo.license) meta.push(['Licence', repo.license]);
        if (metaEl) metaEl.innerHTML = meta.map(([k, v]) => `<dt>${k}</dt><dd>${v}</dd>`).join('');

        const techs = (project && project.technologies) || (repo.language ? [repo.language] : []);
        if (techEl) techEl.innerHTML = techs.length
            ? techs.map(t => `<span class="tech-tag">${t}</span>`).join('')
            : '';

        if (topicsEl && repo.topics && repo.topics.length) {
            topicsEl.innerHTML = repo.topics.map(t => `<span class="tech-tag">${t}</span>`).join('');
            topicsEl.style.display = 'flex';
        } else if (topicsEl) topicsEl.style.display = 'none';

        contentEl.style.display = 'block';
    }).catch(showError);

    closeBtn.addEventListener('click', closeModal, { once: true });
    backdrop.addEventListener('click', closeModal, { once: true });
    const onEsc = (e) => {
        if (e.key === 'Escape' && modal.classList.contains('modal-projet-open')) {
            closeModal();
            document.removeEventListener('keydown', onEsc);
        }
    };
    document.addEventListener('keydown', onEsc);
}

// Export pour utilisation globale
window.PortfolioData = PortfolioData;
window.renderPortfolio = renderPortfolio;
window.showProjectDetails = showProjectDetails;
window.scheduleStaggeredImageLoad = scheduleStaggeredImageLoad;

