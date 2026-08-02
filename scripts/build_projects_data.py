#!/usr/bin/env python3
"""
Genere src/data/projects.json a partir de assets/data/repos-loupix57.json
et de la liste des autres projets (loupix, likedevGit).
Chaque projet a : id (slug URL), title, description, category, technologies,
year, account, status, featured, licence, imageUrl, repo, github_url, stars, forks, etc.
"""
import json
import re
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
REPOS_FILE = BASE_DIR / 'assets' / 'data' / 'repos-loupix57.json'
OUT_FILE = BASE_DIR / 'src' / 'data' / 'projects.json'
ALIASES_FILE = BASE_DIR / 'src' / 'data' / 'project-slug-aliases.json'

# Categories et technologies par repo name (loupix57) - aligne avec github-projects.js
REPO_META = {
    'ClientCRM': ('web', ['Next.js', 'React', 'TypeScript']),
    'ClipForge': ('specialized', ['NestJS', 'Python', 'Next.js']),
    'CryptoCluster': ('specialized', ['Python', 'FastAPI', 'Redis', 'InfluxDB']),
    'CryptoSpreadEdge': ('specialized', ['Python', 'FastAPI', 'Docker Swarm', 'IA']),
    'CvLetterAssistant': ('tools', ['Node.js', 'Express', 'Ollama', 'LLM']),
    'DataWhisper': ('specialized', ['Python', 'FastAPI', 'React', 'Docker']),
    'DeliveryTrack': ('web', ['Next.js', 'TypeScript']),
    'Design-Patterns': ('learning', ['Java', 'Go', 'Python', 'TypeScript', 'PHP']),
    'DispyCluster': ('tools', ['Python', 'Raspberry Pi', 'Dispy']),
    'DistributionJournaux': ('web', ['Node.js', 'MongoDB']),
    'DuelDeDame': ('web', ['Next.js', 'NestJS', 'TypeScript']),
    'DuelDeDame-Legacy': ('web', ['TypeScript']),
    'EcoDataHub': ('specialized', ['Python', 'FastAPI', 'ML', 'LLM']),
    'EduConnect': ('web', ['Next.js', 'React', 'TypeScript', 'Tailwind']),
    'GestionnaireEvenements': ('web', ['PHP']),
    'IntelliReply': ('iot', ['Python', 'Flask']),
    'JobHunter': ('tools', ['Python', 'FastAPI', 'Celery']),
    'JournauxGestion': ('web', ['Python', 'Django', 'Angular', 'Flutter']),
    'LAtelierDuSavoir': ('web', ['JavaScript']),
    'NftCrypto': ('specialized', ['TypeScript', 'Blockchain', 'NFT']),
    'PhotosShare': ('web', ['React', 'JavaScript']),
    'QuickBill': ('web', ['Next.js', 'Prisma', 'OCR']),
    'RestaurationRapide': ('web', ['Node.js', 'MongoDB']),
    'scalpel-numerique': ('specialized', ['Python', 'MediaPipe', 'Kivy']),
    'SocialCare-Hub': ('web', ['React', 'TypeScript']),
    'TapTapCar': ('web', ['PHP']),
    'TicketCaisse': ('mobile', ['Dart', 'Flutter', 'OCR']),
    'turfrace': ('specialized', ['Python', 'FastAPI', 'ML']),
    'YoutubeDownloader': ('tools', ['Python', 'AngularJS']),
}

FEATURED_L57 = {
    'ClientCRM', 'ClipForge', 'CryptoCluster', 'CryptoSpreadEdge',
    'CvLetterAssistant', 'DataWhisper', 'DeliveryTrack', 'DispyCluster', 'DuelDeDame',
    'EcoDataHub', 'EduConnect', 'JobHunter', 'LAtelierDuSavoir', 'NftCrypto', 'QuickBill',
    'RestaurationRapide', 'scalpel-numerique', 'SocialCare-Hub', 'TicketCaisse', 'turfrace',
}

REPO_LICENCE = {
    'DuelDeDame-Legacy': 'MIT', 'EduConnect': 'MIT',
}

