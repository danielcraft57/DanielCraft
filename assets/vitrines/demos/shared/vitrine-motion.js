(function () {
  "use strict";

  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function initReveal() {
    var nodes = document.querySelectorAll(".vt-reveal, .vt-reveal-fade, .vt-reveal-stagger, .vt-ken-burns");
    if (!nodes.length) return;
    if (reduced) {
      nodes.forEach(function (el) {
        el.classList.add("vt-reveal--in");
      });
      return;
    }
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("vt-reveal--in");
          io.unobserve(entry.target);
        });
      },
      { root: null, rootMargin: "0px 0px -8% 0px", threshold: 0.12 }
    );
    nodes.forEach(function (el) {
      io.observe(el);
    });
  }

  function initStaggerIndex() {
    document.querySelectorAll(".vt-reveal-stagger").forEach(function (wrap) {
      Array.prototype.forEach.call(wrap.children, function (child, i) {
        child.style.setProperty("--vt-i", String(i));
      });
    });
  }

  function animateCount(el) {
    var end = parseInt(el.getAttribute("data-vt-count-end") || "", 10);
    if (!Number.isFinite(end)) return;
    var suffix = el.getAttribute("data-vt-count-suffix") || "";
    var prefix = el.getAttribute("data-vt-count-prefix") || "";
    var duration = 1400;
    var start = performance.now();
    function tick(now) {
      var t = Math.min(1, (now - start) / duration);
      var eased = 1 - Math.pow(1 - t, 3);
      var val = Math.round(end * eased);
      el.textContent = prefix + val.toLocaleString("fr-FR") + suffix;
      if (t < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }

  function initCounters() {
    var counters = document.querySelectorAll("[data-vt-count-end]");
    if (!counters.length) return;
    if (reduced) return;
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          var el = entry.target;
          if (el.dataset.vtCounted) return;
          el.dataset.vtCounted = "1";
          animateCount(el);
          io.unobserve(el);
        });
      },
      { threshold: 0.4 }
    );
    counters.forEach(function (el) {
      io.observe(el);
    });
  }

  function initNavbarScroll() {
    var nav = document.querySelector(".vt-navbar");
    if (!nav) return;
    function onScroll() {
      nav.classList.toggle("vt-navbar--scrolled", window.scrollY > 24);
    }
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  function init() {
    initStaggerIndex();
    initReveal();
    initCounters();
    initNavbarScroll();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
