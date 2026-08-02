/**
 * Recherche client-side — catalogue des offres (/nos-offres)
 * Mode filtre : grille plate dédoublonnée (sans catégories ni bloc « 3 offres »).
 */
(function () {
  'use strict';

  const input = document.getElementById('prestationsSearchInput');
  const clearBtn = document.getElementById('prestationsSearchClear');
  const wrapper = document.getElementById('prestationsSearchWrapper');
  const info = document.getElementById('prestationsSearchResultsInfo');
  const chips = document.querySelectorAll('[data-prestations-search-chip]');
  const page = document.querySelector('.page-prestations-catalog');
  const resultsWrap = document.getElementById('prestationsSearchResultsWrap');
  const resultsGrid = document.getElementById('prestationsSearchResults');
  const catalogBrowse = document.getElementById('prestationsCatalogBrowse');

  if (!input || !page || !resultsWrap || !resultsGrid || !catalogBrowse) return;

  const cards = Array.from(catalogBrowse.querySelectorAll('.prestation-card[data-prestation-slug]'));
  if (!cards.length) return;

  const searchIndex = cards.map((card) => {
    const slug = (card.getAttribute('data-prestation-slug') || '').toLowerCase();
    const cat = (card.querySelector('.prestation-card-visual')?.getAttribute('data-prestation-cat') || '').toLowerCase();
    const text = (card.textContent || '').toLowerCase().replace(/\s+/g, ' ').trim();
    return { card, slug, cat, text };
  });

  /** Première carte par slug (évite les doublons featured + catégorie). */
  const uniqueBySlug = new Map();
  searchIndex.forEach((entry) => {
    if (!uniqueBySlug.has(entry.slug)) {
      uniqueBySlug.set(entry.slug, entry);
    }
  });

  const chipQueries = new Map();
  chips.forEach((btn) => {
    const chip = btn.getAttribute('data-prestations-search-chip') || '';
    const query = (btn.getAttribute('data-prestations-search-query') || '').trim();
    if (chip && query) chipQueries.set(chip, query);
  });

  let activeChip = '';

  function normalizeQuery(q) {
    return (q || '').toLowerCase().trim().normalize('NFD').replace(/\p{Diacritic}/gu, '');
  }

  function tokensFromQuery(q) {
    const base = normalizeQuery(q);
    if (!base) return [];
    return base.split(/\s+/).filter(Boolean);
  }

  function cardMatchesText(entry, tokens) {
    if (!tokens.length) return true;
    const hay = normalizeQuery(`${entry.slug} ${entry.cat} ${entry.text}`);
    return tokens.every((t) => hay.includes(t));
  }

  function syncChipFromInput() {
    const normalized = normalizeQuery(input.value);
    let next = '';
    chipQueries.forEach((query, chip) => {
      if (normalizeQuery(query) === normalized) next = chip;
    });
    activeChip = next;
    setChipActive(activeChip);
  }

  function setChipActive(chip) {
    chips.forEach((btn) => {
      btn.classList.toggle('is-active', btn.getAttribute('data-prestations-search-chip') === chip && chip !== '');
    });
  }

  function clearResultsGrid() {
    resultsGrid.innerHTML = '';
  }

  function renderResults(matched) {
    clearResultsGrid();
    matched.forEach((entry, index) => {
      const clone = entry.card.cloneNode(true);
      clone.classList.remove('is-search-hidden', 'is-search-match', 'prestation-card--featured', 'is-wow-visible');
      clone.classList.add('prestation-card--results');
      clone.setAttribute('data-prestation-results', 'true');
      resultsGrid.appendChild(clone);
    });
  }

  function syncSearchUrl(raw) {
    try {
      const url = new URL(window.location.href);
      const q = (raw || '').trim();
      if (q.length > 0) {
        url.searchParams.set('q', q);
      } else {
        url.searchParams.delete('q');
      }
      const next = url.pathname + url.search + url.hash;
      if (next !== window.location.pathname + window.location.search + window.location.hash) {
        window.history.replaceState(null, '', next);
      }
    } catch (_) {
      /* ignore */
    }
  }

  function applySearch() {
    const raw = input.value;
    const textTokens = tokensFromQuery(raw);
    const filtering = textTokens.length > 0;
    let visibleCount = 0;

    syncSearchUrl(raw);
    page.classList.toggle('is-catalog-filtering', filtering);

    if (filtering) {
      const matched = [];
      uniqueBySlug.forEach((entry) => {
        if (cardMatchesText(entry, textTokens)) {
          matched.push(entry);
        }
      });
      visibleCount = matched.length;
      if (visibleCount === 0) {
        const popularSlugs = ['site-vitrine', 'visibilite-complete', 'repondeur-intelligent'];
        popularSlugs.forEach((slug) => {
          const entry = uniqueBySlug.get(slug);
          if (entry) matched.push(entry);
        });
      }
      renderResults(matched);
      resultsWrap.hidden = false;
      catalogBrowse.hidden = true;
    } else {
      clearResultsGrid();
      resultsWrap.hidden = true;
      catalogBrowse.hidden = false;
      searchIndex.forEach((entry) => {
        entry.card.classList.remove('is-search-hidden', 'is-search-match');
      });
    }

    if (clearBtn) {
      clearBtn.hidden = !(raw.length > 0);
    }
    if (wrapper) {
      wrapper.classList.toggle('is-typing', raw.length > 0);
    }

    if (info) {
      if (!filtering) {
        info.textContent = '';
      } else if (visibleCount === 0) {
        info.textContent = 'Aucun résultat — voici nos prestations les plus demandées. ';
        const link = document.createElement('a');
        link.href = '/contact';
        link.textContent = 'Parler de mon projet →';
        info.textContent = '';
        info.appendChild(document.createTextNode('Aucun résultat — voici nos prestations les plus demandées. '));
        info.appendChild(link);
      } else if (visibleCount === 1) {
        info.textContent = '1 prestation trouvée';
      } else {
        info.textContent = `${visibleCount} prestations trouvées`;
      }
    }

    document.dispatchEvent(
      new CustomEvent('prestations-search-applied', {
        detail: { visibleCount, activeChip, filtering },
      }),
    );
  }

  let debounceTimer;
  input.addEventListener('input', () => {
    syncChipFromInput();
    window.clearTimeout(debounceTimer);
    debounceTimer = window.setTimeout(applySearch, 120);
  });

  if (clearBtn) {
    clearBtn.addEventListener('click', () => {
      input.value = '';
      activeChip = '';
      setChipActive('');
      input.focus();
      applySearch();
    });
  }

  chips.forEach((btn) => {
    btn.addEventListener('click', () => {
      const chip = btn.getAttribute('data-prestations-search-chip') || '';
      const query = (btn.getAttribute('data-prestations-search-query') || '').trim();
      if (activeChip === chip && normalizeQuery(input.value) === normalizeQuery(query)) {
        input.value = '';
        activeChip = '';
        setChipActive('');
      } else {
        input.value = query;
        activeChip = chip;
        setChipActive(chip);
      }
      applySearch();
      input.focus();
    });
  });

  const form = input.closest('form');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      applySearch();
    });
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === '/' && document.activeElement !== input && !/input|textarea|select/i.test((document.activeElement || {}).tagName || '')) {
      e.preventDefault();
      input.focus();
    }
    if (e.key === 'Escape' && document.activeElement === input) {
      input.value = '';
      activeChip = '';
      setChipActive('');
      applySearch();
      input.blur();
    }
  });

  const params = new URLSearchParams(window.location.search);
  const qParam = params.get('q');
  if (qParam) {
    input.value = qParam;
    syncChipFromInput();
    applySearch();
  }

  requestAnimationFrame(() => {
    const hero = document.querySelector('.prestations-search-hero');
    if (hero) hero.classList.add('is-visible');
  });
})();