OTHER_PROJECTS = [
    {'id': 'dispy-cluster', 'title': 'DispyCluster', 'description': 'Système de clustering distribué pour le traitement de données.', 'category': 'tools', 'technologies': ['Python'], 'year': 2025, 'lastUpdate': 'Novembre 2025', 'account': 'loupix', 'status': 'active', 'featured': True, 'imageUrl': 'assets/images/projets/DispyCluster.jpg'},
    {'id': 'duel-de-dame-loupix', 'title': 'DuelDeDame', 'description': 'Jeu de dame développé avec des patterns designs. Pour l\'apprentissage.', 'category': 'web', 'technologies': ['TypeScript'], 'year': 2025, 'lastUpdate': 'Septembre 2025', 'account': 'loupix', 'status': 'active', 'featured': True, 'licence': 'MIT', 'imageUrl': 'assets/images/projets/DuelDeDame.jpg'},
    {'id': 'crypto-spread-edge', 'title': 'CryptoSpreadEdge', 'description': 'Système de trading crypto haute fréquence avec IA et déploiement Docker Swarm.', 'category': 'specialized', 'technologies': ['Python', 'IA', 'Docker Swarm'], 'year': 2025, 'lastUpdate': 'Septembre 2025', 'account': 'loupix', 'status': 'active', 'featured': True, 'imageUrl': 'assets/images/projets/CryptoSpreadEdge.jpg'},
    {'id': 'ticket-caisse', 'title': 'TicketCaisse', 'description': 'Application mobile de gestion de caisse et tickets.', 'category': 'mobile', 'technologies': ['Dart', 'Flutter'], 'year': 2025, 'lastUpdate': 'Septembre 2025', 'account': 'loupix', 'status': 'active', 'featured': True, 'imageUrl': 'assets/images/projets/TicketCaisse.jpg'},
    {'id': 'intelli-reply', 'title': 'IntelliReply', 'description': 'Système intelligent de réponse automatique.', 'category': 'tools', 'technologies': ['Python', 'IA'], 'year': 2025, 'lastUpdate': 'Septembre 2025', 'account': 'loupix', 'status': 'active', 'featured': False, 'imageUrl': 'assets/images/projets/IntelliReply.jpg'},
    {'id': 'torrent-sphere-app', 'title': 'TorrentSphere App', 'description': 'Application de téléchargement de torrents.', 'category': 'tools', 'technologies': [], 'year': 2025, 'lastUpdate': 'Septembre 2025', 'account': 'loupix', 'status': 'active', 'featured': False},
    {'id': 'torrent-sphere-platform', 'title': 'TorrentSphere Platform', 'description': 'Plateforme de téléchargement de torrents avec scraping automatique.', 'category': 'specialized', 'technologies': [], 'year': 2025, 'lastUpdate': 'Septembre 2025', 'account': 'loupix', 'status': 'active', 'featured': False},
    {'id': 'journaux-gestion', 'title': 'Journaux Gestion', 'description': 'Système de gestion de journaux.', 'category': 'web', 'technologies': [], 'year': 2024, 'lastUpdate': 'Avril 2024', 'account': 'loupix', 'status': 'archived', 'featured': False},
    {'id': 'nft-et-crypto', 'title': 'NFT & Crypto', 'description': 'Recherche en Contrat virtuel / NFT.', 'category': 'specialized', 'technologies': ['TypeScript', 'Blockchain', 'NFT'], 'year': 2024, 'lastUpdate': 'Avril 2024', 'account': 'loupix', 'status': 'archived', 'featured': True},
    {'id': 'design-patterns', 'title': 'Design Patterns', 'description': 'Implémentation de patterns de conception en PHP.', 'category': 'learning', 'technologies': ['PHP'], 'year': 2024, 'lastUpdate': 'Avril 2024', 'account': 'loupix', 'status': 'archived', 'featured': False},
    {'id': 'restauration', 'title': 'Plateforme de Restauration', 'description': 'Plateforme de restauration entièrement configurable / NoCode.', 'category': 'web', 'technologies': ['JavaScript'], 'year': 2024, 'lastUpdate': 'Avril 2024', 'account': 'loupix', 'status': 'archived', 'featured': True},
    {'id': 'photos-share', 'title': 'Partage de Photos', 'description': 'Partage de photos développé en ReactJs.', 'category': 'web', 'technologies': ['JavaScript', 'React'], 'year': 2024, 'lastUpdate': 'Avril 2024', 'account': 'loupix', 'status': 'archived', 'featured': True},
    {'id': 'youtube-downloader', 'title': 'YouTube Downloader', 'description': 'Plateforme de téléchargement de vidéo.', 'category': 'tools', 'technologies': ['Python'], 'year': 2024, 'lastUpdate': 'Avril 2024', 'account': 'loupix', 'status': 'archived', 'featured': False},
    {'id': 'taptapcar', 'title': 'TapTapCar', 'description': 'Logiciel de covoiturage.', 'category': 'web', 'technologies': ['PHP'], 'year': 2024, 'lastUpdate': 'Avril 2024', 'account': 'loupix', 'status': 'archived', 'featured': False},
    {'id': 'distribution-journaux', 'title': 'Distribution de Journaux', 'description': 'Distribution de journaux dans le grand duché.', 'category': 'web', 'technologies': ['JavaScript'], 'year': 2024, 'lastUpdate': 'Avril 2024', 'account': 'loupix', 'status': 'archived', 'featured': False},
    {'id': 'gestionnaire-evenements', 'title': 'Gestionnaire d\'Événements', 'description': 'Gestionnaire d\'événement.', 'category': 'web', 'technologies': ['PHP'], 'year': 2024, 'lastUpdate': 'Avril 2024', 'account': 'loupix', 'status': 'archived', 'featured': False},
    {'id': 'edu-connect', 'title': 'EduConnect', 'description': 'Plateforme éducative moderne pour enseignants - Gestion de classes, devoirs, ressources et plus encore.', 'category': 'web', 'technologies': ['TypeScript', 'Next.js'], 'year': 2025, 'lastUpdate': 'Septembre 2025', 'account': 'likedevGit', 'status': 'active', 'featured': True, 'licence': 'MIT', 'repo': 'likedevGit/EduConnect'},
    {'id': 'cv-letter-assistant', 'title': 'CV & Letter Assistant', 'description': 'Assistant pour la création de CV et lettres de motivation.', 'category': 'tools', 'technologies': ['HTML', 'CSS', 'JavaScript'], 'year': 2025, 'lastUpdate': 'Septembre 2025', 'account': 'likedevGit', 'status': 'active', 'featured': False, 'repo': 'likedevGit/CvLetterAssistant'},
    {'id': 'delivery-track', 'title': 'DeliveryTrack', 'description': 'Application de suivi de livraisons avec thème Speed & Efficiency - Interface moderne, graphiques interactifs et animations avancées.', 'category': 'web', 'technologies': ['TypeScript'], 'year': 2025, 'lastUpdate': 'Août 2025', 'account': 'likedevGit', 'status': 'active', 'featured': True, 'repo': 'likedevGit/DeliveryTrack'},
    {'id': 'client-crm', 'title': 'ClientCRM', 'description': 'CRM simple et modulaire pour PME - Next.js, TypeScript, Tailwind.', 'category': 'web', 'technologies': ['TypeScript', 'Next.js', 'Tailwind CSS'], 'year': 2025, 'lastUpdate': 'Août 2025', 'account': 'likedevGit', 'status': 'active', 'featured': True, 'repo': 'likedevGit/ClientCRM'},
    {'id': 'duel-de-dame-likedev', 'title': 'DuelDeDame', 'description': 'Jeu de dame développé avec des patterns designs. Pour l\'apprentissage.', 'category': 'web', 'technologies': ['TypeScript'], 'year': 2025, 'lastUpdate': 'Août 2025', 'account': 'likedevGit', 'status': 'active', 'featured': True, 'licence': 'MIT', 'repo': 'likedevGit/DuelDeDame'},
    {'id': 'l-atelier-du-savoir', 'title': 'L\'Atelier du Savoir', 'description': 'Échange et vente de cours, formations et tests en ligne.', 'category': 'web', 'technologies': ['JavaScript'], 'year': 2025, 'lastUpdate': 'Août 2025', 'account': 'likedevGit', 'status': 'active', 'featured': True, 'repo': 'likedevGit/LAtelierDuSavoir'},
    {'id': 'quick-bill', 'title': 'QuickBill', 'description': 'Gestionnaire de factures scannés, de rapports et analyses.', 'category': 'web', 'technologies': ['TypeScript'], 'year': 2025, 'lastUpdate': 'Août 2025', 'account': 'likedevGit', 'status': 'active', 'featured': True, 'repo': 'likedevGit/QuickBill'},
    {'id': 'social-care-hub', 'title': 'SocialCare Hub', 'description': 'Regroupement de services sociaux sur une seule plate-forme.', 'category': 'web', 'technologies': ['TypeScript'], 'year': 2025, 'lastUpdate': 'Août 2025', 'account': 'likedevGit', 'status': 'active', 'featured': True, 'repo': 'likedevGit/SocialCare-Hub'},
]

