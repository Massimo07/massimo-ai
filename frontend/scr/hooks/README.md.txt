# /frontend/src/hooks

Questa cartella contiene tutti i **custom React Hooks** creati per Massimo AI, per gestire logica riutilizzabile, stato, side effects e integrazioni API in modo modulare e pulito.

---

## Scopo

- Separare la logica complessa da componenti UI  
- Favorire il riuso e la testabilità  
- Gestire side effects, polling, notifiche, autenticazione, permessi, local storage e altro

---

## Struttura tipica

- `useAuth.js` — gestione autenticazione e token  
- `useFetch.js` — fetch dati da API con gestione errori e loading  
- `useNotification.js` — logica per mostrare notifiche/toast  
- `usePermission.js` — gestione permessi e ruoli utente  
- `usePolling.js` — polling ricorrente per aggiornamenti dati  
- `useDebounce.js` — debounce di input per performance  
- `useLocalStorage.js` — sincronizza stato React con localStorage/sessionStorage  
- … altri hook custom specifici per funzionalità

---

## Convenzioni

- Nome hook sempre in camelCase e con prefisso `use`  
- Hooks **non devono** contenere logica UI o JSX, solo logica di stato/comportamento  
- Devono restituire solo dati e funzioni necessari al componente  
- Gestire cleanup in `useEffect` per evitare memory leak

---

## Esempio base: useFetch.js

```jsx
import { useState, useEffect } from 'react';

export default function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let isMounted = true;
    fetch(url)
      .then(res => res.json())
      .then(json => {
        if (isMounted) {
          setData(json);
          setLoading(false);
        }
      })
      .catch(err => {
        if (isMounted) {
          setError(err);
          setLoading(false);
        }
      });
    return () => { isMounted = false; };
  }, [url]);

  return { data, loading, error };
}
