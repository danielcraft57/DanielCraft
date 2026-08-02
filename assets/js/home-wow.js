/**
 * Accueil : stagger reveal bandes + tilt optionnel (nos-offres).
 */
(function () {
  'use strict';

  if (!document.querySelector('.home-hero--wow') && !document.querySelector('.home-offers')) return;

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function initTiltCards() {
    if (reduceMotion) return;
    document.querySelectorAll('[data-home-tilt]').forEach(function (card) {
      const max = 10;
      card.addEventListener('mousemove', function (ev) {
        const rect = card.getBoundingClientRect();
        const x = (ev.clientX - rect.left) / rect.width - 0.5;
        const y = (ev.clientY - rect.top) / rect.height - 0.5;
        card.style.transform =
          'perspective(900px) rotateX(' + -y * max + 'deg) rotateY(' + x * max + 'deg) translateY(-6px)';
        card.classList.add('is-tilt-active');
      });
      card.addEventListener('mouseleave', function () {
        card.style.transform = '';
        card.classList.remove('is-tilt-active');
      });
    });
  }

  function initHeroParallax() {
    if (reduceMotion) return;
    if (window.matchMedia('(max-width: 959px)').matches) return;
    const media = document.querySelector('.home-split__media img');
    if (!media) return;
    window.addEventListener(
      'scroll',
      function () {
        const y = window.scrollY;
        if (y > 700) return;
        media.style.transform = 'translateY(' + y * 0.05 + 'px)';
      },
      { passive: true },
    );
  }

  function initStagger() {
    const blocks = document.querySelectorAll('.home-stagger');
    if (!blocks.length) return;

    if (window.matchMedia('(max-width: 767px)').matches || reduceMotion) {
      blocks.forEach(function (el) {
        el.classList.add('is-visible');
      });
      return;
    }

    const io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -40px 0px' },
    );
    blocks.forEach(function (el) {
      io.observe(el);
    });
  }

  initTiltCards();
  initHeroParallax();
  initStagger();
})();
