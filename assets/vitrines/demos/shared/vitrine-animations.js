/**
 * Init AOS (scroll) + anime.js (hero) pour vitrines sélectionnées.
 * Librairies suggérées dans la veille Codeur (animations / scroll) :
 * https://www.codeur.com/blog/meilleures-librairies-javascript/
 */
(function () {
  "use strict";

  var reduceMotion =
    typeof window.matchMedia === "function" &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function initAos() {
    if (typeof window.AOS === "undefined") return;
    window.AOS.init({
      duration: 720,
      easing: "ease-out-cubic",
      once: true,
      offset: 48,
      disable: reduceMotion,
    });
  }

  function revealHeroPreState() {
    document.querySelectorAll(".vitrine-hero-animate.is-vitrine-prejs").forEach(function (el) {
      el.classList.remove("is-vitrine-prejs");
    });
  }

  function initHeroAnime() {
    if (reduceMotion || typeof window.anime === "undefined") return;
    var hero = document.querySelector(".vitrine-hero-animate");
    if (!hero) {
      revealHeroPreState();
      return;
    }

    var blocks = hero.querySelectorAll(".title, .subtitle, .buttons");
    if (!blocks.length) {
      revealHeroPreState();
      return;
    }

    var tl = window.anime.timeline({
      easing: "easeOutExpo",
      complete: revealHeroPreState,
    });

    tl.add({
      targets: blocks,
      opacity: [0, 1],
      translateY: [22, 0],
      duration: 880,
      delay: window.anime.stagger(110, { start: 120 }),
    });

    var buttons = hero.querySelectorAll(".buttons .button");
    if (buttons.length) {
      tl.add(
        {
          targets: buttons,
          scale: [0.94, 1],
          duration: 520,
          delay: window.anime.stagger(80),
          easing: "easeOutBack",
        },
        "-=480"
      );
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    initAos();
    if (reduceMotion) {
      revealHeroPreState();
      return;
    }
    initHeroAnime();
    if (typeof window.anime === "undefined") {
      revealHeroPreState();
    }
    /* Si anime.js ne charge pas ou reste bloqué, afficher le hero au plus tard */
    window.setTimeout(revealHeroPreState, 2400);
  });
})();
