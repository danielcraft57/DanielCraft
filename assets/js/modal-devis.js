/**
 * Modale "Devis gratuit" : affiche les infos du profil GitHub loupix57 et CTA vers contact.
 * Charge les donnees via l'API GitHub et ouvre/ferme la modale.
 */
(function () {
    'use strict';

    const GITHUB_USER = 'loupix57';
    const API_USER = `https://api.github.com/users/${GITHUB_USER}`;
    const API_REPOS = `https://api.github.com/users/${GITHUB_USER}/repos?sort=updated&per_page=8`;

    const modal = document.getElementById('modalDevis');
    const backdrop = document.getElementById('modalDevisBackdrop');
    const box = document.getElementById('modalDevisBox');
    const closeBtn = document.getElementById('modalDevisClose');
    const openBtn = document.getElementById('navCtaDevis');
    const loadingEl = document.getElementById('modalDevisLoading');
    const contentEl = document.getElementById('modalDevisContent');
    const errorEl = document.getElementById('modalDevisError');

    if (!modal || !openBtn) return;

    /**
     * Ouvre la modale et charge les donnees si pas encore fait.
     */
    function openModal() {
        modal.classList.add('modal-devis-open');
        modal.setAttribute('aria-hidden', 'false');
        if (openBtn) openBtn.setAttribute('aria-expanded', 'true');
        document.body.style.overflow = 'hidden';
        if (!modal.dataset.loaded) {
            loadGitHubData();
        }
        closeBtn.focus();
    }

    /**
     * Ferme la modale.
     */
    function closeModal() {
        modal.classList.remove('modal-devis-open');
        modal.setAttribute('aria-hidden', 'true');
        if (openBtn) openBtn.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
        openBtn.focus();
    }

    /**
     * Charge le profil et les repos GitHub puis affiche le contenu.
     */
    function loadGitHubData() {
        Promise.all([
            fetch(API_USER).then(function (r) { return r.ok ? r.json() : null; }),
            fetch(API_REPOS).then(function (r) { return r.ok ? r.json() : []; })
        ]).then(function (results) {
            var user = results[0];
            var repos = Array.isArray(results[1]) ? results[1] : [];
            modal.dataset.loaded = '1';
            if (user) {
                renderProfile(user);
                renderRepos(repos);
                loadingEl.style.display = 'none';
                contentEl.style.display = 'block';
            } else {
                showError();
            }
        }).catch(function () {
            showError();
        });
    }

    /**
     * Affiche le profil utilisateur dans la modale.
     * @param {Object} user - Objet utilisateur retourne par l'API GitHub.
     */
    function renderProfile(user) {
        var avatar = document.getElementById('modalDevisAvatar');
        var name = document.getElementById('modalDevisName');
        var bio = document.getElementById('modalDevisBio');
        var meta = document.getElementById('modalDevisMeta');

        if (avatar) {
            avatar.src = user.avatar_url || '';
            avatar.alt = user.name || user.login || '';
        }
        if (name) name.textContent = user.name || user.login || '';
        if (bio) {
            bio.textContent = user.bio || 'Developpeur Full-Stack, projets web et outils.';
            bio.style.display = user.bio ? '' : 'none';
        }
        if (meta) {
            var items = [];
            if (user.location) items.push('<li><i class="fas fa-map-marker-alt" aria-hidden="true"></i> ' + escapeHtml(user.location) + '</li>');
            if (user.blog) items.push('<li><i class="fas fa-link" aria-hidden="true"></i> <a href="' + escapeHtml(user.blog) + '" target="_blank" rel="noopener noreferrer">' + escapeHtml(user.blog) + '</a></li>');
            if (user.public_repos != null) items.push('<li><i class="fas fa-folder" aria-hidden="true"></i> ' + user.public_repos + ' depots</li>');
            if (user.followers != null) items.push('<li><i class="fas fa-users" aria-hidden="true"></i> ' + user.followers + ' abonnes</li>');
            meta.innerHTML = items.join('');
        }
    }

    /**
     * Affiche la liste des repos dans la modale.
     * @param {Array} repos - Tableau de depots retourne par l'API GitHub.
     */
    function renderRepos(repos) {
        var section = document.getElementById('modalDevisReposSection');
        var list = document.getElementById('modalDevisReposList');
        if (!list) return;
        if (!repos.length) {
            if (section) section.style.display = 'none';
            return;
        }
        list.innerHTML = repos.map(function (repo) {
            var desc = repo.description ? escapeHtml(repo.description.substring(0, 80)) + (repo.description.length > 80 ? '...' : '') : '';
            var lang = repo.language ? '<span class="modal-devis-repo-lang">' + escapeHtml(repo.language) + '</span>' : '';
            return '<li class="modal-devis-repo-item">' +
                '<a href="' + escapeHtml(repo.html_url) + '" target="_blank" rel="noopener noreferrer" class="modal-devis-repo-link">' +
                '<span class="modal-devis-repo-name">' + escapeHtml(repo.name) + '</span>' + lang +
                (desc ? '<span class="modal-devis-repo-desc">' + desc + '</span>' : '') +
                '</a></li>';
        }).join('');
    }

    function escapeHtml(text) {
        var div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    function showError() {
        loadingEl.style.display = 'none';
        contentEl.style.display = 'none';
        errorEl.style.display = 'block';
    }

    openBtn.addEventListener('click', function (e) {
        e.preventDefault();
        openModal();
    });

    closeBtn.addEventListener('click', closeModal);
    backdrop.addEventListener('click', closeModal);

    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && modal.classList.contains('modal-devis-open')) {
            closeModal();
        }
    });

    // Lien CTA dans la modale : fermer apres clic (optionnel, pour UX)
    var ctaBtn = document.getElementById('modalDevisCtaBtn');
    if (ctaBtn) {
        ctaBtn.addEventListener('click', function () {
            closeModal();
        });
    }
})();
