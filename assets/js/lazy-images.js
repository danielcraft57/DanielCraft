/**
 * Lazy load générique : img.dc-lazy-img[data-src] (+ picture source[data-srcset]).
 * Utilisé sur /echantillons/ et /bouquins/ (catalogues lourds).
 */
(function () {
  'use strict';

  var CLASS = 'dc-lazy-img';
  var ROOT_MARGIN = '320px 0px';

  function hydrate(img) {
    if (!img || img.getAttribute('data-lazy-done') === '1') return;
    var picture = img.closest('picture');
    if (picture) {
      picture.querySelectorAll('source[data-srcset]').forEach(function (source) {
        var srcset = source.getAttribute('data-srcset');
        if (srcset) {
          source.setAttribute('srcset', srcset);
          source.removeAttribute('data-srcset');
        }
      });
    }
    var src = img.getAttribute('data-src');
    if (src) {
      img.setAttribute('src', src);
      img.removeAttribute('data-src');
    }
    img.setAttribute('data-lazy-done', '1');
    img.classList.add('is-loaded');
  }

  function observe(scope) {
    var root = scope || document;
    var targets = root.querySelectorAll('img.' + CLASS + '[data-src]');
    if (!targets.length) return;

    if (!('IntersectionObserver' in window)) {
      targets.forEach(hydrate);
      return;
    }

    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          hydrate(entry.target);
          io.unobserve(entry.target);
        });
      },
      { root: null, rootMargin: ROOT_MARGIN, threshold: 0.01 }
    );

    targets.forEach(function (img) {
      io.observe(img);
    });
  }

  window.dcLazyImages = { hydrate: hydrate, observe: observe };

  function boot() {
    observe(document);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
