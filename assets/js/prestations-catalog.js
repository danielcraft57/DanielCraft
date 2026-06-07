/**
 * Catalogue prestations : pré-sélection du service dans le wizard contact (?service=slug).
 */
(function () {
  'use strict';

  const params = new URLSearchParams(window.location.search);
  const service = params.get('service');
  if (!service) return;

  document.querySelectorAll('.prestation-card .service-cta, .service-card .service-cta').forEach((link) => {
    try {
      const url = new URL(link.getAttribute('href') || '', window.location.origin);
      if (url.hash === '#contact' || url.pathname === '/' && url.hash === '#contact') {
        url.searchParams.set('service', service);
        link.setAttribute('href', url.pathname + url.search + url.hash);
      }
    } catch {
      /* ignore */
    }
  });
})();
