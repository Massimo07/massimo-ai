import React, { useEffect, useState } from "react";
import AdaptiveLayout from "../components/AdaptiveLayout";

const WorldOnboarding = ({ worldId }) => {
  const [world, setWorld] = useState(null);

  useEffect(() => {
    fetch(`/api/worlds/${worldId}`)
      .then((r) => r.json())
      .then(setWorld);
  }, [worldId]);

  if (!world) return <AdaptiveLayout><p>Caricamento…</p></AdaptiveLayout>;

  return (
    <AdaptiveLayout>
      <h1 className="text-2xl text-gold font-extrabold mb-4">
        Benvenuto in {world.name}!
      </h1>
      <div className="bg-black/70 border-2 border-gold rounded-2xl p-6 mb-6 shadow-lg">
        <p className="text-lg mb-3">Ecco cosa puoi fare da subito:</p>
        <ul className="mb-4 list-disc pl-6">
          {world.functions.map((f, i) => (
            <li key={i} className="text-gold text-base mb-1">{f}</li>
          ))}
        </ul>
        <p className="text-white mb-3">Vuoi personalizzare le funzioni del tuo mondo?</p>
        <button
          onClick={() => alert("Personalizzazione avanzata in arrivo!")}
          className="px-4 py-2 rounded-xl bg-gold text-black font-bold shadow hover:scale-105 transition"
        >
          Personalizza ora
        </button>
      </div>
      <div className="bg-black/50 p-5 rounded-xl shadow">
        <p className="text-xs text-cyan-300">
          {world.onboarding_status === "Pronto"
            ? "Il tuo mondo è già attivo. Puoi invitare altri, connettere plugin, gestire abbonamenti e molto altro!"
            : "Onboarding in corso…"}
        </p>
      </div>
    </AdaptiveLayout>
  );
};

export default WorldOnboarding;
