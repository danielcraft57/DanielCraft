/**
 * Catalogue /nos-offres : hub catégories, budget slider, overflow chips/sidebar.
 */
(function () {
  'use strict';

  var page = document.querySelector('.page-nos-offres');
  if (!page) return;

  var hub = document.getElementById('prestations-cat-hub');
  var productsWrap = document.getElementById('prestationsCategoryProducts');
  var backBtn = document.getElementById('prestationsBackHub');
  var sections = Array.from(document.querySelectorAll('[data-category-section]'));
  var budgetRange = document.getElementById('prestationsBudgetRange');
  var budgetValue = document.getElementById('prestationsBudgetValue');

  function setSidebarActive(nav) {
    document.querySelectorAll('[data-cat-nav]').forEach(function (a) {
      a.classList.toggle('is-active', a.getAttribute('data-cat-nav') === nav);
    });
  }

  function showHub() {
    if (hub) hub.hidden = false;
    if (productsWrap) productsWrap.hidden = true;
    sections.forEach(function (s) {
      s.hidden = true;
    });
    setSidebarActive('hub');
    applyBudgetFilter();
  }

  function showCategory(cid) {
    if (!cid || cid === 'hub') {
      showHub();
      return;
    }
    if (hub) hub.hidden = true;
    if (productsWrap) productsWrap.hidden = false;
    sections.forEach(function (s) {
      var match = s.getAttribute('data-category-section') === cid;
      s.hidden = !match;
    });
    setSidebarActive(cid);
    applyBudgetFilter();
    var target = document.getElementById(cid);
    if (target) {
      try {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      } catch (e) {}
    }
  }

  function applyBudgetFilter() {
    if (!budgetRange) return;
    var max = parseInt(budgetRange.value, 10) || 99999;
    if (budgetValue) budgetValue.textContent = max + ' €';
    budgetRange.setAttribute('aria-valuenow', String(max));
    document.querySelectorAll('.prestation-card[data-price-eur]').forEach(function (card) {
      var price = parseInt(card.getAttribute('data-price-eur') || '0', 10) || 0;
      var over = price > max;
      card.classList.toggle('is-budget-hidden', over);
      if (over) card.setAttribute('hidden', '');
      else card.removeAttribute('hidden');
    });
  }

  document.querySelectorAll('[data-cat-frame]').forEach(function (el) {
    el.addEventListener('click', function (ev) {
      ev.preventDefault();
      showCategory(el.getAttribute('data-cat-frame') || '');
    });
  });

  document.querySelectorAll('[data-cat-nav]').forEach(function (el) {
    el.addEventListener('click', function (ev) {
      var nav = el.getAttribute('data-cat-nav') || '';
      if (nav === 'hub' || sections.some(function (s) { return s.getAttribute('data-category-section') === nav; })) {
        ev.preventDefault();
        showCategory(nav);
      }
    });
  });

  if (backBtn) {
    backBtn.addEventListener('click', function () {
      showHub();
      if (hub) {
        try {
          hub.scrollIntoView({ behavior: 'smooth', block: 'start' });
        } catch (e) {}
      }
    });
  }

  if (budgetRange) {
    budgetRange.addEventListener('input', applyBudgetFilter);
    applyBudgetFilter();
  }

  // Overflow chips
  var chipsMore = document.getElementById('prestationsChipsMore');
  var chipsRoot = document.querySelector('[data-chips-overflow]');
  if (chipsMore && chipsRoot) {
    chipsMore.addEventListener('click', function () {
      var open = chipsRoot.classList.toggle('is-chips-expanded');
      chipsMore.setAttribute('aria-expanded', open ? 'true' : 'false');
      chipsRoot.querySelectorAll('.is-chip-overflow').forEach(function (chip) {
        chip.hidden = !open;
      });
      var label = chipsMore.querySelector('span');
      var icon = chipsMore.querySelector('i');
      if (label) label.textContent = open ? 'Moins' : 'Plus';
      if (icon) {
        icon.className = open ? 'fas fa-minus' : 'fas fa-plus';
      }
    });
  }

  // Overflow sidebar (montre 5 items + bouton)
  var sideList = document.getElementById('prestationsSidebarList');
  var sideMore = document.getElementById('prestationsSidebarMore');
  if (sideList && sideMore) {
    var items = Array.from(sideList.children);
    var limit = 5;
    if (items.length > limit) {
      items.forEach(function (li, i) {
        if (i >= limit) li.classList.add('is-side-overflow');
      });
      sideMore.hidden = false;
      sideList.classList.add('is-side-collapsed');
      sideMore.addEventListener('click', function () {
        var open = sideList.classList.toggle('is-side-expanded');
        sideList.classList.toggle('is-side-collapsed', !open);
        var span = sideMore.querySelector('span');
        var icon = sideMore.querySelector('i');
        if (span) span.textContent = open ? 'Voir moins' : 'Voir plus';
        if (icon) icon.className = open ? 'fas fa-chevron-up' : 'fas fa-chevron-down';
      });
    }
  }

  // Deep link #packs etc.
  var hash = (window.location.hash || '').replace(/^#/, '');
  if (hash && sections.some(function (s) { return s.getAttribute('data-category-section') === hash; })) {
    showCategory(hash);
  } else {
    showHub();
  }
})();
