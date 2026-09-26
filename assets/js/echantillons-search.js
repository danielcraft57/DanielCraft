/**
 * Page /echantillons/ : recherche, chips secteurs, groupes par metier, shuffle journalier.
 * ADN aligne /bouquins + /nos-offres.
 */
(function () {
  'use strict';

  var catalog = document.querySelector('[data-echantillons-catalog]');
  if (!catalog) return;

  var hero = document.querySelector('.echantillons-search-hero');
  if (hero) hero.classList.add('is-visible');

  var grids = catalog.querySelectorAll('[data-echantillons-daily-shuffle]');
  var input = document.getElementById('echantillonsSearchInput');
  var clearBtn = document.getElementById('echantillonsSearchClear');
  var info = document.getElementById('echantillonsSearchResultsInfo');
  var form = document.querySelector('.echantillons-search-form');
  var chips = document.querySelectorAll('[data-echantillons-filter]');
  var chipsMore = document.getElementById('echantillonsChipsMore');
  var activeFilter = 'all';
  var query = '';

  function daySeed() {
    var d = new Date();
    return d.getFullYear() * 10000 + (d.getMonth() + 1) * 100 + d.getDate();
  }

  function mulberry32(a) {
    return function () {
      a |= 0;
      a = (a + 0x6d2b79f5) | 0;
      var t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  function shuffleDaily(container, salt) {
    if (!container) return;
    var cards = Array.prototype.slice.call(container.querySelectorAll('.vitrine-card'));
    if (cards.length < 2) return;
    var rand = mulberry32((daySeed() ^ 0xec4a) + (salt || 0));
    for (var i = cards.length - 1; i > 0; i--) {
      var j = Math.floor(rand() * (i + 1));
      var tmp = cards[i];
      cards[i] = cards[j];
      cards[j] = tmp;
    }
    cards.forEach(function (card, idx) {
      card.style.setProperty('--reveal-delay', Math.min(idx * 40, 400) + 'ms');
      container.appendChild(card);
    });
  }

  function normalize(s) {
    return (s || '')
      .toLowerCase()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .trim();
  }

  function syncGroups() {
    catalog.querySelectorAll('[data-echantillons-group]').forEach(function (group) {
      var visible = group.querySelector('.vitrine-card:not([hidden])');
      group.hidden = !visible;
    });
  }

  function applyFilters() {
    var cards = catalog.querySelectorAll('.vitrine-card');
    var q = normalize(query);
    var shown = 0;
    cards.forEach(function (card) {
      var cat = card.getAttribute('data-vitrine-cat') || '';
      var hay = normalize(card.getAttribute('data-vitrine-search') || card.textContent || '');
      var matchCat = activeFilter === 'all' || cat === activeFilter;
      var matchQ = !q || hay.indexOf(q) !== -1;
      var show = matchCat && matchQ;
      card.hidden = !show;
      if (show) shown += 1;
    });
    syncGroups();
    var page = document.querySelector('.page-echantillons');
    if (page) {
      page.classList.toggle('is-catalog-filtering', !!(q || activeFilter !== 'all'));
      page.classList.toggle('is-catalog-grouped-focus', activeFilter !== 'all' && !q);
    }
    if (info) {
      if (q || activeFilter !== 'all') {
        info.textContent =
          shown === 0
            ? 'Aucun echantillon pour cette recherche.'
            : shown + ' echantillon' + (shown > 1 ? 's' : '') + ' trouve' + (shown > 1 ? 's' : '') + '.';
      } else {
        info.textContent = '';
      }
    }
    if (window.dcLazyImages && typeof window.dcLazyImages.observe === 'function') {
      window.dcLazyImages.observe(catalog);
    }
  }

  function setFilter(cat) {
    activeFilter = cat || 'all';
    chips.forEach(function (chip) {
      var on = (chip.getAttribute('data-echantillons-filter') || '') === activeFilter;
      chip.classList.toggle('is-active', on);
      chip.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
    applyFilters();
  }

  grids.forEach(function (grid, i) {
    shuffleDaily(grid, i * 97);
  });

  chips.forEach(function (chip) {
    chip.addEventListener('click', function () {
      setFilter(chip.getAttribute('data-echantillons-filter') || 'all');
    });
  });

  if (chipsMore) {
    chipsMore.addEventListener('click', function () {
      var open = chipsMore.getAttribute('aria-expanded') === 'true';
      var next = !open;
      chipsMore.setAttribute('aria-expanded', next ? 'true' : 'false');
      document.querySelectorAll('.echantillons-search-hero .is-chip-overflow').forEach(function (el) {
        el.hidden = !next;
      });
      var label = chipsMore.querySelector('span');
      if (label) label.textContent = next ? 'Moins' : 'Plus';
      var icon = chipsMore.querySelector('i');
      if (icon) {
        icon.classList.toggle('fa-plus', !next);
        icon.classList.toggle('fa-minus', next);
      }
    });
  }

  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      query = input ? input.value : '';
      applyFilters();
    });
  }

  if (input) {
    input.addEventListener('input', function () {
      query = input.value;
      if (clearBtn) clearBtn.hidden = !query;
      applyFilters();
    });
  }

  if (clearBtn) {
    clearBtn.addEventListener('click', function () {
      if (input) input.value = '';
      query = '';
      clearBtn.hidden = true;
      applyFilters();
      if (input) input.focus();
    });
  }

  document.addEventListener('keydown', function (e) {
    if (e.key === '/' && document.activeElement !== input) {
      var tag = (document.activeElement && document.activeElement.tagName) || '';
      if (tag === 'INPUT' || tag === 'TEXTAREA' || (document.activeElement && document.activeElement.isContentEditable)) {
        return;
      }
      e.preventDefault();
      if (input) input.focus();
    }
  });

  applyFilters();
})();
