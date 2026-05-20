// Recherche client-side pour le blog DanielCraft
// Utilise les donnees JSON embarquees dans #blog-articles-data

(function () {
  const dataEl = document.getElementById('blog-articles-data');
  const input = document.getElementById('blogSearchInput');
  const clearBtn = document.getElementById('blogSearchClear');
  const grid = document.getElementById('blogArticlesGrid');
  const info = document.getElementById('blogSearchResultsInfo');
  const recommendationsSection = document.querySelector('.blog-recommendations-index');
  const seriesSection = document.querySelector('.blog-series-featured');
  const allSection = document.querySelector('.blog-all-articles');

  if (!dataEl || !input || !grid) return;

  let articles = [];
  try {
    const raw = dataEl.textContent || dataEl.innerText || '[]';
    articles = JSON.parse(raw);
  } catch (e) {
    console.warn('[BlogSearch] Impossible de parser les donnees articles', e);
  }

  if (!Array.isArray(articles) || !articles.length) return;

  // Map slug -> card DOM
  const cardsBySlug = {};
  grid.querySelectorAll('.article-card').forEach(card => {
    const href = card.getAttribute('href') || card.querySelector('a')?.getAttribute('href');
    const slugMatch = href && href.match(/([^/]+)\.html$|articles\/([^/]+)$/);
    let slug = null;
    if (slugMatch) {
      slug = slugMatch[1] || slugMatch[2];
    } else if (href) {
      slug = href.split('/').pop().replace(/\.html$/, '');
    }
    if (slug) {
      cardsBySlug[slug] = card;
    }
  });

  // Pre-normalisation pour recherche
  const normalizedArticles = articles.map(a => {
    const title = (a.title || '').toLowerCase();
    const excerpt = (a.excerpt || '').toLowerCase();
    const type = (a.type || '').toLowerCase();
    const tags = Array.isArray(a.tags) ? a.tags.join(' ').toLowerCase() : '';
    return { ...a, _norm: { title, excerpt, type, tags } };
  });

  function reorderCardsBySlugs(slugs) {
    if (!Array.isArray(slugs) || !slugs.length) return;
    const frag = document.createDocumentFragment();
    slugs.forEach((slug) => {
      const card = cardsBySlug[slug];
      if (card) frag.appendChild(card);
    });
    grid.appendChild(frag);
  }

  async function applyPersonalizationRanking() {
    if (!window.Personalization || typeof window.Personalization.getContext !== 'function') return;
    const ctx = await window.Personalization.getContext({ useCache: true });
    if (!ctx || !ctx.success || typeof window.Personalization.rankArticles !== 'function') return;
    const ranked = window.Personalization.rankArticles(normalizedArticles, ctx);
    const slugs = ranked.map((a) => a.slug).filter(Boolean);
    reorderCardsBySlugs(slugs);
    ranked.slice(0, 6).forEach((article) => {
      const card = cardsBySlug[article.slug];
      if (!card) return;
      const reasons = Array.isArray(article._personalizationReasons) ? article._personalizationReasons : [];
      if (!reasons.length) return;
      let badge = card.querySelector('.article-type');
      if (!badge) {
        badge = document.createElement('div');
        badge.className = 'article-type';
        card.insertBefore(badge, card.firstChild);
      }
      badge.textContent = 'Recommandé: ' + reasons.slice(0, 2).join(' + ');
    });
  }

  function computeScore(article, tokens) {
    const { title, excerpt, type, tags } = article._norm;
    let score = 0;
    for (const t of tokens) {
      if (!t) continue;
      if (title.includes(t)) score += 8;
      if (tags.includes(t)) score += 6;
      if (type.includes(t)) score += 4;
      if (excerpt.includes(t)) score += 3;
    }
    return score;
  }

  function applySearch(query) {
    const q = (query || '').trim().toLowerCase();

    if (!q || q.length < 2) {
      // Reset : tout afficher
      Object.values(cardsBySlug).forEach(card => {
        card.style.display = '';
        card.classList.remove('blog-card-highlight');
      });
      if (info) info.textContent = '';
      if (recommendationsSection) recommendationsSection.style.display = '';
      if (seriesSection) seriesSection.style.display = '';
      // Marge normale de la section "Tous les articles"
      if (allSection) {
        allSection.classList.remove('blog-all-articles--search-active');
      }
      return;
    }

    const tokens = q.split(/\s+/).filter(Boolean);
    const scored = normalizedArticles.map(a => ({
      article: a,
      score: computeScore(a, tokens),
    })).filter(x => x.score > 0);

    // Trier par score puis par date desc
    scored.sort((a, b) => {
      if (b.score !== a.score) return b.score - a.score;
      const da = (a.article.date || '').toString();
      const db = (b.article.date || '').toString();
      return db.localeCompare(da);
    });

    const keepSlugs = new Set(scored.map(x => x.article.slug));

    Object.entries(cardsBySlug).forEach(([slug, card]) => {
      if (keepSlugs.has(slug)) {
        card.style.display = '';
        // petite animation d'apparition
        card.classList.add('blog-card-highlight');
      } else {
        card.style.display = 'none';
        card.classList.remove('blog-card-highlight');
      }
    });

    if (info) {
      const count = scored.length;
      if (count === 0) {
        info.textContent = `Aucun résultat pour « ${query} ». Essaie un autre mot-clé.`;
      } else if (count === 1) {
        info.textContent = `1 résultat pour « ${query} ».`;
      } else {
        info.textContent = `${count} résultats pour « ${query} ».`;
      }
    }

    if (recommendationsSection) recommendationsSection.style.display = 'none';
    if (seriesSection) seriesSection.style.display = 'none';

    // Compacter la section "Tous les articles" quand une recherche est active
    if (allSection) {
      allSection.classList.add('blog-all-articles--search-active');
    }
  }

  let debounceId = null;
  input.addEventListener('input', (e) => {
    const value = e.target.value;
    if (debounceId) clearTimeout(debounceId);
    debounceId = setTimeout(() => applySearch(value), 160);
  });

  if (clearBtn) {
    clearBtn.addEventListener('click', () => {
      input.value = '';
      applySearch('');
      input.focus();
    });
  }

  // Focus automatique léger si hash #blog-search
  if (window.location.hash === '#blog-search') {
    setTimeout(() => input.focus(), 300);
  }

  applyPersonalizationRanking();
})();

