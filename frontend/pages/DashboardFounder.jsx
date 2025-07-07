import React, { useEffect, useState } from "react";
import AdaptiveLayout from "../components/AdaptiveLayout";

const kpiStyle = "bg-black/70 text-gold rounded-xl shadow px-6 py-4 text-center m-2 flex flex-col items-center";

const DashboardFounder = ({ worldId }) => {
  const [metrics, setMetrics] = useState(null);

  useEffect(() => {
    fetch(`/api/analytics/overview?world_id=${worldId}`).then(r => r.json()).then(setMetrics);
  }, [worldId]);

  if (!metrics) return <div>Caricamento dati…</div>;

  return (
    <AdaptiveLayout>
      <h1 className="text-3xl font-bold text-gold mb-8">Dashboard Founder</h1>
      <div className="grid grid-cols-2 md:grid-cols-4 gap-6 mb-8">
        <div className={kpiStyle}>
          <div className="text-xl font-bold">{metrics.users.total_users}</div>
          <div className="text-sm text-white/70">Utenti Totali</div>
        </div>
        <div className={kpiStyle}>
          <div className="text-xl font-bold">{metrics.users.new_users_last_7d}</div>
          <div className="text-sm text-white/70">Nuovi ultimi 7gg</div>
        </div>
        <div className={kpiStyle}>
          <div className="text-xl font-bold">{metrics.users.active_users}</div>
          <div className="text-sm text-white/70">Utenti Attivi</div>
        </div>
        <div className={kpiStyle}>
          <div className="text-xl font-bold">€{metrics.revenue.total_revenue.toLocaleString()}</div>
          <div className="text-sm text-white/70">Revenue Totale</div>
        </div>
        <div className={kpiStyle}>
          <div className="text-xl font-bold">€{metrics.revenue.monthly_revenue.toLocaleString()}</div>
          <div className="text-sm text-white/70">Revenue Mese</div>
        </div>
        <div className={kpiStyle}>
          <div className="text-xl font-bold">{metrics.agents.total_agents}</div>
          <div className="text-sm text-white/70">Agent Totali</div>
        </div>
        <div className={kpiStyle}>
          <div className="text-xl font-bold">{metrics.agents.active_agents}</div>
          <div className="text-sm text-white/70">Agent Attivi</div>
        </div>
        <div className={kpiStyle}>
          <div className="text-xl font-bold">{metrics.impact.positive_feedback}</div>
          <div className="text-sm text-white/70">Feedback Positivi</div>
        </div>
      </div>
      <div className="bg-white/5 p-6 rounded-2xl mt-6">
        <h2 className="text-xl text-gold mb-4">Net Promoter Score (NPS)</h2>
        <div className="text-2xl text-cyan-400">{metrics.impact.nps_score.toFixed(1)}%</div>
        <div className="text-white/70 text-xs">Clienti promuovono la tua AI? Più è alto, più il tuo mondo evolve.</div>
      </div>
    </AdaptiveLayout>
  );
};

export default DashboardFounder;
