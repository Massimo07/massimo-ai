import React, { useEffect, useState } from "react";
import AdaptiveLayout from "../components/AdaptiveLayout";

const PluginStore = ({ worldId }) => {
  const [plugins, setPlugins] = useState([]);
  const [installed, setInstalled] = useState([]);

  useEffect(() => {
    fetch("/api/plugins").then(r => r.json()).then(setPlugins);
    // Qui fetch dei plugin già installati su questo mondo (API aggiuntiva)
    // fetch(`/api/worlds/${worldId}`).then(r => r.json()).then(w => setInstalled(w.plugins || []));
  }, [worldId]);

  const install = async (plugin_key) => {
    await fetch("/api/plugins/install", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ world_id: worldId, plugin_key }),
    });
    setInstalled([...installed, plugin_key]);
  };

  return (
    <AdaptiveLayout>
      <h1 className="text-2xl text-gold mb-4">Plugin Store</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {plugins.map((p) => (
          <div key={p.name} className="rounded-2xl bg-white/5 p-4 shadow">
            <div className="text-xl text-cyan-400 font-bold mb-2">{p.name}</div>
            <div className="text-white/80 mb-2">{p.description}</div>
            <div className="text-xs text-gold mb-3">{p.category}</div>
            <button
              className={`btn ${installed.includes(p.name) ? "opacity-50 pointer-events-none" : ""}`}
              onClick={() => install(p.name)}
            >
              {installed.includes(p.name) ? "Installato" : "Installa"}
            </button>
          </div>
        ))}
      </div>
    </AdaptiveLayout>
  );
};

export default PluginStore;
