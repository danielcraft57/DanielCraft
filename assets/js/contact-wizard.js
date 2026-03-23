/**
 * Formulaire contact en 4 étapes : prestation (liste cliquable), créneau, coordonnées, message.
 */
(function () {
  'use strict';

  const MONTH_NAMES = [
    'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
    'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'
  ];
  function pad2(n) {
    return String(n).padStart(2, '0');
  }

  function toISODate(d) {
    return `${d.getFullYear()}-${pad2(d.getMonth() + 1)}-${pad2(d.getDate())}`;
  }

  function parseISODate(s) {
    const [y, m, day] = s.split('-').map(Number);
    return new Date(y, m - 1, day);
  }

  /** Lundi = 0 … Dimanche = 6 */
  function mondayIndex(d) {
    return (d.getDay() + 6) % 7;
  }

  function isWeekend(d) {
    const day = d.getDay();
    return day === 0 || day === 6;
  }

  function isSameDay(a, b) {
    return (
      a.getFullYear() === b.getFullYear() &&
      a.getMonth() === b.getMonth() &&
      a.getDate() === b.getDate()
    );
  }

  function startOfDay(d) {
    return new Date(d.getFullYear(), d.getMonth(), d.getDate());
  }

  function addDays(d, n) {
    const x = new Date(d);
    x.setDate(x.getDate() + n);
    return x;
  }

  /** Dimanche de Pâques (calendrier grégorien), heure locale. */
  function easterSunday(year) {
    const a = year % 19;
    const b = Math.floor(year / 100);
    const c = year % 100;
    const d = Math.floor(b / 4);
    const e = b % 4;
    const f = Math.floor((b + 8) / 25);
    const g = Math.floor((b - f + 1) / 3);
    const h = (19 * a + b - d - g + 15) % 30;
    const i = Math.floor(c / 4);
    const k = c % 4;
    const l = (32 + 2 * e + 2 * i - h - k) % 7;
    const m = Math.floor((a + 11 * h + 22 * l) / 451);
    const month = Math.floor((h + l - 7 * m + 114) / 31);
    const day = ((h + l - 7 * m + 114) % 31) + 1;
    return new Date(year, month - 1, day);
  }

  /** Jours fériés métropole (fixes + Pâques, Ascension, Pentecôte). */
  function isFrenchPublicHoliday(d) {
    const y = d.getFullYear();
    const m = d.getMonth() + 1;
    const day = d.getDate();
    const key = `${m}-${day}`;
    const fixed = [
      '1-1',
      '5-1',
      '5-8',
      '7-14',
      '8-15',
      '11-1',
      '11-11',
      '12-25'
    ];
    if (fixed.includes(key)) return true;
    const easter = easterSunday(y);
    const easterMon = addDays(easter, 1);
    const ascension = addDays(easter, 39);
    const whitMon = addDays(easter, 50);
    return isSameDay(d, easterMon) || isSameDay(d, ascension) || isSameDay(d, whitMon);
  }

  /** Lundi–vendredi hors fériés (jours ouvrés). */
  function isJourOuvre(d) {
    return !isWeekend(d) && !isFrenchPublicHoliday(d);
  }

  function formatFrenchLong(iso) {
    if (!iso) return '';
    const d = parseISODate(iso);
    const wd = ['dimanche', 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi'][d.getDay()];
    return `${wd} ${d.getDate()} ${MONTH_NAMES[d.getMonth()]} ${d.getFullYear()}`;
  }

  /**
   * Créneaux « circadiens » : évite le tout début de matinée et le creux post-repas,
   * fenêtre d’éveil plus stable (fin matinée + milieu d’après-midi).
   */
  function buildTimeSlots() {
    const slots = [];
    for (let h = 10; h < 12; h++) {
      slots.push(`${pad2(h)}:00`, `${pad2(h)}:30`);
    }
    for (let h = 15; h < 17; h++) {
      slots.push(`${pad2(h)}:00`, `${pad2(h)}:30`);
    }
    slots.push('17:00');
    return slots;
  }

  /** Fenêtre max. de réservation (jours calendaires, pas seulement ouvrés). */
  const MAX_CALENDAR_RANGE_DAYS = 45;

  const TIME_SLOTS = buildTimeSlots();

  /**
   * Offres alignées sur /autres-prestations + forfaits page d’accueil.
   * slug → champ POST `service` ; budget optionnel (réf. forfait affichée côté mail).
   */
  /** Types de projet (portfolio + ancien formulaire). */
  const CONTACT_PROJECT_TYPES = [
    { slug: 'web', label: 'Développement Web', icon: 'fa-laptop-code' },
    { slug: 'backend', label: 'Backend & APIs', icon: 'fa-server' },
    { slug: 'mobile', label: 'Application mobile', icon: 'fa-mobile-alt' },
    { slug: 'desktop', label: 'Application desktop', icon: 'fa-desktop' },
    { slug: 'tools', label: 'Outils & automatisation', icon: 'fa-tools' },
    { slug: 'specialized', label: 'Spécialisé (data, finance, IoT…)', icon: 'fa-microchip' },
    { slug: 'learning', label: 'Veille / apprentissage / proto', icon: 'fa-graduation-cap' },
    { slug: 'other', label: 'Autre / à préciser', icon: 'fa-ellipsis-h' }
  ];

  /**
   * Offres avec tags = types de projet (étape 1) pour regroupement à l’étape 2.
   * Un même slug peut apparaître dans plusieurs groupes si pertinent.
   */
  const CONTACT_SERVICE_ITEMS = [
    { slug: 'pack_vitrine', title: 'Site vitrine', hint: '490€ · responsive, code source inclus', icon: 'fa-globe', budget: '490', tags: ['web'] },
    { slug: 'pack_identite', title: 'Identité & visibilité (multi-supports)', hint: '990€ · site + réseaux + documents', icon: 'fa-fingerprint', budget: '990', tags: ['web'] },
    { slug: 'pack_seo_complet', title: 'SEO Google + ChatGPT (pack)', hint: '699€ · visibilité search + IA', icon: 'fa-search', budget: '699', tags: ['web'] },
    { slug: 'seo_basique_290', title: 'SEO basique (audit + corrections)', hint: '290€', icon: 'fa-search', tags: ['web', 'learning'] },
    { slug: 'seo_chatgpt_490', title: 'SEO pour ChatGPT / découvrabilité IA', hint: '490€', icon: 'fa-robot', tags: ['web', 'specialized'] },
    { slug: 'ia_faq_site', title: 'Assistant IA FAQ pour site web', hint: '990€', icon: 'fa-comments', tags: ['specialized', 'web'] },
    { slug: 'ia_support_client', title: 'Assistant IA support client / email', hint: '1200€', icon: 'fa-envelope', tags: ['specialized'] },
    { slug: 'ia_contenu_web', title: 'Générateur de contenus web par IA', hint: '650€', icon: 'fa-file-alt', tags: ['specialized', 'web'] },
    { slug: 'ia_redaction_pro', title: 'Assistant IA rédaction commerciale', hint: '490€', icon: 'fa-pen-fancy', tags: ['specialized'] },
    { slug: 'ia_analyse_donnees', title: 'Analyse de données avec IA', hint: '1450€', icon: 'fa-chart-bar', tags: ['specialized', 'desktop'] },
    { slug: 'ia_chatbot_ecom', title: 'Chatbot IA e-commerce', hint: '1600€', icon: 'fa-shopping-cart', tags: ['specialized', 'mobile', 'web'] },
    { slug: 'ia_automatisation', title: 'Automatisation de tâches avec IA', hint: '1200€', icon: 'fa-tasks', tags: ['specialized', 'tools'] },
    { slug: 'ia_abo_mensuel', title: 'Maintenance mensuelle assistant IA', hint: '75€ / mois', icon: 'fa-wrench', tags: ['specialized'] },
    { slug: 'ia_evolution', title: 'Évolution fonctionnalités IA', hint: 'À partir de 330€', icon: 'fa-plus-circle', tags: ['specialized'] },
    { slug: 'ia_audit', title: 'Audit utilisation IA', hint: '400€', icon: 'fa-search', tags: ['specialized', 'learning'] },
    { slug: 'tech_conseil_archi', title: 'Conseil technique / architecture', hint: '380€', icon: 'fa-sitemap', tags: ['backend', 'mobile', 'desktop', 'tools'] },
    { slug: 'tech_integration_crm', title: 'Intégration CRM ou outil métier', hint: 'À partir de 290€', icon: 'fa-link', tags: ['tools', 'backend'] },
    { slug: 'tech_migration_donnees', title: 'Script de migration de données', hint: '330€', icon: 'fa-database', tags: ['backend', 'desktop'] },
    { slug: 'tech_api_webhook', title: 'Intégration API / webhook', hint: 'À partir de 150€', icon: 'fa-code-branch', tags: ['backend', 'mobile', 'web', 'tools'] },
    { slug: 'tech_perf_rapport', title: 'Rapport de performances (one-shot)', hint: '120€', icon: 'fa-tachometer-alt', tags: ['web'] },
    { slug: 'site_page_supp', title: 'Page supplémentaire (site vitrine)', hint: '65€ / page', icon: 'fa-file', tags: ['web'] },
    { slug: 'site_form_avance', title: 'Formulaire avancé / intégration', hint: '99€', icon: 'fa-wpforms', tags: ['web'] },
    { slug: 'site_refonte_visuelle', title: 'Refonte visuelle légère', hint: '330€', icon: 'fa-palette', tags: ['web'] },
    { slug: 'site_maj_contenu_5h', title: 'Mise à jour de contenu (pack 5h)', hint: '170€', icon: 'fa-edit', tags: ['web'] },
    { slug: 'maint_site_mensuel', title: 'Maintenance site (mensuelle)', hint: '39€ / mois', icon: 'fa-cogs', tags: ['web'] },
    { slug: 'maint_hebergement', title: 'Hébergement + nom de domaine (annuel)', hint: '79€ / an', icon: 'fa-server', tags: ['web'] },
    { slug: 'maint_backup', title: 'Backup & sécurisation', hint: '99€', icon: 'fa-save', tags: ['web', 'backend'] },
    { slug: 'maint_ssl', title: 'Certificat SSL + configuration', hint: '45€', icon: 'fa-lock', tags: ['web'] },
    { slug: 'maint_support_abo', title: 'Support / abonnement', hint: '25€ / mois', icon: 'fa-headset', tags: ['web'] },
    { slug: 'maint_depannage_2h', title: 'Dépannage / intervention (forfait 2h)', hint: '120€', icon: 'fa-tools', tags: ['web', 'desktop'] },
    { slug: 'maint_accompagnement_h', title: 'Accompagnement technique (à l’heure)', hint: '60€ / h', icon: 'fa-user-cog', tags: ['web', 'desktop', 'tools'] },
    { slug: 'maint_support_prio_h', title: 'Support prioritaire (à l’heure)', hint: '70€ / h', icon: 'fa-bolt', tags: ['web'] },
    {
      slug: 'besoin_a_preciser',
      title: 'Je ne sais pas encore',
      hint: 'On précise ensemble au call',
      icon: 'fa-question-circle',
      tags: ['web', 'backend', 'mobile', 'desktop', 'tools', 'specialized', 'learning', 'other']
    },
    {
      slug: 'projet_sur_mesure',
      title: 'Projet sur mesure / autre',
      hint: 'Devis personnalisé',
      icon: 'fa-puzzle-piece',
      tags: ['web', 'backend', 'mobile', 'desktop', 'tools', 'specialized', 'learning', 'other']
    }
  ];

  const WIZARD_STEP_COUNT = 5;

  const MSG_STATIC_SERVER =
    'Le serveur actuel ne traite pas correctement le POST PHP. Lancez le site avec PHP (ex: php -S 127.0.0.1:8000 -t dist).';

  function init() {
    const form = document.getElementById('contactForm');
    if (!form || form.dataset.contactWizard !== 'true') return;

    const feedbackEl = document.getElementById('formFeedback');
    const submitBtn = document.getElementById('contactSubmitBtn');
    const steps = Array.from(form.querySelectorAll('.contact-step'));
    const progressItems = Array.from(form.querySelectorAll('.contact-progress-min__item'));
    const liveRegion = form.querySelector('.contact-wizard-live');
    const serviceField = form.querySelector('#service');
    const budgetField = form.querySelector('#budget');
    const projectTypeField = form.querySelector('#project_type');
    const projectTypeMount = form.querySelector('#contactProjectTypeMount');
    const serviceMount = form.querySelector('#contactServiceMount');
    const pickedWrap = form.querySelector('#contactPickedServiceWrap');
    const pickedTitleEl = form.querySelector('#contactPickedServiceTitle');
    const pickedPriceEl = form.querySelector('#contactPickedServicePrice');
    const btnChangeService = form.querySelector('#contactChangeService');

    const state = {
      step: 1,
      viewYear: new Date().getFullYear(),
      viewMonth: new Date().getMonth(),
      selectedDate: '',
      selectedTime: '',
      selectedServiceTitle: '',
      selectedServicePrice: '',
      sending: false,
      timeOverlayOpen: false,
      timeOverlayReturnFocus: null
    };

    const timeOverlay = document.getElementById('contactTimeOverlay');
    const timeOverlayBackdrop = document.getElementById('contactTimeOverlayBackdrop');
    const timeOverlayClose = document.getElementById('contactTimeOverlayClose');
    const timeOverlayDateLine = document.getElementById('contactTimeOverlayDateLine');

    const hiddenDate = form.querySelector('#preferred_date');
    const hiddenTime = form.querySelector('#preferred_time');
    const calendarGrid = form.querySelector('#calendarGrid');
    const calendarMonthLabel = form.querySelector('#calendarMonthLabel');
    const btnPrevMonth = form.querySelector('#calendarPrev');
    const btnNextMonth = form.querySelector('#calendarNext');
    const timeSlotsEl = form.querySelector('#contactTimeSlots');
    const summaryDate = form.querySelector('#contactSummaryDate');
    const wizardBackFromService = document.getElementById('wizardBackFromService');
    const wizardNextFromCalendar = document.getElementById('wizardNextFromCalendar');
    const wizardBackFromCalendar = document.getElementById('wizardBackFromCalendar');
    const wizardNextFromCoords = document.getElementById('wizardNextFromCoords');
    const wizardBackFromCoords = document.getElementById('wizardBackFromCoords');
    const wizardBackFromMessage = document.getElementById('wizardBackFromMessage');
    const messageEl = form.querySelector('#message');
    const recapTypeEl = form.querySelector('#contactRecapType');
    const recapServiceEl = form.querySelector('#contactRecapService');
    const recapDateEl = form.querySelector('#contactRecapDate');
    const recapTimeEl = form.querySelector('#contactRecapTime');
    const validationRecapBlock = form.querySelector('.contact-validation-recap');
    const pendingBlock = form.querySelector('#contactValidationPending');
    const successBlock = form.querySelector('#contactValidationSuccess');
    const errorOverlay = document.getElementById('contactErrorOverlay');
    const errorOverlayBackdrop = document.getElementById('contactErrorOverlayBackdrop');
    const errorOverlayClose = document.getElementById('contactErrorOverlayClose');
    const errorOverlayMessage = document.getElementById('contactErrorOverlayMessage');
    const errorOverlayTips = document.getElementById('contactErrorOverlayTips');

    const today = startOfDay(new Date());
    const maxDate = addDays(today, MAX_CALENDAR_RANGE_DAYS);

    function updateSummary() {
      if (!summaryDate) return;
      if (!state.selectedDate) {
        summaryDate.textContent = '—';
        return;
      }
      let line = formatFrenchLong(state.selectedDate);
      if (state.selectedTime === 'flexible') {
        line += ' — créneau à définir par email';
      } else if (state.selectedTime) {
        line += ' à ' + state.selectedTime.replace(':', 'h');
      }
      summaryDate.textContent = line;
    }

    function escapeHtml(str) {
      return String(str).replace(/[&<>"']/g, (ch) => {
        const m = {
          '&': '&amp;',
          '<': '&lt;',
          '>': '&gt;',
          '"': '&quot;',
          "'": '&#39;'
        };
        return m[ch] || ch;
      });
    }

    function extractPriceLabelFromHint(hint) {
      const s = String(hint || '').trim();
      if (!s) return '';
      const first = s.split('·')[0].trim();
      // On ne considère "prix" que si on détecte un signe euro.
      if (!first.includes('€')) return '';
      return first;
    }

    function extractBudgetValueFromHint(hint) {
      const label = extractPriceLabelFromHint(hint);
      if (!label) return '';
      const m = label.match(/(\d[\d\s]*)\s*€/);
      if (!m) return '';
      return m[1].replace(/\s/g, '');
    }

    function extractDescriptionFromHint(hint) {
      const s = String(hint || '').trim();
      if (!s) return '';
      const parts = s.split('·');
      if (parts.length <= 1) return '';
      return parts.slice(1).join('·').trim();
    }

    function buildAutoMessage() {
      const typeSlug = (projectTypeField && projectTypeField.value) || '';
      const typeLabel = (CONTACT_PROJECT_TYPES.find((x) => x.slug === typeSlug) || {})
        .label || typeSlug || '—';

      const serviceTitle = state.selectedServiceTitle || '—';

      const dateLine = state.selectedDate ? formatFrenchLong(state.selectedDate) : '—';
      let timeLine = '—';
      if (state.selectedTime) {
        timeLine =
          state.selectedTime === 'flexible'
            ? 'Créneau flexible (à définir par email)'
            : `À ${state.selectedTime.replace(':', 'h')}`;
      }

      return [
        'Pré-sélection faite via le formulaire :',
        `- Type de projet : ${typeLabel}`,
        `- Prestation : ${serviceTitle}`,
        `- Date proposée : ${dateLine}`,
        `- Heure : ${timeLine}`
      ].join('\n');
    }

    function updateValidationRecap() {
      if (!recapTypeEl || !recapServiceEl || !recapDateEl || !recapTimeEl) return;

      const typeSlug = (projectTypeField && projectTypeField.value) || '';
      const typeObj = CONTACT_PROJECT_TYPES.find((x) => x.slug === typeSlug);
      recapTypeEl.textContent = typeObj?.label || '—';
      recapServiceEl.textContent = state.selectedServiceTitle || '—';

      recapDateEl.textContent = state.selectedDate ? formatFrenchLong(state.selectedDate) : '—';

      let timeLabel = '—';
      if (state.selectedTime) {
        timeLabel =
          state.selectedTime === 'flexible'
            ? 'Flexible (à définir par email)'
            : 'À ' + state.selectedTime.replace(':', 'h');
      }
      recapTimeEl.textContent = timeLabel;
    }

    function setValidationStatus(status) {
      // Garantit un affichage exclusif : pending OU success, jamais les deux.
      if (pendingBlock) pendingBlock.hidden = status !== 'pending';
      if (successBlock) successBlock.hidden = status !== 'success';
      // Pendant l'envoi, on masque le récap pour éviter l'affichage simultané.
      if (validationRecapBlock) validationRecapBlock.hidden = status === 'pending';
    }

    function showFeedback(message, isError) {
      if (!feedbackEl) return;
      feedbackEl.textContent = message;
      feedbackEl.hidden = false;
      feedbackEl.className = 'form-feedback ' + (isError ? 'form-feedback--error' : 'form-feedback--success');
    }

    function hideFeedback() {
      if (!feedbackEl) return;
      feedbackEl.hidden = true;
      feedbackEl.textContent = '';
    }

    function closeErrorOverlay() {
      if (!errorOverlay) return;
      errorOverlay.classList.remove('is-open');
      errorOverlay.setAttribute('aria-hidden', 'true');
    }

    function openErrorOverlay(message, tips) {
      if (!errorOverlay || !errorOverlayMessage) return;
      errorOverlayMessage.textContent = message;
      if (errorOverlayTips) {
        errorOverlayTips.innerHTML = '';
        (tips || []).forEach((tip) => {
          const li = document.createElement('li');
          li.textContent = tip;
          errorOverlayTips.appendChild(li);
        });
      }
      errorOverlay.classList.add('is-open');
      errorOverlay.setAttribute('aria-hidden', 'false');
    }

    function buildErrorOverlayContent(data, resStatus) {
      const raw = String(data?.error || '').trim();
      if (resStatus === 500 || /mail\(\)|PHPMailer|smtp|envoi email impossible/i.test(raw)) {
        return {
          message:
            'L’email n’a pas pu être transmis au serveur mail. La demande n’est pas envoyée.',
          tips: [
            'Vérifiez la configuration SMTP (.env : serveur, port, identifiants).',
            'Consultez les logs PHP pour le détail (authentification TLS / login).',
            'Si besoin, contactez directement contact@danielcraft.fr.'
          ]
        };
      }
      if (/requ[êe]te invalide/i.test(raw)) {
        return {
          message: 'La requête a été refusée pour raison de sécurité.',
          tips: [
            'Rechargez la page puis recommencez le formulaire.',
            'Désactivez temporairement les extensions qui auto-remplissent.',
            'Si le problème persiste, contactez contact@danielcraft.fr.'
          ]
        };
      }
      return {
        message: raw || 'Une erreur est survenue pendant l’envoi.',
        tips: [
          'Réessayez dans quelques instants.',
          'Vérifiez votre connexion Internet.',
          'Sinon, écrivez à contact@danielcraft.fr.'
        ]
      };
    }

    function announce(msg) {
      if (liveRegion) liveRegion.textContent = msg;
    }

    function onTimeOverlayEscape(e) {
      if (e.key === 'Escape') {
        e.preventDefault();
        closeTimeOverlay();
      }
    }

    function closeTimeOverlay() {
      if (!timeOverlay || !state.timeOverlayOpen) return;
      state.timeOverlayOpen = false;
      timeOverlay.classList.remove('contact-time-overlay--open');
      timeOverlay.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('contact-time-overlay-active');
      document.removeEventListener('keydown', onTimeOverlayEscape);
      const ret = state.timeOverlayReturnFocus;
      state.timeOverlayReturnFocus = null;
      if (ret && typeof ret.focus === 'function') {
        ret.focus({ preventScroll: true });
      }
    }

    function openTimeOverlay(focusReturnEl) {
      if (!timeOverlay || !state.selectedDate) return;
      state.timeOverlayOpen = true;
      state.timeOverlayReturnFocus = focusReturnEl || null;
      if (timeOverlayDateLine) {
        timeOverlayDateLine.textContent = formatFrenchLong(state.selectedDate);
      }
      renderTimeSlots();
      timeOverlay.setAttribute('aria-hidden', 'false');
      timeOverlay.classList.add('contact-time-overlay--open');
      document.body.classList.add('contact-time-overlay-active');
      document.addEventListener('keydown', onTimeOverlayEscape);
      requestAnimationFrame(() => {
        const firstSlot = timeSlotsEl?.querySelector('.time-slot:not(.time-slot--disabled)');
        if (firstSlot && typeof firstSlot.focus === 'function') {
          firstSlot.focus();
        } else if (timeOverlayClose) {
          timeOverlayClose.focus();
        }
      });
    }

    function updateProgress() {
      progressItems.forEach((el, i) => {
        const stepIndex = i + 1;
        el.classList.remove('is-done', 'is-active', 'is-todo');
        if (stepIndex < state.step) el.classList.add('is-done');
        else if (stepIndex === state.step) el.classList.add('is-active');
        else el.classList.add('is-todo');
        if (stepIndex === state.step) el.setAttribute('aria-current', 'step');
        else el.removeAttribute('aria-current');
      });
    }

    function setStep(n) {
      const entering = form.querySelector(`.contact-step[data-step="${n}"]`);
      if (!entering) return;

      if (n === state.step) {
        updateProgress();
        return;
      }

      if (state.step === 3 && n !== 3) {
        closeTimeOverlay();
      }

      state.step = n;

      steps.forEach((stepEl) => {
        const sn = parseInt(stepEl.dataset.step, 10);
        const active = sn === n;
        stepEl.classList.toggle('is-active', active);
        stepEl.setAttribute('aria-hidden', active ? 'false' : 'true');
      });

      updateProgress();

      if (n === 5) {
        updateValidationRecap();
      }

      let focusTarget = null;
      if (n === 1) {
        focusTarget =
          entering.querySelector('.contact-type-chip.is-selected') ||
          entering.querySelector('.contact-type-chip');
      }

      if (n === 2) {
        renderServiceGrid();
        focusTarget = entering.querySelector('.contact-service-card.is-selected') || entering.querySelector('.contact-service-card');
      }

      if (n === 5) {
        focusTarget = document.getElementById('contactSubmitBtn') || entering.querySelector('button[type="submit"]');
      }
      if (!focusTarget) {
        focusTarget = entering.querySelector(
          'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
        );
      }
      if (focusTarget) focusTarget.focus({ preventScroll: true });

      announce(`Étape ${n} sur ${WIZARD_STEP_COUNT} : ${entering.querySelector('.contact-step__title')?.textContent || ''}`);
    }

    function updatePickedServiceBanner() {
      if (!pickedWrap || !pickedTitleEl) return;
      const slug = (serviceField && serviceField.value) || '';
      if (slug && state.selectedServiceTitle) {
        pickedTitleEl.textContent = state.selectedServiceTitle;
        if (pickedPriceEl) {
          if (state.selectedServicePrice) {
            pickedPriceEl.textContent = 'Prix : ' + state.selectedServicePrice;
            pickedPriceEl.hidden = false;
          } else {
            pickedPriceEl.textContent = '';
            pickedPriceEl.hidden = true;
          }
        }
        pickedWrap.hidden = false;
      } else {
        pickedWrap.hidden = true;
        pickedTitleEl.textContent = '';
        if (pickedPriceEl) {
          pickedPriceEl.textContent = '';
          pickedPriceEl.hidden = true;
        }
      }
    }

    function clearServiceSelectionVisual() {
      serviceMount?.querySelectorAll('.contact-service-card').forEach((btn) => {
        btn.classList.remove('is-selected');
      });
    }

    function clearProjectTypeSelectionVisual() {
      projectTypeMount?.querySelectorAll('.contact-type-chip').forEach((btn) => {
        btn.classList.remove('is-selected');
        btn.setAttribute('aria-pressed', 'false');
      });
    }

    function renderProjectTypes() {
      if (!projectTypeMount) return;
      projectTypeMount.innerHTML = '';
      const row = document.createElement('div');
      row.className = 'contact-type-chips';
      CONTACT_PROJECT_TYPES.forEach((pt) => {
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'contact-type-chip';
        btn.dataset.projectType = pt.slug;
        btn.setAttribute('aria-pressed', 'false');
        btn.setAttribute(
          'aria-label',
          `Type de projet : ${pt.label}. Sélectionner et passer à la prestation.`
        );
        btn.innerHTML =
          '<span class="contact-type-chip__icon" aria-hidden="true"><i class="fas ' +
          pt.icon +
          '"></i></span><span class="contact-type-chip__label">' +
          pt.label +
          '</span>';
        btn.addEventListener('click', () => {
          hideFeedback();
          if (projectTypeField) projectTypeField.value = pt.slug;
          clearProjectTypeSelectionVisual();
          btn.classList.add('is-selected');
          btn.setAttribute('aria-pressed', 'true');
          announce(`Type de projet : ${pt.label}.`);
          // Reset des choix précédents pour éviter de garder une prestation incompatible.
          if (serviceField) serviceField.value = '';
          if (budgetField) budgetField.value = '';
          state.selectedServiceTitle = '';
          state.selectedServicePrice = '';
          updatePickedServiceBanner();
          setStep(2);
        });
        row.appendChild(btn);
      });
      projectTypeMount.appendChild(row);
    }

    function attachServiceCardClick(btn, item) {
      btn.addEventListener('click', () => {
        hideFeedback();
        const pt = (projectTypeField && projectTypeField.value) || '';
        if (!pt) {
          showFeedback('Choisissez d’abord un type de projet.', true);
          setStep(1);
          return;
        }
        if (serviceField) serviceField.value = item.slug;
        const budgetValue = item.budget || extractBudgetValueFromHint(item.hint);
        if (budgetField) budgetField.value = budgetValue || '';
        state.selectedServiceTitle = item.title;
        state.selectedServicePrice = '';
        clearServiceSelectionVisual();
        btn.classList.add('is-selected');
        updatePickedServiceBanner();
        announce(`Prestation : ${item.title}. Choix du créneau.`);
        setStep(3);
      });
    }

    function renderServiceGrid() {
      if (!serviceMount) return;
      serviceMount.innerHTML = '';
      const selectedPt = (projectTypeField && projectTypeField.value) || '';
      const pt = CONTACT_PROJECT_TYPES.find((x) => x.slug === selectedPt) || null;
      const items = selectedPt
        ? CONTACT_SERVICE_ITEMS.filter((it) => it.tags.includes(selectedPt))
        : [];

      if (!selectedPt || !pt || !items.length) {
        const msg = document.createElement('p');
        msg.className = 'contact-step__intro';
        msg.textContent = 'Aucune offre trouvée pour ce type de projet.';
        serviceMount.appendChild(msg);
        return;
      }

      const section = document.createElement('section');
      section.className = 'contact-service-category';

      const h = document.createElement('h4');
      h.className = 'contact-service-category__title';
      h.textContent = pt.label;
      section.appendChild(h);

      const grid = document.createElement('div');
      grid.className = 'contact-service-grid';
      grid.setAttribute('role', 'list');

      items.forEach((item, cardIndex) => {
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'contact-service-card';
        btn.dataset.serviceSlug = item.slug;
        btn.style.setProperty('--contact-card-delay', `${cardIndex * 0.045}s`);
        btn.setAttribute('role', 'listitem');
        btn.setAttribute('aria-label', `${item.title}. Sélectionner et passer au créneau.`);

        const isSelected = (serviceField && serviceField.value) === item.slug;
        if (isSelected) btn.classList.add('is-selected');

        const desc = extractDescriptionFromHint(item.hint);
        const descHtml = desc ? '<span class="contact-service-card__hint">' + escapeHtml(desc) + '</span>' : '';

        btn.innerHTML =
          '<span class="contact-service-card__icon" aria-hidden="true"><i class="fas ' +
          item.icon +
          '"></i></span>' +
          '<span class="contact-service-card__title">' +
          item.title +
          '</span>' +
          descHtml +
          '<span class="contact-service-card__go" aria-hidden="true"><i class="fas fa-arrow-right"></i> Créneau</span>';

        attachServiceCardClick(btn, item);
        grid.appendChild(btn);
      });

      section.appendChild(grid);
      serviceMount.appendChild(section);
    }

    function slotToMinutes(slot) {
      const [h, m] = String(slot).split(':').map(Number);
      return h * 60 + m;
    }

    function nowMinutesLocal() {
      const now = new Date();
      return now.getHours() * 60 + now.getMinutes();
    }

    function hasAvailableTimeForDate(d) {
      if (!isSameDay(d, today)) return true;
      const nowMin = nowMinutesLocal();
      // Un créneau est disponible uniquement s'il est strictement dans le futur.
      return TIME_SLOTS.some((slot) => slotToMinutes(slot) > nowMin);
    }

    /** Au moins un jour ouvré sélectionnable dans ce mois (0–11) */
    function monthHasSelectableDays(year, month) {
      const lastDay = new Date(year, month + 1, 0).getDate();
      for (let day = 1; day <= lastDay; day++) {
        const d = new Date(year, month, day);
        if (d < today || d > maxDate || !isJourOuvre(d) || !hasAvailableTimeForDate(d)) continue;
        return true;
      }
      return false;
    }

    function renderCalendar() {
      // Si la date sélectionnée (souvent aujourd'hui) n'a plus de créneaux, on la purge.
      if (state.selectedDate) {
        const selectedDateObj = parseISODate(state.selectedDate);
        if (!hasAvailableTimeForDate(selectedDateObj)) {
          state.selectedDate = '';
          state.selectedTime = '';
          if (hiddenDate) hiddenDate.value = '';
          if (hiddenTime) hiddenTime.value = '';
          updateSummary();
        }
      }

      const y = state.viewYear;
      const m = state.viewMonth;
      calendarMonthLabel.textContent = `${MONTH_NAMES[m]} ${y}`;

      let py = y;
      let pm = m - 1;
      if (pm < 0) {
        pm = 11;
        py -= 1;
      }
      let ny = y;
      let nm = m + 1;
      if (nm > 11) {
        nm = 0;
        ny += 1;
      }
      btnPrevMonth.disabled = !monthHasSelectableDays(py, pm);
      btnNextMonth.disabled = !monthHasSelectableDays(ny, nm);

      const first = new Date(y, m, 1);
      const lastDay = new Date(y, m + 1, 0).getDate();
      const lead = mondayIndex(first);

      calendarGrid.innerHTML = '';

      for (let i = 0; i < lead; i++) {
        const cell = document.createElement('div');
        cell.className = 'calendar-cell calendar-cell--empty';
        calendarGrid.appendChild(cell);
      }

      for (let day = 1; day <= lastDay; day++) {
        const d = new Date(y, m, day);
        const iso = toISODate(d);
        const cell = document.createElement('button');
        cell.type = 'button';
        cell.className = 'calendar-day';
        cell.textContent = String(day);

        const before = d < today;
        const after = d > maxDate;
        const ouvre = isJourOuvre(d);
        const hasSlots = hasAvailableTimeForDate(d);
        const disabled = before || after || !ouvre || !hasSlots;

        if (disabled) {
          cell.classList.add('calendar-day--disabled');
          cell.disabled = true;
          cell.setAttribute('aria-disabled', 'true');
        } else {
          if (iso === state.selectedDate) {
            cell.classList.add('calendar-day--selected');
            cell.setAttribute('aria-pressed', 'true');
          } else {
            cell.setAttribute('aria-pressed', 'false');
          }
          cell.addEventListener('click', () => {
            state.selectedDate = iso;
            hiddenDate.value = iso;
            renderCalendar();
            updateSummary();
            announce(`Date sélectionnée : ${formatFrenchLong(iso)}`);
            const selectedBtn = calendarGrid.querySelector('.calendar-day--selected');
            openTimeOverlay(selectedBtn || null);
          });
        }
        calendarGrid.appendChild(cell);
      }
    }

    function renderTimeSlots() {
      timeSlotsEl.innerHTML = '';
      const hasDate = !!state.selectedDate;
      const selectedDateObj = hasDate ? parseISODate(state.selectedDate) : null;
      const isTodaySelected = !!selectedDateObj && isSameDay(selectedDateObj, today);
      const nowMin = nowMinutesLocal();
      const hasAnyFutureSlot = !!selectedDateObj && hasAvailableTimeForDate(selectedDateObj);

      TIME_SLOTS.forEach((t) => {
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'time-slot';
        const [hh, mm] = t.split(':');
        btn.textContent = `${hh}h${mm}`;

        const slotPastForToday = isTodaySelected && slotToMinutes(t) <= nowMin;
        if (!hasDate || slotPastForToday) {
          btn.disabled = true;
          btn.classList.add('time-slot--disabled');
        }
        if (t === state.selectedTime) {
          btn.classList.add('time-slot--selected');
          btn.setAttribute('aria-pressed', 'true');
        } else {
          btn.setAttribute('aria-pressed', 'false');
        }

        btn.addEventListener('click', () => {
          state.selectedTime = t;
          hiddenTime.value = t;
          timeSlotsEl.querySelectorAll('.time-slot').forEach((b) => {
            b.classList.remove('time-slot--selected');
            b.setAttribute('aria-pressed', 'false');
          });
          btn.classList.add('time-slot--selected');
          btn.setAttribute('aria-pressed', 'true');
          updateSummary();
          announce(`Créneau ${btn.textContent} sélectionné`);
          closeTimeOverlay();
        });
        timeSlotsEl.appendChild(btn);
      });

      const flex = document.createElement('button');
      flex.type = 'button';
      flex.className = 'time-slot time-slot--flex';
      flex.textContent = 'Flexible (on s’ajuste par email)';
      if (!hasDate || !hasAnyFutureSlot) {
        flex.disabled = true;
        flex.classList.add('time-slot--disabled');
      }
      if (state.selectedTime === 'flexible') {
        flex.classList.add('time-slot--selected');
        flex.setAttribute('aria-pressed', 'true');
      }
      flex.addEventListener('click', () => {
        state.selectedTime = 'flexible';
        hiddenTime.value = 'flexible';
        timeSlotsEl.querySelectorAll('.time-slot').forEach((b) => {
          b.classList.remove('time-slot--selected');
          b.setAttribute('aria-pressed', 'false');
        });
        flex.classList.add('time-slot--selected');
        flex.setAttribute('aria-pressed', 'true');
        updateSummary();
        announce('Créneau flexible sélectionné');
        closeTimeOverlay();
      });
      timeSlotsEl.appendChild(flex);
    }

    timeOverlayBackdrop?.addEventListener('click', () => closeTimeOverlay());
    timeOverlayClose?.addEventListener('click', () => closeTimeOverlay());

    btnPrevMonth.addEventListener('click', () => {
      closeTimeOverlay();
      let y = state.viewYear;
      let m = state.viewMonth - 1;
      if (m < 0) {
        m = 11;
        y -= 1;
      }
      if (!monthHasSelectableDays(y, m)) return;
      state.viewYear = y;
      state.viewMonth = m;
      renderCalendar();
    });

    btnNextMonth.addEventListener('click', () => {
      closeTimeOverlay();
      let y = state.viewYear;
      let m = state.viewMonth + 1;
      if (m > 11) {
        m = 0;
        y += 1;
      }
      if (!monthHasSelectableDays(y, m)) return;
      state.viewYear = y;
      state.viewMonth = m;
      renderCalendar();
    });

    function validateStepProjectType() {
      const pt = (projectTypeField && projectTypeField.value) || '';
      if (!pt) {
        showFeedback('Choisissez un type de projet.', true);
        return false;
      }
      hideFeedback();
      return true;
    }

    function validateStepPrestation() {
      const v = (serviceField && serviceField.value) || '';
      if (!v) {
        showFeedback('Choisissez une prestation dans la liste.', true);
        return false;
      }
      hideFeedback();
      return true;
    }

    function validateStepCalendar() {
      if (!state.selectedDate || !hiddenDate.value) {
        showFeedback('Veuillez choisir un jour ouvré (hors week-ends et jours fériés) dans le calendrier.', true);
        return false;
      }
      if (!state.selectedTime || !hiddenTime.value) {
        showFeedback('Veuillez choisir un créneau horaire ou l’option flexible.', true);
        return false;
      }
      hideFeedback();
      return true;
    }

    function validateStepCoords() {
      const name = (form.querySelector('#name')?.value || '').trim();
      const email = (form.querySelector('#email')?.value || '').trim();
      const phone = (form.querySelector('#phone')?.value || '').trim();

      if (!name || !email || !phone) {
        showFeedback('Nom, email et téléphone sont obligatoires.', true);
        return false;
      }
      hideFeedback();
      return true;
    }

    btnChangeService?.addEventListener('click', () => {
      hideFeedback();
      setStep(2);
    });

    wizardBackFromService?.addEventListener('click', () => {
      hideFeedback();
      setStep(1);
    });

    wizardBackFromCalendar?.addEventListener('click', () => {
      hideFeedback();
      setStep(2);
    });

    wizardNextFromCalendar?.addEventListener('click', () => {
      if (!validateStepCalendar()) return;
      setStep(4);
    });

    wizardBackFromCoords?.addEventListener('click', () => {
      hideFeedback();
      setStep(3);
    });

    async function sendContactRequest() {
      if (state.sending) return;
      state.sending = true;

      // Backend exige un message non vide : on le génère à partir des choix.
      if (messageEl) {
        const current = (messageEl.value || '').trim();
        if (!current) messageEl.value = buildAutoMessage();
      }

      hideFeedback();
      closeErrorOverlay();
      setValidationStatus('pending');
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.classList.add('is-loading');
      }

      const formData = new FormData(form);

      try {
        const res = await fetch('/api/send-contact.php', {
          method: 'POST',
          body: formData
        });
        const data = await res.json().catch(() => ({}));

        if (
          (res.status === 501 || res.status === 405) &&
          /^https?:\/\/(127\.0\.0\.1|localhost)(:\d+)?$/i.test(window.location.origin)
        ) {
          const err = buildErrorOverlayContent({ error: MSG_STATIC_SERVER }, res.status);
          setValidationStatus('idle');
          openErrorOverlay(err.message, err.tips);
          setStep(4);
        } else if (res.ok && data.success) {
          closeTimeOverlay();
          hideFeedback();
          setValidationStatus('success');
          setStep(5);
        } else {
          setValidationStatus('idle');
          const err = buildErrorOverlayContent(data, res.status);
          openErrorOverlay(err.message, err.tips);
          setStep(4);
        }
      } catch (err) {
        setValidationStatus('idle');
        openErrorOverlay(
          'Impossible de contacter le serveur pour envoyer la demande.',
          [
            'Vérifiez votre connexion Internet.',
            'En local : vérifiez que le serveur PHP est bien démarré.',
            'Réessayez ensuite.'
          ]
        );
        setStep(4);
      } finally {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.classList.remove('is-loading');
        }
        state.sending = false;
      }
    }

    wizardNextFromCoords?.addEventListener('click', () => {
      if (!validateStepCoords()) return;
      hideFeedback();
      setStep(5);
      sendContactRequest();
    });

    wizardBackFromMessage?.addEventListener('click', () => {
      hideFeedback();
      setStep(4);
    });
    errorOverlayBackdrop?.addEventListener('click', closeErrorOverlay);
    errorOverlayClose?.addEventListener('click', closeErrorOverlay);

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      if (!validateStepProjectType()) {
        setStep(1);
        return;
      }
      if (!validateStepPrestation()) {
        setStep(2);
        return;
      }
      if (!validateStepCalendar()) {
        setStep(3);
        return;
      }
      if (!validateStepCoords()) {
        setStep(4);
        return;
      }
      await sendContactRequest();
    });

    renderProjectTypes();
    renderCalendar();
    renderTimeSlots();
    updateSummary();
    updatePickedServiceBanner();
    setValidationStatus('idle');
    updateProgress();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