MANUAL_SLUG_ALIASES = {
    'photos-share': 'photosshare',
    'restauration': 'restaurationrapide',
    'distribution-journaux': 'distributionjournaux',
    'gestionnaire-evenements': 'gestionnaireevenements',
}


def name_to_slug(name: str) -> str:
    return name.replace('_', '-').lower()


def _norm_title(title: str) -> str:
    return re.sub(r'[^a-z0-9]', '', (title or '').lower())


def _repo_basename(repo: str) -> str:
    if not repo:
        return ''
    return re.sub(r'[^a-z0-9]', '', repo.split('/')[-1].lower())


class _ProjectRegistry:
    def __init__(self) -> None:
        self.projects: list = []
        self.aliases: dict[str, str] = {}
        self._by_title: dict[str, str] = {}
        self._by_repo: dict[str, str] = {}
        self._by_slug: dict[str, str] = {}

    def add(self, project: dict) -> bool:
        slug = (project.get('slug') or project.get('id') or '').strip()
        if not slug:
            return False

        title_key = _norm_title(project.get('title') or '')
        repo_key = _repo_basename(project.get('repo') or '')

        canonical = self._by_slug.get(slug)
        if not canonical and title_key:
            canonical = self._by_title.get(title_key)
        if not canonical and repo_key:
            canonical = self._by_repo.get(repo_key)

        if canonical:
            if canonical != slug:
                self.aliases[slug] = canonical
            return False

        self.projects.append(project)
        self._by_slug[slug] = slug
        if title_key:
            self._by_title[title_key] = slug
        if repo_key:
            self._by_repo[repo_key] = slug
        return True


