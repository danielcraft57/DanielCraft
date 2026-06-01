/**
 * Fiche vitrine : classe d’amélioration progressive (hover appareils, etc.).
 * Les révélations au scroll restent gérées par main.js (scroll-reveal).
 */
(function () {
  var root = document.querySelector('.vitrine-detail-root');
  if (!root) return;
  root.classList.add('vitrine-detail--enhanced');
})();
