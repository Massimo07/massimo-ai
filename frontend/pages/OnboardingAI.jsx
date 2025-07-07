// Massimo AI – OnboardingAI.jsx
import React, { useState } from "react";
import { useLang } from "../i18n";
export default function OnboardingAI({ onComplete }) {
  const { t } = useLang();
  const [step, setStep] = useState(0);
  const steps = [
    { title: t("Scegli avatar"), content: "Avatar picker qui (con IA)" },
    { title: t("Quiz iniziale"), content: "Micro quiz + test motivazionale" },
    { title: t("Scegli sponsor"), content: "Seleziona sponsor/team" },
    { title: t("Setup livello"), content: "Scegli potenza AI e livello servizi" },
    { title: t("Pronto!"), content: "Benvenuto nel tuo mondo Massimo AI" },
  ];
  return (
    <div className="max-w-lg mx-auto p-6 bg-white rounded-xl shadow-xl">
      <h2 className="text-xl font-bold mb-4">{steps[step].title}</h2>
      <div className="mb-4">{steps[step].content}</div>
      <button
        className="px-4 py-2 bg-violet-700 text-white rounded-xl"
        onClick={() => step < steps.length - 1 ? setStep(step + 1) : onComplete()}
      >
        {step < steps.length - 1 ? t("Avanti") : t("Entra nel mondo AI")}
      </button>
    </div>
  );
}
