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

  function initReadProgress() {
    var bar = document.querySelector(".vt-read-progress");
    if (!bar) {
      bar = document.createElement("div");
      bar.className = "vt-read-progress";
      bar.setAttribute("aria-hidden", "true");
      document.body.prepend(bar);
    }
    if (reduced) return;
    function onScroll() {
      var h = document.documentElement;
      var max = h.scrollHeight - h.clientHeight;
      var p = max > 0 ? window.scrollY / max : 0;
      bar.style.setProperty("--vt-read", String(Math.min(1, Math.max(0, p))));
    }
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  function initSaasTabs() {
    document.querySelectorAll("[data-vt-tabs]").forEach(function (nav) {
      var buttons = nav.querySelectorAll(".vt-tab-btn");
      var root = nav.closest("section");
      if (!root) return;
      var panels = root.querySelectorAll(".vt-tab-panel");
      buttons.forEach(function (btn) {
        btn.addEventListener("click", function () {
          var target = btn.getAttribute("data-vt-tab-target");
          buttons.forEach(function (b) {
            b.classList.remove("active");
            b.setAttribute("aria-selected", "false");
          });
          panels.forEach(function (p) {
            p.classList.remove("active");
          });
          btn.classList.add("active");
          btn.setAttribute("aria-selected", "true");
          var panel = root.querySelector("#" + target);
          if (panel) panel.classList.add("active");
        });
      });
    });
  }

  function initTiltCards() {
    if (reduced) return;
    document.querySelectorAll(".vt-tilt-card").forEach(function (card) {
      card.addEventListener("mousemove", function (e) {
        var r = card.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width - 0.5;
        var y = (e.clientY - r.top) / r.height - 0.5;
        card.style.transform =
          "perspective(800px) rotateY(" + x * 6 + "deg) rotateX(" + -y * 6 + "deg) translateY(-4px)";
      });
      card.addEventListener("mouseleave", function () {
        card.style.transform = "";
      });
    });
  }

  function initProgressWizard() {
    document.querySelectorAll("[data-vt-progress-wizard]").forEach(function (root) {
      var steps = root.querySelectorAll("[data-vt-wizard-step]");
      var panels = root.querySelectorAll("[data-vt-wizard-panel]");
      var fill = root.querySelector(".vt-wizard-bar-fill");
      var total = parseInt(root.getAttribute("data-vt-step-count") || "1", 10);
      function goTo(idx) {
        steps.forEach(function (btn, i) {
          var on = i === idx;
          btn.classList.toggle("active", on);
          btn.setAttribute("aria-current", on ? "step" : "false");
        });
        panels.forEach(function (panel, i) {
          panel.classList.toggle("active", i === idx);
        });
        if (fill) {
          var pct = Math.round(((idx + 1) / total) * 100);
          fill.style.setProperty("--vt-wizard-pct", pct + "%");
        }
      }
      steps.forEach(function (btn) {
        btn.addEventListener("click", function () {
          var idx = parseInt(btn.getAttribute("data-vt-wizard-step") || "0", 10);
          goTo(idx);
        });
      });
    });
  }

  function initDialogs() {
    document.querySelectorAll("[data-vt-dialog-open]").forEach(function (btn) {
      btn.addEventListener("click", function (e) {
        var id = btn.getAttribute("data-vt-dialog-open");
        var dlg = id ? document.getElementById(id) : null;
        if (!dlg) return;
        e.preventDefault();
        dlg.hidden = false;
        requestAnimationFrame(function () {
          dlg.classList.add("is-open");
        });
      });
    });
    document.querySelectorAll("[data-vt-dialog]").forEach(function (dlg) {
      function close() {
        dlg.classList.remove("is-open");
        setTimeout(function () {
          dlg.hidden = true;
        }, 320);
      }
      dlg.addEventListener("click", function (e) {
        if (e.target === dlg) close();
      });
      dlg.querySelectorAll("[data-vt-dialog-close]").forEach(function (b) {
        b.addEventListener("click", close);
      });
    });
  }

  function initSnackbar() {
    var snack = document.querySelector(".vt-snackbar");
    if (!snack) return;
    var timer = 0;
    function show(msg) {
      if (msg) snack.textContent = msg;
      snack.classList.add("is-on");
      clearTimeout(timer);
      timer = setTimeout(function () {
        snack.classList.remove("is-on");
      }, 2800);
    }
    document.querySelectorAll("[data-vt-snack]").forEach(function (el) {
      el.addEventListener("click", function () {
        show(el.getAttribute("data-vt-snack") || "OK");
      });
    });
    window.vtShowSnack = show;
  }

  function initFabMenu() {
    document.querySelectorAll("[data-vt-fab-menu]").forEach(function (wrap) {
      var main = wrap.querySelector(".vt-fab-menu-main");
      if (!main) return;
      main.addEventListener("click", function () {
        var open = wrap.classList.toggle("is-open");
        main.setAttribute("aria-expanded", open ? "true" : "false");
      });
    });
  }

  function initChipRows() {
    document.querySelectorAll(".vt-chip-row, .vt-date-row, .vt-time-grid").forEach(function (row) {
      row.addEventListener("click", function (e) {
        var btn = e.target.closest("button");
        if (!btn || !row.contains(btn)) return;
        row.querySelectorAll("button").forEach(function (b) {
          b.classList.remove("on");
        });
        btn.classList.add("on");
      });
    });
  }

  function init() {
    initStaggerIndex();
    initReveal();
    initCounters();
    initNavbarScroll();
    initReadProgress();
    initSaasTabs();
    initTiltCards();
    initProgressWizard();
    initDialogs();
    initSnackbar();
    initFabMenu();
    initChipRows();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
