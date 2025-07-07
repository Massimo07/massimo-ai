// /frontend/i18n/index.js
import it from "./it";
import en from "./en";
import es from "./es";
import fr from "./fr";
import de from "./de";

const LANGS = { it, en, es, fr, de };

export function getTranslation(lang = "it", key, fallback = "") {
  const dict = LANGS[lang] || LANGS["it"];
  return dict[key] || fallback || key;
}

// Hook React per usare le traduzioni in ogni componente
import { useState, useEffect } from "react";

export function useLang(defaultLang = "it") {
  const [lang, setLang] = useState(() => {
    if (typeof window !== "undefined") {
      // Rileva preferenza browser o localStorage
      return localStorage.getItem("lang") ||
        navigator.language.slice(0, 2) ||
        defaultLang;
    }
    return defaultLang;
  });

  useEffect(() => {
    if (typeof window !== "undefined") {
      localStorage.setItem("lang", lang);
    }
  }, [lang]);

  // Per tradurre velocemente: t("chiave")
  function t(key, fallback = "") {
    return getTranslation(lang, key, fallback);
  }

  return { lang, setLang, t };
}
