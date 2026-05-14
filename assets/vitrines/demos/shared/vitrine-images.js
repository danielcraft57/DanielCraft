/**
 * Swiper (carrousel) + GLightbox (galerie plein écran / zoom) pour visuels vitrine.
 * Librairies : https://swiperjs.com/ · https://github.com/biati-digital/glightbox
 */
(function () {
  "use strict";

  var reduceMotion =
    typeof window.matchMedia === "function" &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function initSwipers() {
    if (typeof Swiper === "undefined") return;
    document.querySelectorAll(".vitrine-image-swiper").forEach(function (el) {
      var paginationEl = el.querySelector(".swiper-pagination");
      var nextEl = el.querySelector(".swiper-button-next");
      var prevEl = el.querySelector(".swiper-button-prev");
      var opts = {
        loop: true,
        grabCursor: true,
        speed: reduceMotion ? 0 : 620,
        autoplay: reduceMotion
          ? false
          : {
              delay: 5000,
              disableOnInteraction: true,
              pauseOnMouseEnter: true,
            },
        effect: reduceMotion ? "slide" : "coverflow",
        centeredSlides: true,
        slidesPerView: 1,
        spaceBetween: 16,
        breakpoints: {
          640: {
            slidesPerView: 1.12,
            spaceBetween: 18,
          },
          900: {
            slidesPerView: 1.55,
            spaceBetween: 20,
          },
          1200: {
            slidesPerView: 2,
            spaceBetween: 22,
          },
        },
        pagination: paginationEl
          ? {
              el: paginationEl,
              clickable: true,
            }
          : undefined,
        navigation:
          nextEl && prevEl
            ? {
                nextEl: nextEl,
                prevEl: prevEl,
              }
            : undefined,
      };
      if (!reduceMotion) {
        opts.coverflowEffect = {
          rotate: 20,
          stretch: 0,
          depth: 120,
          modifier: 1,
          slideShadows: false,
        };
      }
      new Swiper(el, opts);
    });
  }

  function initGLightbox() {
    if (typeof GLightbox === "undefined") return;
    GLightbox({
      selector: ".glightbox",
      touchNavigation: true,
      loop: true,
      zoomable: true,
      draggable: true,
      openEffect: reduceMotion ? "none" : "zoom",
      closeEffect: reduceMotion ? "none" : "zoom",
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    augmentFigureRevealTargets();
    initSwipers();
    initGLightbox();
    initImgReveal();
  });

  /** Figures hors colonnes déjà marquées : même animation d’apparition au scroll */
  function augmentFigureRevealTargets() {
    document.querySelectorAll("main figure.vitrine-figure").forEach(function (fig) {
      if (fig.closest(".vitrine-img-reveal")) return;
      fig.classList.add("vitrine-img-reveal");
    });
  }

  function initImgReveal() {
    var nodes = document.querySelectorAll(".vitrine-img-reveal");
    if (!nodes.length) return;
    if (reduceMotion) {
      nodes.forEach(function (el) {
        el.classList.add("is-inview");
      });
      return;
    }
    if (typeof IntersectionObserver === "undefined") {
      nodes.forEach(function (el) {
        el.classList.add("is-inview");
      });
      return;
    }
    var obs = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) {
            e.target.classList.add("is-inview");
            obs.unobserve(e.target);
          }
        });
      },
      { rootMargin: "0px 0px -6% 0px", threshold: 0.08 }
    );
    nodes.forEach(function (el) {
      obs.observe(el);
    });
  }
})();
