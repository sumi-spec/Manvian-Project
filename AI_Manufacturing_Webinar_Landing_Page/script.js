/**
 * MANVIAN - AI for Manufacturing Webinar Landing Page
 * Interactive Logic, Form Validation, LocalStorage Caching & Calendar Generation
 */

document.addEventListener('DOMContentLoaded', () => {
  initNavbar();
  initCountdown();
  initSmoothScroll();
  initAgendaAccordion();
  initFaqAccordion();
  initRegistrationForm();
  initModal();
});

/* ==========================================================================
   1. Navbar & Mobile Drawer
   ========================================================================== */
function initNavbar() {
  const navbar = document.getElementById('navbar');
  const mobileToggle = document.getElementById('mobileToggle');
  const mobileDrawer = document.getElementById('mobileDrawer');
  const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');

  // Sticky background on scroll
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }, { passive: true });

  // Toggle mobile drawer
  if (mobileToggle && mobileDrawer) {
    mobileToggle.addEventListener('click', () => {
      const isOpen = mobileDrawer.classList.toggle('active');
      mobileToggle.setAttribute('aria-expanded', isOpen);
      mobileToggle.innerHTML = isOpen
        ? `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>`
        : `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>`;
    });

    // Close mobile drawer when clicking nav links
    mobileNavLinks.forEach(link => {
      link.addEventListener('click', () => {
        mobileDrawer.classList.remove('active');
        mobileToggle.setAttribute('aria-expanded', 'false');
        mobileToggle.innerHTML = `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>`;
      });
    });
  }
}

/* ==========================================================================
   2. Countdown Timer
   ========================================================================== */
function initCountdown() {
  const daysEl = document.getElementById('timerDays');
  const hoursEl = document.getElementById('timerHours');
  const minsEl = document.getElementById('timerMinutes');
  const secsEl = document.getElementById('timerSeconds');

  if (!daysEl || !hoursEl || !minsEl || !secsEl) return;

  // Set webinar target date: December 10, 2026, 14:00 EST (19:00 UTC)
  const targetDate = new Date('2026-12-10T14:00:00-05:00').getTime();

  function updateTimer() {
    const now = new Date().getTime();
    let difference = targetDate - now;

    // Fallback if target date passed: set 14 days ahead for continuous demo
    if (difference <= 0) {
      difference = 14 * 24 * 60 * 60 * 1000;
    }

    const days = Math.floor(difference / (1000 * 60 * 60 * 24));
    const hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((difference % (1000 * 60)) / 1000);

    daysEl.textContent = String(days).padStart(2, '0');
    hoursEl.textContent = String(hours).padStart(2, '0');
    minsEl.textContent = String(minutes).padStart(2, '0');
    secsEl.textContent = String(seconds).padStart(2, '0');
  }

  updateTimer();
  setInterval(updateTimer, 1000);
}

/* ==========================================================================
   3. Smooth Scroll & CTA Focus
   ========================================================================== */
function initSmoothScroll() {
  const registerTriggers = document.querySelectorAll('.js-register-trigger');
  const nameInput = document.getElementById('fullName');

  registerTriggers.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const target = document.getElementById('register');
      if (target) {
        target.scrollIntoView({ behavior: 'smooth' });
        setTimeout(() => {
          if (nameInput) nameInput.focus();
        }, 500);
      }
    });
  });
}

/* ==========================================================================
   4. Agenda Interactive Accordion
   ========================================================================== */
function initAgendaAccordion() {
  const agendaCards = document.querySelectorAll('.agenda-card');

  agendaCards.forEach(card => {
    card.addEventListener('click', () => {
      const isAlreadyActive = card.classList.contains('active');

      // Close other cards
      agendaCards.forEach(otherCard => {
        otherCard.classList.remove('active');
        otherCard.setAttribute('aria-expanded', 'false');
      });

      // Toggle clicked card
      if (!isAlreadyActive) {
        card.classList.add('active');
        card.setAttribute('aria-expanded', 'true');
      }
    });

    // Support keyboard Enter / Space
    card.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        card.click();
      }
    });
  });
}

/* ==========================================================================
   5. FAQ Interactive Accordion
   ========================================================================== */
function initFaqAccordion() {
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question');
    if (!questionBtn) return;

    questionBtn.addEventListener('click', () => {
      const isActive = item.classList.contains('active');

      // Close all other FAQs
      faqItems.forEach(otherItem => {
        otherItem.classList.remove('active');
        const btn = otherItem.querySelector('.faq-question');
        if (btn) btn.setAttribute('aria-expanded', 'false');
      });

      // Toggle selected
      if (!isActive) {
        item.classList.add('active');
        questionBtn.setAttribute('aria-expanded', 'true');
      }
    });
  });
}

