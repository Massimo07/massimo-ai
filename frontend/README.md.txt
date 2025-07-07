# /frontend – Massimo AI

Questa cartella contiene il frontend ufficiale Massimo AI.
- Stack: **React 18+, Vite, TailwindCSS, Zustand/Redux**
- PRONTO per deployment su Vercel/Netlify/Cloud.
- Pronto per white-label, dark mode, multilingua, PWA.
- Template admin + dashboard founder + UI agent/AI personalizzati.
- Si collega via REST o WebSocket a `/api`.

## Principali cartelle/componenti:

- `src/components/` → UI riutilizzabili (Card, Table, Modal, Loader, Navbar, Sidebar…)
- `src/pages/` → Dashboard founder, agent, worlds, users, analytics
- `src/services/` → API client avanzato (con token refresh automatico!)
- `src/store/` → Zustand o Redux per stato globale user, agent, abbonamenti
- `src/hooks/` → Hook custom (auth, data fetch, permission)
- `src/assets/` → Logo, branding, icone AI personalizzabili
- `src/App.jsx` → Router, layout, loading
- `src/i18n/` → Multilingua istantanea (i18next)

---

## Features già integrate:

- **Login (JWT, token refresh)**
- **Gestione utenti/admin/permessi**
- **Gestione agent/AI, creazione/assegnazione**
- **Gestione mondi/AI Factory, abbonamenti, pagamenti**
- **Dashboard founder: KPI, ricavi, nuovi utenti, eventi**
- **Grafici analytics (Recharts/ChartJS)**
- **Dark mode & responsive 100%**
- **Error handler globale + toast + retry**
- **Compatibile con smartglass, mobile, tablet**
- **Notifiche real-time (WebSocket/Server Sent Event)**
- **Customizzazione UI per team, mondi, white-label**
- **Audit e logging azioni (visibile in dashboard)**
- **Hook e layout pronti per moduli futuri**

---

## Quick start

```bash
yarn install   # o npm install
yarn dev       # avvia in locale (default: http://localhost:5173)
