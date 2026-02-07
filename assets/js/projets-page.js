// ===== PROJETS PAGE - Rendu des projets GitHub =====

function renderProjects(filters = {}) {
    const grid = document.getElementById('projectsGrid');
    if (!grid) return;

    let projects = GitHubProjects.projects;

    // Filtres
    if (filters.category && filters.category !== 'all') {
        projects = projects.filter(p => p.category === filters.category);
    }

    if (filters.year && filters.year !== 'all') {
        projects = projects.filter(p => p.year === parseInt(filters.year));
    }

    if (filters.status && filters.status !== 'all') {
        projects = projects.filter(p => p.status === filters.status);
    }

    // Tri par année (plus récent en premier)
    projects.sort((a, b) => {
        if (a.year !== b.year) return b.year - a.year;
        return new Date(b.lastUpdate) - new Date(a.lastUpdate);
    });

    if (projects.length === 0) {
        grid.innerHTML = '<div class="no-projects"><p>Aucun projet trouvé avec ces filtres.</p></div>';
        return;
    }

    grid.innerHTML = projects.map(project => {
        const statusBadge = project.status === 'active' 
            ? '<span class="status-badge active">Actif</span>' 
            : '<span class="status-badge archived">Archivé</span>';
        
        const licenceBadge = project.licence 
            ? `<span class="licence-badge">${project.licence}</span>` 
            : '';
        
        const forkBadge = project.isFork 
            ? '<span class="fork-badge">Fork</span>' 
            : '';

        return `
            <div class="project-card" data-category="${project.category}" data-year="${project.year}" data-status="${project.status}">
                <div class="project-header">
                    <h3 class="project-title">${project.title}</h3>
                    <div class="project-badges">
                        ${statusBadge}
                        ${licenceBadge}
                        ${forkBadge}
                    </div>
                </div>
                
                <p class="project-description">${project.description}</p>
                
                <div class="project-tech">
                    ${project.technologies.length > 0 
                        ? project.technologies.map(tech => `<span class="tech-tag">${tech}</span>`).join('')
                        : '<span class="tech-tag">À déterminer</span>'
                    }
                </div>
                
                <div class="project-meta">
                    <div class="meta-item">
                        <i class="fas fa-calendar"></i>
                        <span>${project.year}</span>
                    </div>
                    <div class="meta-item">
                        <i class="fas fa-clock"></i>
                        <span>${project.lastUpdate}</span>
                    </div>
                    <div class="meta-item">
                        <i class="fas fa-user"></i>
                        <span>${project.account}</span>
                    </div>
                </div>
                
                ${project.featured ? '<div class="featured-badge">Projet phare</div>' : ''}
            </div>
        `;
    }).join('');
}

function renderTechnologies() {
    const grid = document.getElementById('technologiesGrid');
    if (!grid) return;

    const technologies = GitHubProjects.getTechnologies();
    const techCounts = {};

    // Compter les occurrences
    GitHubProjects.projects.forEach(project => {
        project.technologies.forEach(tech => {
            if (tech) {
                techCounts[tech] = (techCounts[tech] || 0) + 1;
            }
        });
    });

    // Trier par nombre d'occurrences
    const sortedTechs = technologies.sort((a, b) => techCounts[b] - techCounts[a]);

    grid.innerHTML = sortedTechs.map(tech => {
        const count = techCounts[tech];
        const percentage = Math.round((count / GitHubProjects.projects.length) * 100);
        
        return `
            <div class="tech-card">
                <div class="tech-name">${tech}</div>
                <div class="tech-stats">
                    <span class="tech-count">${count} projet${count > 1 ? 's' : ''}</span>
                    <span class="tech-percentage">${percentage}%</span>
                </div>
                <div class="tech-bar">
                    <div class="tech-bar-fill" style="width: ${percentage}%"></div>
                </div>
            </div>
        `;
    }).join('');
}

// Gestion des filtres
function initFilters() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Retirer active de tous les boutons du même groupe
            const group = button.closest('.filter-group');
            group.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');

            // Appliquer les filtres
            const filters = {
                category: document.querySelector('[data-filter].active')?.dataset.filter || 'all',
                year: document.querySelector('[data-year].active')?.dataset.year || 'all',
                status: document.querySelector('[data-status].active')?.dataset.status || 'all'
            };

            renderProjects(filters);
        });
    });
}

// Initialisation
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        renderProjects();
        renderTechnologies();
        initFilters();
    });
} else {
    renderProjects();
    renderTechnologies();
    initFilters();
}

