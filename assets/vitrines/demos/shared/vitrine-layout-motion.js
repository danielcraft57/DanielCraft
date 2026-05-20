/**
 * IntersectionObserver pour .vt-reveal — sections majeures au scroll.
 */
(function () {
  "use strict";

  var reduce =
    typeof window.matchMedia === "function" &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function reveal(el) {
    el.classList.add("is-visible");
  }

  function initVtReveal() {
    var nodes = document.querySelectorAll(".vt-reveal");
    if (!nodes.length) return;

    if (reduce || typeof IntersectionObserver === "undefined") {
      nodes.forEach(reveal);
      return;
    }

    var obs = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) {
            reveal(e.target);
            obs.unobserve(e.target);
          }
        });
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0.12 }
    );

    nodes.forEach(function (el) {
      obs.observe(el);
    });
  }

  document.addEventListener("DOMContentLoaded", initVtReveal);
})();