def main():
    registry = _ProjectRegistry()

    if REPOS_FILE.exists():
        repos = json.loads(REPOS_FILE.read_text(encoding='utf-8-sig'))
        by_name = {r['name']: r for r in repos}
        for name, (category, technologies) in REPO_META.items():
            repo = by_name.get(name)
            if not repo:
                continue
            slug = name_to_slug(name)
            desc = (repo.get('description') or '').strip() or name
            pushed = repo.get('pushed_at') or repo.get('updated_at') or ''
            try:
                year = int(datetime.fromisoformat(pushed.replace('Z', '+00:00')).year) if pushed else 2026
            except Exception:
                year = 2026
            lic = repo.get('license')
            if isinstance(lic, dict) and lic.get('spdx_id'):
                licence = lic['spdx_id']
            elif isinstance(lic, str) and lic:
                licence = lic
            else:
                licence = REPO_LICENCE.get(name, '')
            image_name = 'scalpel-numerique.jpg' if name == 'scalpel-numerique' else name.replace(' ', '-') + '.jpg'
            registry.add({
                'id': slug,
                'slug': slug,
                'title': name,
                'description': desc,
                'category': category,
                'technologies': technologies,
                'year': year,
                'lastUpdate': pushed[:10] if pushed else '2026-02-07',
                'account': 'loupix57',
                'status': 'archived' if repo.get('archived') else 'active',
                'featured': name in FEATURED_L57,
                'licence': licence or REPO_LICENCE.get(name, ''),
                'imageUrl': f'assets/images/projets/{image_name}',
                'repo': repo.get('full_name', ''),
                'github_url': repo.get('html_url', ''),
                'stars': repo.get('stargazers_count', 0),
                'forks': repo.get('forks_count', 0),
                'language': repo.get('language'),
                'archived': repo.get('archived', False),
                'pushed_at': pushed,
            })

    for p in OTHER_PROJECTS:
        pid = (p.get('id') or '').strip()
        if pid in MANUAL_SLUG_ALIASES:
            continue
        registry.add({
            'id': p['id'],
            'slug': p['id'],
            'title': p['title'],
            'description': p['description'],
            'category': p['category'],
            'technologies': p.get('technologies', []),
            'year': p['year'],
            'lastUpdate': p.get('lastUpdate', ''),
            'account': p['account'],
            'status': p['status'],
            'featured': p.get('featured', False),
            'licence': p.get('licence', ''),
            'imageUrl': p.get('imageUrl', ''),
            'repo': p.get('repo', ''),
            'github_url': f"https://github.com/{p['repo']}" if p.get('repo') else '',
            'stars': 0,
            'forks': 0,
            'archived': p.get('status') == 'archived',
            'isFork': p.get('isFork', False),
        })

    canonical_slugs = {(p.get('slug') or p.get('id') or '').strip() for p in registry.projects}
    for alias, canonical in MANUAL_SLUG_ALIASES.items():
        a = (alias or '').strip()
        c = (canonical or '').strip()
        if a and c and a != c and c in canonical_slugs and a not in registry.aliases:
            registry.aliases[a] = c

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(json.dumps(registry.projects, ensure_ascii=False, indent=2), encoding='utf-8')
    ALIASES_FILE.write_text(
        json.dumps(registry.aliases, ensure_ascii=False, indent=2, sort_keys=True),
        encoding='utf-8',
    )
    print(f"[OK] {len(registry.projects)} projets ecrits dans {OUT_FILE}")
    if registry.aliases:
        print(f"[OK] {len(registry.aliases)} alias slug -> canonical dans {ALIASES_FILE}")


if __name__ == '__main__':
    main()
