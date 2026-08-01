/**
 * Recherche client-side — catalogue des livres (/livres)
 * Miroir de prestations-search.js (slugs, chips, ?q=, hero is-visible).
 */
(function () {
  'use strict';

  const input = document.getElementById('livresSearchInput');
  const clearBtn = document.getElementById('livresSearchClear');
  const wrapper = document.getElementById('livresSearchWrapper');
  const info = document.getElementById('livresSearchResultsInfo');
  const chips = document.querySelectorAll('[data-livres-search-chip]');
  const page = document.querySelector('.page-livres');
  const resultsWrap = document.getElementById('livresSearchResultsWrap');
  const resultsGrid = document.getElementById('livresSearchResults');
  const catalogBrowse = document.getElementById('livresCatalogBrowse');

  if (!input || !page || !resultsWrap || !resultsGrid || !catalogBrowse) return;

  const cards = Array.from(catalogBrowse.querySelectorAll('.livre-card[data-livre-slug]'));
  if (!cards.length) return;

  const searchIndex = cards.map((card) => {
    const slug = (card.getAttribute('data-livre-slug') || '').toLowerCase();
    const cat = (card.querySelector('[data-livre-cat]')?.getAttribute('data-livre-cat') || '').toLowerCase();
    const level = (card.getAttribute('data-livre-level') || '').toLowerCase();
    const keywords = (card.getAttribute('data-livre-keywords') || '').toLowerCase();
    const text = (card.textContent || '').toLowerCase().replace(/\s+/g, ' ').trim();
    return { card, slug, cat, level, keywords, text };
  });

  const uniqueBySlug = new Map();
  searchIndex.forEach((entry) => {
    if (!uniqueBySlug.has(entry.slug)) {
      uniqueBySlug.set(entry.slug, entry);
    }
  });

  const chipQueries = new Map();
  chips.forEach((btn) => {
    const chip = btn.getAttribute('data-livres-search-chip') || '';
    const query = (btn.getAttribute('data-livres-search-query') || '').trim();
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
    const hay = normalizeQuery(
      `${entry.slug} ${entry.cat} ${entry.level} ${entry.keywords} ${entry.text}`,
    );
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
      btn.classList.toggle('is-active', btn.getAttribute('data-livres-search-chip') === chip && chip !== '');
    });
  }

  function clearResultsGrid() {
    resultsGrid.innerHTML = '';
  }

  function renderResults(matched) {
    clearResultsGrid();
    matched.forEach((entry) => {
      const clone = entry.card.cloneNode(true);
      clone.classList.remove('is-search-hidden', 'is-search-match', 'livre-card--featured', 'is-wow-visible');
      clone.classList.add('livre-card--results');
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
        ['javascript-les-bases', 'python-les-bases', 'ia-les-bases'].forEach((slug) => {
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
        info.textContent = '';
        info.appendChild(document.createTextNode('Aucun résultat — voici quelques livres populaires. '));
        const link = document.createElement('a');
        link.href = '/contact';
        link.textContent = 'Une question ? →';
        info.appendChild(link);
      } else if (visibleCount === 1) {
        info.textContent = '1 livre trouvé';
      } else {
        info.textContent = `${visibleCount} livres trouvés`;
      }
    }
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
      applySearch();
      input.focus();
    });
  }

  chips.forEach((btn) => {
    btn.addEventListener('click', () => {
      const chip = btn.getAttribute('data-livres-search-chip') || '';
      const query = chipQueries.get(chip) || '';
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
    if (e.key === '/' && !e.ctrlKey && !e.metaKey && !e.altKey) {
      const t = e.target;
      if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.isContentEditable)) return;
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

  try {
    const params = new URLSearchParams(window.location.search);
    const q = params.get('q');
    if (q) {
      input.value = q;
      syncChipFromInput();
    }
  } catch (_) {
    /* ignore */
  }

  applySearch();

  requestAnimationFrame(() => {
    const hero = document.querySelector('.prestations-search-hero');
    if (hero) hero.classList.add('is-visible');
  });
})();
