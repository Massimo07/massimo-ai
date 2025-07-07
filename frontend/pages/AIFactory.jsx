import React, { useState } from "react";
import AdaptiveLayout from "../components/AdaptiveLayout";

const AIFactory = () => {
  const [prompt, setPrompt] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleCreate = async () => {
    setLoading(true);
    const res = await fetch("/api/factory/create", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt }),
    });
    const data = await res.json();
    setResult(data);
    setLoading(false);
  };

  return (
    <AdaptiveLayout>
      <h1 className="text-3xl font-extrabold mb-4">AI Factory</h1>
      <p className="mb-6 text-lg text-white/80">
        Scrivi il tuo sogno, esigenza o settore e genera <b>istantaneamente</b> il tuo mondo digitale!
      </p>
      <div className="flex gap-4 mb-6">
        <input
          value={prompt}
          onChange={e => setPrompt(e.target.value)}
          className="flex-1 p-3 rounded-xl border-2 border-gold bg-black text-gold text-lg focus:outline-none"
          placeholder='Es: "No, voglio un Massimo AI per... la mia scuola di inglese"'
        />
        <button
          onClick={handleCreate}
          disabled={loading || !prompt}
          className="px-5 py-3 rounded-xl bg-gradient-to-r from-cyan-400 via-violet-600 to-orange-400 text-white font-bold shadow-lg hover:scale-105 transition"
        >
          {loading ? "Sto generando…" : "Crea il tuo mondo AI"}
        </button>
      </div>
      {result && (
        <div className="mt-8 bg-black/70 border-2 border-gold rounded-2xl p-6 text-white shadow-xl">
          <h2 className="text-2xl font-bold text-gold mb-2">Risultato</h2>
          <pre className="whitespace-pre-wrap text-base">{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </AdaptiveLayout>
  );
};

export default AIFactory;
