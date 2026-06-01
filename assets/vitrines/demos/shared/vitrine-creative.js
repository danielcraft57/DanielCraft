/**
 * Barre de progression de scroll, halo hero au pointeur, micro-magnétisme CTA.
 */
(function () {
  "use strict";

  var reduceMotion =
    typeof window.matchMedia === "function" &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function updateReadProgress() {
    var doc = document.documentElement;
    var scrollTop = window.scrollY || doc.scrollTop;
    var maxScroll = doc.scrollHeight - window.innerHeight;
    var p = maxScroll > 0 ? scrollTop / maxScroll : 0;
    doc.style.setProperty("--vitrine-read", String(Math.min(1, Math.max(0, p))));
  }

  function initHeroGlow() {
    document.querySelectorAll(".vitrine-hero-glowspot").forEach(function (hero) {
      function setFromEvent(e) {
        var r = hero.getBoundingClientRect();
        var x = ((e.clientX - r.left) / Math.max(1, r.width)) * 100;
        var y = ((e.clientY - r.top) / Math.max(1, r.height)) * 100;
        hero.style.setProperty("--vg-x", x + "%");
        hero.style.setProperty("--vg-y", y + "%");
      }
      hero.addEventListener("mousemove", setFromEvent);
      hero.addEventListener("mouseleave", function () {
        hero.style.setProperty("--vg-x", "50%");
        hero.style.setProperty("--vg-y", "42%");
      });
    });
  }

  function initMagnetic() {
    document.querySelectorAll(".vitrine-magnetic-wrap").forEach(function (wrap) {
      wrap.addEventListener("mousemove", function (e) {
        wrap.querySelectorAll("a.button, button.button").forEach(function (btn) {
          var br = btn.getBoundingClientRect();
          var cx = br.left + br.width / 2;
          var cy = br.top + br.height / 2;
          var mx = (e.clientX - cx) * 0.09;
          var my = (e.clientY - cy) * 0.09;
          var cap = 12;
          mx = Math.max(-cap, Math.min(cap, mx));
          my = Math.max(-cap, Math.min(cap, my));
          btn.style.transform = "translate(" + mx + "px," + my + "px)";
        });
      });
      wrap.addEventListener("mouseleave", function () {
        wrap.querySelectorAll("a.button, button.button").forEach(function (btn) {
          btn.style.transform = "";
        });
      });
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    window.addEventListener("scroll", updateReadProgress, { passive: true });
    window.addEventListener("resize", updateReadProgress, { passive: true });
    updateReadProgress();

    if (reduceMotion) {
      return;
    }
    initHeroGlow();
    initMagnetic();
  });
})();