/* ==========================================================================
   6. Form Validation & Client-Side Registration Persistence
   ========================================================================== */
function initRegistrationForm() {
  const form = document.getElementById('webinarRegistrationForm');
  if (!form) return;

  const fullName = document.getElementById('fullName');
  const workEmail = document.getElementById('workEmail');
  const phoneNumber = document.getElementById('phoneNumber');
  const designation = document.getElementById('designation');
  const companyName = document.getElementById('companyName');
  const industrySector = document.getElementById('industrySector');
  const submitBtn = document.getElementById('submitBtn');

  // Input real-time validation listeners
  fullName.addEventListener('input', () => validateField(fullName, validateName));
  workEmail.addEventListener('input', () => validateField(workEmail, validateEmail));
  phoneNumber.addEventListener('input', () => validateField(phoneNumber, validatePhone));
  designation.addEventListener('change', () => validateField(designation, validateRequiredSelect));

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const isNameValid = validateField(fullName, validateName);
    const isEmailValid = validateField(workEmail, validateEmail);
    const isPhoneValid = validateField(phoneNumber, validatePhone);
    const isDesignationValid = validateField(designation, validateRequiredSelect);

    if (!isNameValid || !isEmailValid || !isPhoneValid || !isDesignationValid) {
      // Find first invalid input and focus
      const firstInvalid = form.querySelector('.form-group.has-error input, .form-group.has-error select');
      if (firstInvalid) firstInvalid.focus();
      return;
    }

    // Submit state animation
    submitBtn.disabled = true;
    const originalText = submitBtn.innerHTML;
    submitBtn.innerHTML = `
      <svg class="animate-spin" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="animation: spin 1s linear infinite;">
        <circle cx="12" cy="12" r="10" stroke-opacity="0.25"></circle>
        <path d="M12 2a10 10 0 0 1 10 10" stroke="currentColor"></path>
      </svg>
      Securing Your Seat...
    `;

    setTimeout(() => {
      // Generate registration record
      const regId = 'MNV-' + Math.floor(100000 + Math.random() * 900000);
      const registrationData = {
        id: regId,
        fullName: fullName.value.trim(),
        workEmail: workEmail.value.trim(),
        phoneNumber: phoneNumber.value.trim(),
        designation: designation.value,
        companyName: companyName ? companyName.value.trim() : 'N/A',
        industrySector: industrySector ? industrySector.value : 'General Manufacturing',
        registeredAt: new Date().toISOString()
      };

      // Store in LocalStorage (client-side demo state)
      saveRegistrationLocally(registrationData);

      // Reset button
      submitBtn.disabled = false;
      submitBtn.innerHTML = originalText;

      // Reset Form
      form.reset();
      clearErrors(form);

      // Open Success Modal
      showConfirmationModal(registrationData);
    }, 900);
  });
}

function validateField(inputElement, validationFn) {
  const group = inputElement.closest('.form-group');
  const errorMsg = group.querySelector('.field-error-msg');
  const result = validationFn(inputElement.value.trim());

  if (!result.isValid) {
    group.classList.add('has-error');
    inputElement.classList.add('error');
    inputElement.setAttribute('aria-invalid', 'true');
    if (errorMsg) errorMsg.textContent = result.message;
    return false;
  } else {
    group.classList.remove('has-error');
    inputElement.classList.remove('error');
    inputElement.removeAttribute('aria-invalid');
    if (errorMsg) errorMsg.textContent = '';
    return true;
  }
}

