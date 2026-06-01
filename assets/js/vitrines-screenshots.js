/**
 * Fiches vitrines : aperçu des captures longues — léger défilement automatique
 * dans le cadre (une fois à l'entrée dans le viewport), puis retour en haut.
 * Respecte prefers-reduced-motion.
 */
(function () {
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce) return;

  function easeInOutQuad(t) {
    return t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
  }

  function runScrollDemo(vp) {
    const max = vp.scrollHeight - vp.clientHeight;
    if (max <= 4) return;

    const durationDown = Math.min(10000, 3200 + max * 0.35);
    const start = performance.now();

    function tick(now) {
      const elapsed = now - start;
      const p = Math.min(1, elapsed / durationDown);
      vp.scrollTop = max * easeInOutQuad(p);
      if (p < 1) {
        requestAnimationFrame(tick);
        return;
      }
      window.setTimeout(() => {
        vp.scrollTo({ top: 0, behavior: 'smooth' });
      }, 400);
    }

    requestAnimationFrame(tick);
  }

  document.querySelectorAll('[data-vitrine-auto-scroll]').forEach((vp) => {
    let done = false;
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (!e.isIntersecting || done) return;
          done = true;
          io.disconnect();
          window.setTimeout(() => runScrollDemo(vp), 300);
        });
      },
      { root: null, threshold: 0.2 }
    );
    io.observe(vp);
  });
})();
