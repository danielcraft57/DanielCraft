/**
 * Blog index : spotlight hero, entrée animée.
 */
(function () {
  'use strict';

  const hero = document.querySelector('.blog-search-hero--wow');
  if (!hero) return;

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function initHeroSpotlight() {
    if (reduceMotion) return;
    hero.addEventListener(
      'mousemove',
      function (ev) {
        const rect = hero.getBoundingClientRect();
        const x = ((ev.clientX - rect.left) / rect.width) * 100;
        const y = ((ev.clientY - rect.top) / rect.height) * 100;
        hero.style.setProperty('--spot-x', x + '%');
        hero.style.setProperty('--spot-y', y + '%');
        hero.classList.add('is-spotlight');
      },
      { passive: true },
    );
    hero.addEventListener('mouseleave', function () {
      hero.classList.remove('is-spotlight');
    });
  }

  requestAnimationFrame(function () {
    hero.classList.add('is-visible');
  });

  initHeroSpotlight();
})();
