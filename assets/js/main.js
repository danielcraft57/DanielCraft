// ===== MAIN JAVASCRIPT - V6 FREELANCE =====

class DanielCraftApp {
  constructor() {
    this.init();
  }

  init() {
    this.setupEventListeners();
    this.initNavigation();
    this.initCounters();
    this.initPortfolioFilter();
    this.initContactForm();
    this.initMobileMenu();
    this.initDropdownMenu();
    this.initScrollAnimations();
    this.initFaqAccordion();
    this.initBackToTop();
  }

  /** Affiche/masque le bouton "retour en haut" au scroll (logique dans handleNavbarScroll). */
  initBackToTop() {
    // Le clic et la visibilité du bouton #backToTop sont gérés dans setupEventListeners et handleNavbarScroll
  }

  setupEventListeners() {
    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(link => {
      link.addEventListener('click', this.handleSmoothScroll.bind(this));
    });

    // Navbar scroll effect
    window.addEventListener('scroll', this.throttle(this.handleNavbarScroll.bind(this), 16));

    // Back to top : clic scroll en haut
    const backToTop = document.getElementById('backToTop');
    if (backToTop) {
      backToTop.addEventListener('click', (e) => {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    }
  }

  handleSmoothScroll(e) {
    e.preventDefault();
    const targetId = e.target.closest('a').getAttribute('href');
    const targetElement = document.querySelector(targetId);
    
    if (targetElement) {
      const offsetTop = targetElement.offsetTop - 80;
      
      window.scrollTo({
        top: offsetTop,
        behavior: 'smooth'
      });

      this.updateActiveNavLink(targetId);
      this.closeMobileMenu();
    }
  }

  handleNavbarScroll() {
    const navbar = document.getElementById('navbar');
    if (navbar) {
      const scrolled = window.scrollY > 50;
      navbar.classList.toggle('scrolled', scrolled);
      if (window.scrollY > 200) {
        navbar.classList.add('compact');
      } else {
        navbar.classList.remove('compact');
      }
    }
    const backToTop = document.getElementById('backToTop');
    if (backToTop) {
      backToTop.classList.toggle('is-visible', window.scrollY > 400);
    }
  }

  initNavigation() {
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('section[id]');

    window.addEventListener('scroll', () => {
      let current = '';
      sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (window.scrollY >= sectionTop - 200) {
          current = section.getAttribute('id');
        }
      });

      navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
          link.classList.add('active');
        }
      });
    });
  }

  updateActiveNavLink(targetId) {
    document.querySelectorAll('.nav-link').forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === targetId) {
        link.classList.add('active');
      }
    });
  }

  initCounters() {
    const counters = document.querySelectorAll('.stat-number');
    
    const animateCounter = (counter) => {
      const target = parseInt(counter.getAttribute('data-target'));
      const suffix = target === 100 ? '' : '+';
      const duration = 2000;
      const increment = target / (duration / 16);
      let current = 0;

      const updateCounter = () => {
        current += increment;
        if (current < target) {
          counter.textContent = Math.floor(current) + suffix;
          requestAnimationFrame(updateCounter);
        } else {
          counter.textContent = target + suffix;
        }
      };

      updateCounter();
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });

    counters.forEach(counter => observer.observe(counter));
  }

  initPortfolioFilter() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    
    filterButtons.forEach(button => {
      button.addEventListener('click', () => {
        // Remove active class from all buttons
        filterButtons.forEach(btn => btn.classList.remove('active'));
        // Add active class to clicked button
        button.classList.add('active');
        
        // Get filter value
        const filter = button.getAttribute('data-filter');
        
        // Filter portfolio items
        if (window.renderPortfolio) {
          window.renderPortfolio(filter);
        }
      });
    });
  }

  initContactForm() {
    const form = document.getElementById('contactForm');
    const feedbackEl = document.getElementById('formFeedback');
    const submitBtn = document.getElementById('contactSubmitBtn');
    if (!form || !feedbackEl || !submitBtn) return;

    function showFeedback(message, isError = false) {
      feedbackEl.textContent = message;
      feedbackEl.hidden = false;
      feedbackEl.className = 'form-feedback ' + (isError ? 'form-feedback--error' : 'form-feedback--success');
    }

    function hideFeedback() {
      feedbackEl.hidden = true;
      feedbackEl.textContent = '';
    }

    form.addEventListener('submit', async (e) => {
      e.preventDefault();

      const formData = new FormData(form);
      const name = (formData.get('name') || '').trim();
      const email = (formData.get('email') || '').trim();
      const message = (formData.get('message') || '').trim();
      const service = formData.get('service');

      if (!name || !email || !message) {
        showFeedback('Veuillez remplir tous les champs obligatoires (nom, email, message).', true);
        return;
      }

      if (!service) {
        showFeedback('Veuillez sélectionner un type de projet.', true);
        return;
      }

      hideFeedback();
      submitBtn.disabled = true;
      submitBtn.classList.add('is-loading');

      try {
        const res = await fetch('/api/send-contact.php', {
          method: 'POST',
          body: formData
        });
        const data = await res.json().catch(() => ({}));

        if (res.ok && data.success) {
          showFeedback('Merci pour votre message. Je vous répondrai rapidement.');
          form.reset();
          feedbackEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        } else {
          showFeedback(data.error || 'Une erreur est survenue. Réessayez ou écrivez à contact@danielcraft.fr.', true);
          feedbackEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
      } catch (err) {
        showFeedback('Erreur de connexion. Vérifiez votre réseau ou écrivez à contact@danielcraft.fr.', true);
        feedbackEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      } finally {
        submitBtn.disabled = false;
        submitBtn.classList.remove('is-loading');
      }
    });
  }

  initMobileMenu() {
    const toggle = document.getElementById('navToggle');
    const menu = document.getElementById('navMenu');
    
    if (toggle && menu) {
      // Fermer le menu au clic sur un lien
      const menuLinks = menu.querySelectorAll('.nav-link');
      menuLinks.forEach(link => {
        link.addEventListener('click', () => {
          this.closeMobileMenu();
        });
      });
      
      // Toggle menu
      toggle.addEventListener('click', () => {
        const isOpen = menu.classList.contains('active');
        if (isOpen) {
          this.closeMobileMenu();
        } else {
          this.openMobileMenu();
        }
      });
      
      // Fermer le menu avec Escape
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && menu.classList.contains('active')) {
          this.closeMobileMenu();
        }
      });
      
      // Fermer le menu au clic en dehors
      document.addEventListener('click', (e) => {
        if (menu.classList.contains('active') && 
            !menu.contains(e.target) && 
            !toggle.contains(e.target)) {
          this.closeMobileMenu();
        }
      });
    }
  }
  
  openMobileMenu() {
    const toggle = document.getElementById('navToggle');
    const menu = document.getElementById('navMenu');
    
    if (toggle && menu) {
      menu.classList.add('active');
      toggle.classList.add('active');
      toggle.setAttribute('aria-expanded', 'true');
      document.body.classList.add('menu-open');
      // Focus sur le premier lien pour l'accessibilité
      const firstLink = menu.querySelector('.nav-link');
      if (firstLink) {
        setTimeout(() => firstLink.focus(), 100);
      }
    }
  }
  
  closeMobileMenu() {
    const toggle = document.getElementById('navToggle');
    const menu = document.getElementById('navMenu');
    
    if (toggle && menu) {
      menu.classList.remove('active');
      toggle.classList.remove('active');
      toggle.setAttribute('aria-expanded', 'false');
      document.body.classList.remove('menu-open');
      // Retourner le focus au bouton toggle
      toggle.focus();
    }
  }

  initDropdownMenu() {
    const dropdownToggle = document.querySelector('.nav-dropdown-toggle');
    const dropdownMenu = document.querySelector('.nav-dropdown-menu');
    
    if (dropdownToggle && dropdownMenu) {
      dropdownToggle.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        
        const isOpen = dropdownToggle.getAttribute('aria-expanded') === 'true';
        dropdownToggle.setAttribute('aria-expanded', !isOpen);
        dropdownMenu.classList.toggle('active');
        
        // Fermer les autres dropdowns si nécessaire
        document.querySelectorAll('.nav-dropdown-menu').forEach(menu => {
          if (menu !== dropdownMenu) {
            menu.classList.remove('active');
          }
        });
      });
      
      // Fermer au clic en dehors
      document.addEventListener('click', (e) => {
        if (!dropdownToggle.contains(e.target) && !dropdownMenu.contains(e.target)) {
          dropdownMenu.classList.remove('active');
          dropdownToggle.setAttribute('aria-expanded', 'false');
        }
      });
      
      // Fermer avec Escape
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && dropdownMenu.classList.contains('active')) {
          dropdownMenu.classList.remove('active');
          dropdownToggle.setAttribute('aria-expanded', 'false');
          dropdownToggle.focus();
        }
      });
    }
  }

  initScrollAnimations() {
    const observerOptions = {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
        }
      });
    }, observerOptions);

    const selectors = ['.scroll-reveal', '.scroll-reveal-left', '.scroll-reveal-right', '.scroll-reveal-scale'];
    selectors.forEach(sel => {
      document.querySelectorAll(sel).forEach(el => observer.observe(el));
    });
  }

  /**
   * FAQ accordéon : une question ouverte à la fois, aria-expanded et hidden gérés.
   */
  initFaqAccordion() {
    const buttons = document.querySelectorAll('[data-faq-toggle]');
    const items = document.querySelectorAll('.faq-item');
    if (!buttons.length) return;

    const firstBtn = buttons[0];
    const firstPanel = firstBtn && document.getElementById(firstBtn.getAttribute('aria-controls'));
    if (firstBtn && firstPanel) {
      firstBtn.setAttribute('aria-expanded', 'true');
      firstPanel.hidden = false;
      firstBtn.closest('.faq-item').classList.add('is-open');
    }

    buttons.forEach(btn => {
      btn.addEventListener('click', () => {
        const item = btn.closest('.faq-item');
        const panel = document.getElementById(btn.getAttribute('aria-controls'));
        const isOpen = btn.getAttribute('aria-expanded') === 'true';

        items.forEach(it => {
          const b = it.querySelector('[data-faq-toggle]');
          const p = b && document.getElementById(b.getAttribute('aria-controls'));
          if (b) b.setAttribute('aria-expanded', 'false');
          if (p) p.hidden = true;
          it.classList.remove('is-open');
        });

        if (!isOpen) {
          btn.setAttribute('aria-expanded', 'true');
          if (panel) panel.hidden = false;
          item.classList.add('is-open');
        }
      });
    });
  }

  // Utility functions
  throttle(func, limit) {
    let inThrottle;
    return function() {
      const args = arguments;
      const context = this;
      if (!inThrottle) {
        func.apply(context, args);
        inThrottle = true;
        setTimeout(() => inThrottle = false, limit);
      }
    };
  }

  debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
      const later = () => {
        clearTimeout(timeout);
        func(...args);
      };
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
    };
  }
}

// Initialize app when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    new DanielCraftApp();
  });
} else {
  new DanielCraftApp();
}

