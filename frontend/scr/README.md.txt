# Massimo AI – /frontend/src/  
**Struttura completa dei file principali**

> Usa questa guida per non confonderti mai tra componenti, servizi, pagine e asset!

---

## 📁 assets/
- `/frontend/src/assets/logo.svg`
- `/frontend/src/assets/ai_icon.svg`
- … *(icone, immagini, grafica custom)*

## 📁 components/
- `/frontend/src/components/AppNavbar.jsx`
- `/frontend/src/components/Sidebar.jsx`
- `/frontend/src/components/AgentCard.jsx`
- `/frontend/src/components/WorldCard.jsx`
- `/frontend/src/components/SubscriptionCard.jsx`
- `/frontend/src/components/PaymentTable.jsx`
- `/frontend/src/components/UserTable.jsx`
- `/frontend/src/components/AnalyticsChart.jsx`
- `/frontend/src/components/NotificationToast.jsx`
- `/frontend/src/components/Loader.jsx`
- `/frontend/src/components/Modal.jsx`
- … *(altri componenti UI aggiuntivi)*

## 📁 pages/
- `/frontend/src/pages/Dashboard.jsx`
- `/frontend/src/pages/Users.jsx`
- `/frontend/src/pages/Worlds.jsx`
- `/frontend/src/pages/Agents.jsx`
- `/frontend/src/pages/Subscriptions.jsx`
- `/frontend/src/pages/Payments.jsx`
- `/frontend/src/pages/Automation.jsx`
- `/frontend/src/pages/Analytics.jsx`
- `/frontend/src/pages/Login.jsx`
- `/frontend/src/pages/Profile.jsx`
- `/frontend/src/pages/NotFound.jsx`
- … *(aggiungi qui nuove pagine se ti servono!)*

## 📁 services/
- `/frontend/src/services/api.js`
- `/frontend/src/services/auth.js`
- `/frontend/src/services/agent.js`
- `/frontend/src/services/world.js`
- `/frontend/src/services/user.js`
- `/frontend/src/services/subscription.js`
- `/frontend/src/services/payment.js`
- `/frontend/src/services/automation.js`
- `/frontend/src/services/analytics.js`
- `/frontend/src/services/notification.js`
- … *(REST client extra o servizi custom)*

## 📁 store/
- `/frontend/src/store/useAuthStore.js`
- `/frontend/src/store/useUserStore.js`
- `/frontend/src/store/useWorldStore.js`
- `/frontend/src/store/useAgentStore.js`
- `/frontend/src/store/useSubscriptionStore.js`
- `/frontend/src/store/usePaymentStore.js`
- `/frontend/src/store/useAutomationStore.js`
- `/frontend/src/store/useAnalyticsStore.js`
- … *(store globali Zustand/Redux)*

## 📁 hooks/
- `/frontend/src/hooks/useAuth.js`
- `/frontend/src/hooks/useFetch.js`
- `/frontend/src/hooks/usePermission.js`
- `/frontend/src/hooks/useNotification.js`
- `/frontend/src/hooks/usePolling.js`
- … *(aggiungi tutti i custom hook che vuoi!)*

## 📁 i18n/
- `/frontend/src/i18n/it.json`
- `/frontend/src/i18n/en.json`
- `/frontend/src/i18n/es.json`
- … *(altri file lingua)*

## 📁 styles/
- `/frontend/src/styles/tailwind.css`
- `/frontend/src/styles/theme.css`
- … *(altri file CSS/SCSS custom)*

## 📄 App.jsx
## 📄 main.jsx
## 📄 router.jsx
## 📄 index.html
## 📄 README.md *(questo file)*

---

### Come funziona il frontend?
1. Tutto inizia da **`main.jsx`** → carica il router, i provider, lo store.
2. **`App.jsx`** gestisce il layout globale: Navbar, Sidebar, routing delle pagine.
3. Tutte le chiamate API sono pronte in **`/services/`** e sono già integrate con il backend Massimo AI (/api/v1).
4. Tutto lo stato globale (auth, utenti, mondi, agenti, abbonamenti, ecc) viene gestito in **`/store/`**.
5. **Multilingua, dark mode e responsive** sono già inclusi!
6. Puoi customizzare ogni componente o pagina, basta aggiungerlo qui e integrarlo al router.

---

### 📈 Prossimi step consigliati:
- Customizza `assets/` con logo e grafica tua!
- Aggiorna `i18n/` per supporto multilingua istantaneo.
- Estendi pagine/servizi con nuove funzioni (es: AI generativa, onboarding animato, video guide).
- Collega tutto al backend `/api/v1`… e hai una piattaforma da Top 1% mondiale!

---

**Se hai bisogno di snippet, esempio di pagina, componente o hook, chiedi e lo ricevi pronto!**  
Qui il livello è sempre superiore.  
Massimo, ora puoi delegare anche il lavoro a chiunque… senza mai perdere il filo! 🚀
