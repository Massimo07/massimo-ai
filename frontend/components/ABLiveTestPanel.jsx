import React from "react";

const ABLiveTestPanel = () => (
  <div className="bg-gradient-to-r from-violet-900 via-cyan-700 to-black rounded-2xl p-4 shadow-xl mb-6">
    <h2 className="text-xl font-semibold text-gold mb-2">A/B Live Test</h2>
    <div className="text-white text-sm">
      <p>
        Avvia A/B test in tempo reale su nuove funzioni, onboarding, testi, o strategie di agenti.  
        <span className="block text-xs text-cyan-400 mt-1">(*Configura i test dal backend founder.)</span>
      </p>
    </div>
  </div>
);

export default ABLiveTestPanel;
