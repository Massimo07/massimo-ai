import React, { useEffect, useState } from "react";
import AdaptiveLayout from "../components/AdaptiveLayout";

const AutomationCenter = ({ worldId }) => {
  const [automations, setAutomations] = useState([]);
  const [agents, setAgents] = useState([]);
  const [newAuto, setNewAuto] = useState({ trigger: "", actions: [] });

  useEffect(() => {
    fetch(`/api/automations?world_id=${worldId}`).then(r => r.json()).then(setAutomations);
    fetch(`/api/agents?world_id=${worldId}`).then(r => r.json()).then(setAgents);
  }, [worldId]);

  const addAutomation = async () => {
    await fetch("/api/automations/add", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ world_id: worldId, automation: newAuto }),
    });
    setAutomations([...automations, newAuto]);
    setNewAuto({ trigger: "", actions: [] });
  };

  return (
    <AdaptiveLayout>
      <h1 className="text-2xl text-gold mb-4">Centro Automazioni & Agent</h1>
      <div className="mb-6">
        <h2 className="text-lg text-cyan-400">Automazioni attive</h2>
        <ul>
          {automations.map((a, i) => (
            <li key={i} className="mb-1">
              <b>{a.trigger}</b> → Azioni: {a.actions.map(act => act.type).join(", ")}
            </li>
          ))}
        </ul>
      </div>
      <div className="mb-6">
        <h2 className="text-lg text-cyan-400">Nuova Automazione</h2>
        <input className="input mb-2" placeholder="Trigger"
          value={newAuto.trigger} onChange={e => setNewAuto({ ...newAuto, trigger: e.target.value })} />
        <input className="input mb-2" placeholder="Azione (es: send_email)"
          onBlur={e => setNewAuto({ ...newAuto, actions: [{ type: e.target.value }] })} />
        <button className="btn" onClick={addAutomation}>Aggiungi Automazione</button>
      </div>
      <div>
        <h2 className="text-lg text-gold">Agent disponibili</h2>
        <ul>
          {agents.map(a => (
            <li key={a.id} className="mb-2">
              <b>{a.name}</b> – Skill: {a.skills.join(", ")} – Stato: {a.status}
            </li>
          ))}
        </ul>
      </div>
    </AdaptiveLayout>
  );
};

export default AutomationCenter;
