/**
 * Accueil : stagger reveal, tilt, lazy images, rotation blog.
 */
(function () {
  'use strict';

  if (
    !document.querySelector('.home-hero--wow') &&
    !document.querySelector('.home-offers') &&
    !document.querySelector('.home-body-ecom')
  ) {
    return;
  }

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
    const media =
      document.querySelector('.home-hero-anim__stack') ||
      document.querySelector('.home-split__media img');
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

  function hydrateLazyImage(img) {
    if (!img || img.dataset.homeEager !== undefined) return;
    if (img.dataset.lazyDone === '1') return;
    const picture = img.closest('picture');
    if (picture) {
      picture.querySelectorAll('source[data-srcset]').forEach(function (source) {
        source.setAttribute('srcset', source.getAttribute('data-srcset'));
        source.removeAttribute('data-srcset');
      });
    }
    const src = img.getAttribute('data-src');
    if (src) {
      img.setAttribute('src', src);
      img.removeAttribute('data-src');
    }
    img.dataset.lazyDone = '1';
    img.classList.add('is-loaded');
  }

  function initScrollLazyImages() {
    const root = document.querySelector('.page-home-ecom');
    if (!root) return;

    root.querySelectorAll('img:not([data-home-eager])').forEach(function (img) {
      if (img.classList.contains('home-lazy-img') && img.getAttribute('data-src')) return;
      const current = img.getAttribute('src');
      if (!current || current.indexOf('data:') === 0) return;
      img.setAttribute('data-src', current);
      img.removeAttribute('src');
      img.classList.add('home-lazy-img');
      const picture = img.closest('picture');
      if (picture) {
        picture.querySelectorAll('source[srcset]').forEach(function (source) {
          source.setAttribute('data-srcset', source.getAttribute('srcset'));
          source.removeAttribute('srcset');
        });
      }
    });

    const targets = root.querySelectorAll('img.home-lazy-img');
    if (!targets.length) return;

    if (!('IntersectionObserver' in window)) {
      targets.forEach(hydrateLazyImage);
      return;
    }

    const io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          hydrateLazyImage(entry.target);
          io.unobserve(entry.target);
        });
      },
      { root: null, rootMargin: '280px 0px', threshold: 0.01 },
    );

    targets.forEach(function (img) {
      io.observe(img);
    });

    const heroB = document.querySelector('.home-hero-anim__frame--b img.home-lazy-img');
    if (heroB) {
      const kick = function () {
        hydrateLazyImage(heroB);
      };
      if ('requestIdleCallback' in window) {
        window.requestIdleCallback(kick, { timeout: 1800 });
      } else {
        window.setTimeout(kick, 900);
      }
    }
  }

  function initBlogRotate() {
    const root = document.querySelector('[data-home-blog-rotate]');
    if (!root) return;

    // 3 jeux de 3 articles - rotation matin / midi / soir (heure locale)
    const pools = [
      [
        {
          href: '/blog/geo-vs-seo-differences-complementarite/',
          cat: 'Visibilité',
          title: 'Être trouvé sur Google et par les IA : les bases',
          img: 'home-blog-seo',
        },
        {
          href: '/blog/geo-contenu-structure-formats-checklist/',
          cat: 'Contenu',
          title: 'Des pages claires qui convertissent mieux',
          img: 'home-blog-landing',
        },
        {
          href: '/blog/geo-outils-optimisation-moteurs-generatifs/',
          cat: 'Outils',
          title: 'Outils utiles pour suivre ta visibilité',
          img: 'home-blog-fiche',
        },
      ],
      [
        {
          href: '/blog/geo-technique-indexabilite-html-performance/',
          cat: 'Rapide',
          title: 'Un site rapide : ce qui compte vraiment',
          img: 'home-blog-landing',
        },
        {
          href: '/blog/outils-geo-audit-suivi-citations/',
          cat: 'Audit',
          title: 'Auditer ta présence en ligne sans te perdre',
          img: 'home-blog-seo',
        },
        {
          href: '/blog/geo-off-site-mentions-autorite/',
          cat: 'Confiance',
          title: 'Mentions et avis : renforcer ta crédibilité',
          img: 'home-blog-fiche',
        },
      ],
      [
        {
          href: '/blog/les-frameworks-frontend-en-2025-react-vue-angular/',
          cat: 'Choix',
          title: 'Choisir la bonne techno pour ton projet',
          img: 'home-blog-fiche',
        },
        {
          href: '/blog/introduction-à-typescript-pour-les-développeurs-javascript/',
          cat: 'Qualité',
          title: 'Moins de bugs : pourquoi je soigne le code',
          img: 'home-blog-landing',
        },
        {
          href: '/blog/geo-outils-optimisation-moteurs-generatifs/',
          cat: 'IA',
          title: 'Être cité aussi par les outils IA',
          img: 'home-blog-seo',
        },
      ],
    ];

    const hour = new Date().getHours();
    const slot = hour < 12 ? 0 : hour < 18 ? 1 : 2;
    const items = pools[slot];
    const cards = root.querySelectorAll('.home-blog-card');
    cards.forEach(function (card, i) {
      const item = items[i];
      if (!item) return;
      const media = card.querySelector('.home-blog-card__media');
      const img = card.querySelector('img');
      const source = card.querySelector('source');
      const cat = card.querySelector('.home-blog-card__cat');
      const titleA = card.querySelector('h3 a');
      const more = card.querySelector('.home-blog-card__more');
      const schemaUrl = card.querySelector('link[itemprop="url"]');
      const schemaImg = card.querySelector('link[itemprop="image"]');
      const png = '/assets/images/home/' + item.img + '.png';
      const webp = '/assets/images/home/' + item.img + '.webp';
      if (media) media.setAttribute('href', item.href);
      if (schemaUrl) schemaUrl.setAttribute('href', item.href);
      if (schemaImg) schemaImg.setAttribute('href', png);
      if (img) {
        img.alt = '';
        img.dataset.lazyDone = '0';
        img.classList.add('home-lazy-img');
        if (img.hasAttribute('src') && !img.hasAttribute('data-src')) {
          img.setAttribute('data-src', png);
          img.removeAttribute('src');
        } else {
          img.setAttribute('data-src', png);
        }
      }
      if (source) {
        source.removeAttribute('srcset');
        source.setAttribute('data-srcset', webp);
      }
      if (cat) cat.textContent = item.cat;
      if (titleA) {
        titleA.href = item.href;
        titleA.textContent = item.title;
      }
      if (more) more.href = item.href;
    });
  }

  initTiltCards();
  initHeroParallax();
  initStagger();
  initBlogRotate();
  initScrollLazyImages();
})();
