'use client';

import i18n from 'i18next';
import LanguageDetector from 'i18next-browser-languagedetector';
import { initReactI18next } from 'react-i18next';

i18n
  .use(LanguageDetector) // Detecta automáticamente el idioma del navegador
  .use(initReactI18next) // Integra con React
  .init({
    debug: true, // Habilita mensajes de depuración en la consola
    fallbackLng: 'es', // Idioma predeterminado
    interpolation: {
      escapeValue: false, // React ya se encarga de escapar valores
    },
    detection: {
      order: ['navigator', 'querystring', 'localStorage', 'cookie'], // Orden de detección
      caches: ['localStorage', 'cookie'], // Lugares donde guardar el idioma detectado
    },
    resources: {
      es: {
        translation: require('../locales/es.json'),
      },
      en: {
        translation: require('../locales/en.json'),
      },
      fr: {
        translation: require('../locales/fr.json'),
      },
      de: {
        translation: require('../locales/de.json'),
      },
      pt: {
        translation: require('../locales/pt.json'),
      },
    },
  });

export default i18n;