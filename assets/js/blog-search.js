// Recherche client-side pour le blog DanielCraft
// Utilise les donnees JSON embarquees dans #blog-articles-data

(function () {
  'use strict';

  const dataEl = document.getElementById('blog-articles-data');
  const input = document.getElementById('blogSearchInput');
  const clearBtn = document.getElementById('blogSearchClear');
  const wrapper = document.getElementById('blogSearchWrapper');
  const grid = document.getElementById('blogArticlesGrid');
  const info = document.getElementById('blogSearchResultsInfo');
  const chips = document.querySelectorAll('[data-blog-search-query]');
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

  const cardsBySlug = {};
  grid.querySelectorAll('.article-card').forEach((card) => {
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

  function fold(s) {
    return (s || '')
      .toLowerCase()
      .normalize('NFD')
      .replace(/\p{Diacritic}/gu, '');
  }

  const normalizedArticles = articles.map((a) => {
    const title = fold(a.title || '');
    const excerpt = fold(a.excerpt || '');
    const type = fold(a.type || '');
    const tags = Array.isArray(a.tags) ? fold(a.tags.join(' ')) : '';
    const series = fold(a.series || '');
    const slug = fold(a.slug || '');
    return { ...a, _norm: { title, excerpt, type, tags, series, slug } };
  });

  function normalizeQuery(q) {
    return fold(q).trim();
  }

  function syncChipActive() {
    const normalized = normalizeQuery(input.value);
    chips.forEach((btn) => {
      const query = normalizeQuery(btn.getAttribute('data-blog-search-query') || '');
      btn.classList.toggle('is-active', query !== '' && query === normalized);
    });
  }

  function popResultsInfo() {
    if (!info || !info.textContent) return;
    info.classList.remove('is-results-pop');
    void info.offsetWidth;
    info.classList.add('is-results-pop');
  }

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
    const { title, excerpt, type, tags, series, slug } = article._norm;
    let score = 0;
    for (const t of tokens) {
      if (!t) continue;
      if (title.includes(t)) score += 8;
      if (tags.includes(t)) score += 6;
      if (series.includes(t)) score += 6;
      if (slug.includes(t)) score += 5;
      if (type.includes(t)) score += 4;
      if (excerpt.includes(t)) score += 3;
      // Raccourcis pratiques pour la serie IA
      if (t === 'ia' && (slug.includes('ia-') || tags.includes('ia') || series.includes('ia-'))) score += 4;
      if ((t === 'chatgpt' || t === 'claude' || t === 'gemini' || t === 'n8n' || t === 'prompt' || t === 'prompts' || t === 'agent' || t === 'agents') &&
          (title.includes(t) || tags.includes(t) || slug.includes(t) || series.includes(t) || excerpt.includes(t))) {
        score += 3;
      }
    }
    return score;
  }

  function applySearch(query) {
    const q = (query || '').trim();
    const normalized = normalizeQuery(q);
    const tokens = normalized.split(/\s+/).filter(Boolean);

    if (clearBtn) {
      clearBtn.hidden = q.length === 0;
    }
    if (wrapper) {
      wrapper.classList.toggle('is-typing', q.length > 0);
    }

    if (!normalized || normalized.length < 2) {
      Object.values(cardsBySlug).forEach((card) => {
        card.style.display = '';
        card.classList.remove('blog-card-highlight');
      });
      if (info) info.textContent = '';
      if (recommendationsSection) recommendationsSection.style.display = '';
      if (seriesSection) seriesSection.style.display = '';
      if (allSection) {
        allSection.classList.remove('blog-all-articles--search-active');
      }
      syncChipActive();
      return;
    }

    const scored = normalizedArticles
      .map((a) => ({
        article: a,
        score: computeScore(a, tokens),
      }))
      .filter((x) => x.score > 0);

    scored.sort((a, b) => {
      if (b.score !== a.score) return b.score - a.score;
      const da = (a.article.date || '').toString();
      const db = (b.article.date || '').toString();
      return db.localeCompare(da);
    });

    const keepSlugs = new Set(scored.map((x) => x.article.slug));

    Object.entries(cardsBySlug).forEach(([slug, card]) => {
      if (keepSlugs.has(slug)) {
        card.style.display = '';
        card.classList.add('blog-card-highlight');
      } else {
        card.style.display = 'none';
        card.classList.remove('blog-card-highlight');
      }
    });

    if (info) {
      const count = scored.length;
      if (count === 0) {
        info.textContent = `Aucun résultat pour « ${q} ». Essaie un autre mot-clé.`;
      } else if (count === 1) {
        info.textContent = `1 résultat pour « ${q} ».`;
      } else {
        info.textContent = `${count} résultats pour « ${q} ».`;
      }
      popResultsInfo();
    }

    if (recommendationsSection) recommendationsSection.style.display = 'none';
    if (seriesSection) seriesSection.style.display = 'none';
    if (allSection) {
      allSection.classList.add('blog-all-articles--search-active');
    }

    syncChipActive();
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

  chips.forEach((btn) => {
    btn.addEventListener('click', () => {
      const query = (btn.getAttribute('data-blog-search-query') || '').trim();
      const isActive = btn.classList.contains('is-active');
      input.value = isActive ? '' : query;
      applySearch(input.value);
      input.focus();
    });
  });

  document.addEventListener('keydown', (e) => {
    if (
      e.key === '/' &&
      document.activeElement !== input &&
      !/input|textarea|select/i.test((document.activeElement || {}).tagName || '')
    ) {
      e.preventDefault();
      input.focus();
    }
    if (e.key === 'Escape' && document.activeElement === input) {
      input.value = '';
      applySearch('');
      input.blur();
    }
  });

  if (window.location.hash === '#blog-search') {
    setTimeout(() => input.focus(), 300);
  }

  applyPersonalizationRanking();
})();