function validateName(value) {
  if (!value) return { isValid: false, message: 'Full name is required.' };
  if (value.length < 2) return { isValid: false, message: 'Please enter at least 2 characters.' };
  if (!/^[a-zA-Z\s.'-]+$/.test(value)) return { isValid: false, message: 'Name contains invalid characters.' };
  return { isValid: true };
}

function validateEmail(value) {
  if (!value) return { isValid: false, message: 'Work email address is required.' };
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
  if (!emailRegex.test(value)) return { isValid: false, message: 'Please enter a valid business email address.' };
  return { isValid: true };
}

function validatePhone(value) {
  if (!value) return { isValid: false, message: 'Phone number is required.' };
  // Allows digits, spaces, dashes, parentheses, plus sign, min 7 digits
  const cleanDigits = value.replace(/\D/g, '');
  if (cleanDigits.length < 7 || cleanDigits.length > 15) {
    return { isValid: false, message: 'Please enter a valid phone number (7-15 digits).' };
  }
  return { isValid: true };
}

function validateRequiredSelect(value) {
  if (!value || value === '') {
    return { isValid: false, message: 'Please select your professional designation.' };
  }
  return { isValid: true };
}

function clearErrors(form) {
  form.querySelectorAll('.form-group').forEach(grp => grp.classList.remove('has-error'));
  form.querySelectorAll('.form-input, .form-select').forEach(el => {
    el.classList.remove('error');
    el.removeAttribute('aria-invalid');
  });
}

function saveRegistrationLocally(record) {
  try {
    const existing = JSON.parse(localStorage.getItem('manvian_webinar_registrations') || '[]');
    existing.unshift(record);
    localStorage.setItem('manvian_webinar_registrations', JSON.stringify(existing));
    console.info(`[MANVIAN] Successfully saved registration ${record.id} in localStorage.`);
  } catch (err) {
    console.warn('[MANVIAN] LocalStorage error:', err);
  }
}

/* ==========================================================================
   7. Confirmation Modal & Calendar Download (.ics)
   ========================================================================== */
function initModal() {
  const modal = document.getElementById('confirmationModal');
  const closeBtn = document.getElementById('modalCloseBtn');
  const downloadIcsBtn = document.getElementById('downloadCalendarBtn');

  if (closeBtn && modal) {
    closeBtn.addEventListener('click', () => closeModal(modal));
    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeModal(modal);
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modal.classList.contains('active')) {
        closeModal(modal);
      }
    });
  }

  if (downloadIcsBtn) {
    downloadIcsBtn.addEventListener('click', () => {
      generateAndDownloadIcs();
    });
  }
}

function showConfirmationModal(data) {
  const modal = document.getElementById('confirmationModal');
  if (!modal) return;

  const ticketIdEl = document.getElementById('modalTicketId');
  const attendeeNameEl = document.getElementById('modalAttendeeName');
  const attendeeEmailEl = document.getElementById('modalAttendeeEmail');
  const attendeeRoleEl = document.getElementById('modalAttendeeRole');

  if (ticketIdEl) ticketIdEl.textContent = data.id;
  if (attendeeNameEl) attendeeNameEl.textContent = data.fullName;
  if (attendeeEmailEl) attendeeEmailEl.textContent = data.workEmail;
  if (attendeeRoleEl) attendeeRoleEl.textContent = data.designation;

  modal.classList.add('active');
  modal.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';
}

function closeModal(modal) {
  modal.classList.remove('active');
  modal.setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
}

function generateAndDownloadIcs() {
  const icsContent = [
    'BEGIN:VCALENDAR',
    'VERSION:2.0',
    'PRODID:-//MANVIAN Inc//AI for Manufacturing Webinar//EN',
    'CALSCALE:GREGORIAN',
    'METHOD:REQUEST',
    'BEGIN:VEVENT',
    'UID:manvian-webinar-2026-dec10@manvian.com',
    'DTSTAMP:20261124T000000Z',
    'DTSTART:20261210T190000Z',
    'DTEND:20261210T210000Z',
    'SUMMARY:MANVIAN Webinar: Transform Manufacturing with Artificial Intelligence',
    'DESCRIPTION:Exclusive 2-Hour Masterclass on AI in Manufacturing\\nTopics: Predictive Maintenance\\, Computer Vision Inspection\\, Smart Factory Orchestration\\, and ROI Frameworks.\\n\\nAccess Link: https://manvian.com/live-room',
    'LOCATION:MANVIAN Virtual Auditorium (Live Stream)',
    'STATUS:CONFIRMED',
    'END:VEVENT',
    'END:VCALENDAR'
  ].join('\r\n');

  const blob = new Blob([icsContent], { type: 'text/calendar;charset=utf-8' });
  const url = window.URL.createObjectURL(blob);
  const tempLink = document.createElement('a');
  tempLink.href = url;
  tempLink.setAttribute('download', 'MANVIAN-AI-Manufacturing-Webinar.ics');
  document.body.appendChild(tempLink);
  tempLink.click();
  document.body.removeChild(tempLink);
  window.URL.revokeObjectURL(url);
}

// Keyframes CSS animation helper
const styleSheet = document.createElement("style");
styleSheet.innerText = `
  @keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
  }
`;
document.head.appendChild(styleSheet);
