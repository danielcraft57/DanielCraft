/**
 * Catalogue prestations : tilt cartes, spotlight hero.
 */
(function () {
  'use strict';

  const page = document.querySelector('.page-prestations-catalog');
  const hero = document.querySelector('.prestations-search-hero--wow');
  if (!page && !hero) return;

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let tiltCard = null;

  function resetTiltCard(card) {
    if (!card) return;
    card.style.transform = '';
    card.classList.remove('is-tilt-active');
  }

  function initHeroSpotlight() {
    if (!hero || reduceMotion) return;
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

  function initTiltCards() {
    if (!page || reduceMotion || window.matchMedia('(max-width: 767px)').matches) return;
    const max = 8;

    page.addEventListener('mousemove', function (ev) {
      const card = ev.target.closest('.prestation-card[data-prestation-slug]');
      if (!card || card.classList.contains('is-search-hidden')) {
        if (tiltCard) {
          resetTiltCard(tiltCard);
          tiltCard = null;
        }
        return;
      }

      if (tiltCard !== card) {
        resetTiltCard(tiltCard);
        tiltCard = card;
      }

      const rect = card.getBoundingClientRect();
      const x = (ev.clientX - rect.left) / rect.width - 0.5;
      const y = (ev.clientY - rect.top) / rect.height - 0.5;
      card.style.transform =
        'perspective(920px) rotateX(' + -y * max + 'deg) rotateY(' + x * max + 'deg) translateY(-6px)';
      card.classList.add('is-tilt-active');
    });

    page.addEventListener('mouseleave', function () {
      resetTiltCard(tiltCard);
      tiltCard = null;
    });
  }

  function initChipRipple() {
    document.querySelectorAll('[data-prestations-search-chip]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        if (reduceMotion) return;
        btn.classList.remove('is-chip-pulse');
        void btn.offsetWidth;
        btn.classList.add('is-chip-pulse');
      });
    });
  }

  function initResultsPop() {
    const info = document.getElementById('prestationsSearchResultsInfo');
    if (!info || reduceMotion) return;
    document.addEventListener('prestations-search-applied', function () {
      if (!info.textContent) return;
      info.classList.remove('is-results-pop');
      void info.offsetWidth;
      info.classList.add('is-results-pop');
    });
  }

  initHeroSpotlight();
  initTiltCards();
  initChipRipple();
  initResultsPop();
})();
