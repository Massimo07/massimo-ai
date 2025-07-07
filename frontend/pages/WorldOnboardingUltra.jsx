import React, { useEffect, useState } from "react";
import AdaptiveLayout from "../components/AdaptiveLayout";

const WorldOnboardingUltra = ({ worldId }) => {
  const [world, setWorld] = useState(null);
  const [step, setStep] = useState(1);
  const [choice, setChoice] = useState("");
  const [invite, setInvite] = useState("");
  const [invited, setInvited] = useState([]);
  const [badges, setBadges] = useState([]);
  const [branding, setBranding] = useState(null);

  useEffect(() => {
    fetch(`/api/worlds/${worldId}`).then(r => r.json()).then(data => {
      setWorld(data);
      setBadges(data.badges || []);
      setBranding(data.branding || {});
    });
  }, [worldId]);

  // Step 1: Saluto e scelta obiettivo
  if (step === 1 && world)
    return (
      <AdaptiveLayout>
        <h1 className="text-2xl text-gold font-bold mb-4">Benvenuto in {world.name}!</h1>
        <p className="mb-2">Cosa vuoi ottenere subito?</p>
        <ul className="mb-4">
          <li><button className="btn" onClick={() => { setChoice("Crescita personale"); setStep(2); }}>Crescita personale</button></li>
          <li><button className="btn" onClick={() => { setChoice("Automazione business"); setStep(2); }}>Automazione business</button></li>
          <li><button className="btn" onClick={() => { setChoice("Supporto emotivo"); setStep(2); }}>Supporto emotivo</button></li>
          <li>
            <input className="input" placeholder="Altro (scrivi…)" onBlur={e => { setChoice(e.target.value); setStep(2); }} />
          </li>
        </ul>
      </AdaptiveLayout>
    );
  // Step 2: Inviti
  if (step === 2)
    return (
      <AdaptiveLayout>
        <h2 className="text-xl text-cyan-400 mb-2">Vuoi invitare subito qualcuno?</h2>
        <input className="input" value={invite} onChange={e => setInvite(e.target.value)} placeholder="Email collaboratore" />
        <button
          className="btn"
          onClick={async () => {
            const res = await fetch("/api/invite", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ email: invite, world_id: world.id, inviter: "Founder" })
            });
            const data = await res.json();
            setInvited([...invited, data.email]);
            setInvite("");
            setStep(3);
          }}
        >Invia invito</button>
        {invited.length > 0 && <div className="mt-2 text-gold">Invitati: {invited.join(", ")}</div>}
        <button className="btn mt-4" onClick={() => setStep(3)}>Salta</button>
      </AdaptiveLayout>
    );
  // Step 3: Badge e branding
  if (step === 3)
    return (
      <AdaptiveLayout>
        <h2 className="text-xl text-gold mb-2">Il tuo badge Founder è attivo!</h2>
        <div>
          {badges.map(badge => <span key={badge} className="badge mx-2">{badge}</span>)}
        </div>
        <div className="my-4">
          <img src={branding?.logo_url} alt="Logo AI" style={{ height: 80, borderRadius: 16, border: "2px solid #FFD85C" }} />
          <div style={{ background: branding?.primary_color, color: "#000", padding: "8px 18px", borderRadius: 12, marginTop: 8 }}>
            Color principale: {branding?.primary_color}
          </div>
          <div className="mt-1 text-xs text-white/70">Claim: {branding?.claim}</div>
        </div>
        <button className="btn" onClick={() => setStep(4)}>Continua</button>
      </AdaptiveLayout>
    );
  // Step 4: Collegamento dashboard, agent, automazioni, quiz
  if (step === 4)
    return (
      <AdaptiveLayout>
        <h2 className="text-lg text-cyan-400 mb-3">Il tuo mondo è pronto!</h2>
        <div className="flex flex-col gap-3 mt-4">
          <a href={world.dashboard_url} className="btn">Vai alla Dashboard</a>
          <a href={`/agents/${world.id}`} className="btn">Gestisci Agent</a>
          <a href={`/automations/${world.id}`} className="btn">Automazioni</a>
          <a href={`/plugins/${world.id}`} className="btn">Plugin Store</a>
        </div>
        <div className="mt-5">
          <video src={world.tutorial_video_url} controls autoPlay className="rounded-2xl my-4" />
        </div>
        <button className="btn" onClick={() => setStep(5)}>Avanti: Quiz onboarding</button>
      </AdaptiveLayout>
    );
  // Step 5: Quiz onboarding/feedback
  if (step === 5)
    return (
      <AdaptiveLayout>
        <h2 className="text-lg text-gold mb-2">Quiz onboarding</h2>
        <ul>
          {world?.custom_onboarding?.quiz?.map((q, i) => (
            <li key={i}>{q}</li>
          ))}
        </ul>
        <button className="btn" onClick={() => window.location = world.dashboard_url}>Fine – Vai al tuo mondo</button>
      </AdaptiveLayout>
    );

  return null;
};

export default WorldOnboardingUltra;
