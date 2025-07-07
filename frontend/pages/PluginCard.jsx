import React from "react";

const PluginCard = ({ plugin }) => {
  const handleInstall = async () => {
    await fetch("/api/plugins/install", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name: plugin.name }),
    });
    alert("Plugin installato!");
  };

  return (
    <div className="bg-gradient-to-br from-black via-violet-800 to-cyan-950 rounded-2xl shadow-xl p-6 flex flex-col justify-between border-2 border-gold">
      <div>
        <h2 className="text-xl text-gold font-semibold mb-1">{plugin.name}</h2>
        <p className="text-white mb-2">{plugin.description}</p>
        <span className="text-xs text-cyan-400">{plugin.type}</span>
      </div>
      <button
        onClick={handleInstall}
        className="mt-4 px-4 py-2 rounded-xl bg-gold text-black font-bold shadow hover:scale-105 transition"
      >
        Installa
      </button>
    </div>
  );
};

export default PluginCard;
