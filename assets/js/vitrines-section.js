/**
 * Sections catalogue vitrines (accueil #vitrines + page /vitrines/) :
 * filtres secteur + défilement auto des captures au survol.
 */
(function () {
  document.querySelectorAll('[data-vitrines-root]').forEach((root) => {
    initVitrinesCatalogRoot(root);
  });

  function initVitrinesCatalogRoot(root) {
    const grid = root.querySelector('#vitrinesGrid');
    if (!grid) return;

    const featuredWrap = root.querySelector('.vitrines-filter--featured');
    const extendedWrap = root.querySelector('.vitrines-filter--extended');
    const select = root.querySelector('#vitrineFilterSelect');
    const moreBtn = root.querySelector('#vitrineFilterMore');

    function applyFilter(cat) {
      grid.querySelectorAll('.vitrine-card[data-vitrine-cat]').forEach((card) => {
        const c = card.getAttribute('data-vitrine-cat') || '';
        const show = cat === 'all' || c === cat;
        card.hidden = !show;
      });
      if (select && select.value !== cat) select.value = cat;
      root.querySelectorAll('.vitrines-filter-btn').forEach((b) => {
        b.classList.toggle('active', (b.getAttribute('data-vitrine-filter') || 'all') === cat);
      });
    }

    function onFilterClick(btn) {
      const cat = btn.getAttribute('data-vitrine-filter') || 'all';
      applyFilter(cat);
    }

    root.querySelectorAll('.vitrines-filter-btn').forEach((btn) => {
      btn.addEventListener('click', () => onFilterClick(btn));
    });

    if (select) {
      select.addEventListener('change', () => applyFilter(select.value || 'all'));
    }

    if (moreBtn && extendedWrap) {
      moreBtn.addEventListener('click', () => {
        const open = extendedWrap.hidden;
        extendedWrap.hidden = !open;
        moreBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
        moreBtn.textContent = open ? 'Masquer les secteurs' : 'Voir plus de secteurs';
      });
    }

    if (featuredWrap) {
      featuredWrap.addEventListener('click', (e) => {
        const btn = e.target.closest('.vitrines-filter-btn');
        if (btn) onFilterClick(btn);
      });
    }

    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    function easeOutCubic(t) {
      return 1 - Math.pow(1 - t, 3);
    }

    grid.querySelectorAll('.vitrine-card').forEach((card) => {
      const pane = card.querySelector('[data-vitrine-card-hover-scroll]');
      if (!pane) return;

      let rafId = 0;

      function stopAnim() {
        if (rafId) cancelAnimationFrame(rafId);
        rafId = 0;
      }

      function scrollToY(target, durationMs) {
        stopAnim();
        const startY = pane.scrollTop;
        const dy = target - startY;
        if (Math.abs(dy) < 2) {
          pane.scrollTop = target;
          return;
        }
        const t0 = performance.now();

        function frame(now) {
          const u = Math.min(1, (now - t0) / durationMs);
          pane.scrollTop = startY + dy * easeOutCubic(u);
          if (u < 1) rafId = requestAnimationFrame(frame);
          else rafId = 0;
        }

        rafId = requestAnimationFrame(frame);
      }

      card.addEventListener('mouseenter', () => {
        if (reduceMotion) return;
        const max = pane.scrollHeight - pane.clientHeight;
        if (max <= 4) return;
        // Lecture lente de la capture tablette au survol (un poil plus vive)
        const duration = Math.min(72000, 34000 + max * 4.2);
        scrollToY(max, duration);
      });

      card.addEventListener('mouseleave', () => {
        stopAnim();
        if (reduceMotion) {
          pane.scrollTop = 0;
          return;
        }
        scrollToY(0, 3800);
      });
    });
  }
})();
