/**
 * Sections catalogue vitrines (accueil #vitrines + page /vitrines/) :
 * filtres secteur + défilement auto des captures au survol (ascenseurs masqués en CSS).
 */
(function () {
  document.querySelectorAll('[data-vitrines-root]').forEach((root) => {
    initVitrinesCatalogRoot(root);
  });

  function initVitrinesCatalogRoot(root) {
    const filterWrap = root.querySelector('.vitrines-filter');
    const grid = root.querySelector('#vitrinesGrid');
    if (!filterWrap || !grid) return;

    function applyFilter(cat) {
      grid.querySelectorAll('.vitrine-card[data-vitrine-cat]').forEach((card) => {
        const c = card.getAttribute('data-vitrine-cat') || '';
        const show = cat === 'all' || c === cat;
        card.hidden = !show;
      });
    }

    filterWrap.addEventListener('click', (e) => {
      const btn = e.target.closest('.vitrines-filter-btn');
      if (!btn) return;
      const cat = btn.getAttribute('data-vitrine-filter') || 'all';
      filterWrap.querySelectorAll('.vitrines-filter-btn').forEach((b) => {
        b.classList.toggle('active', b === btn);
      });
      applyFilter(cat);
    });

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
        const duration = Math.min(9000, 2200 + max * 0.45);
        scrollToY(max, duration);
      });

      card.addEventListener('mouseleave', () => {
        stopAnim();
        pane.scrollTop = 0;
      });
    });
  }
})();
