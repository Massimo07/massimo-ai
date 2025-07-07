# /frontend/src/assets

Questa cartella contiene tutti i file statici multimediali necessari per il frontend di Massimo AI.

---

## Tipologie di file contenuti

- **Immagini e loghi**: PNG, JPG, SVG usati nel layout, header, landing, icone
- **Icone vettoriali**: SVG o file ottimizzati per prestazioni e scalabilità
- **Favicon**: icona del sito/app per browser e dispositivi
- **Sfondo e texture**: immagini decorative e pattern per sezioni e pagine
- **File statici extra**: come font custom, se presenti

---

## Best practice

- Usa nomi file chiari e consistenti, es.: `logo.svg`, `copertina1.png`, `icon-ai.svg`
- Mantieni la dimensione dei file ottimizzata per la velocità di caricamento (es. PNG compressi, SVG minimizzati)
- Usa SVG per icone e loghi quando possibile per la migliore qualità e scalabilità
- Importa sempre gli asset tramite import ES6 in React (`import logo from '../assets/logo.svg';`)
- Organizza gli asset per tipo o funzione (es. `/icons/`, `/images/`, `/backgrounds/`) se la cartella cresce molto
- Versiona sempre i file all’interno del repository per tenere traccia delle modifiche

---

## Esempio d’uso in React

```jsx
import logo from '../assets/logo.svg';

function Header() {
  return <img src={logo} alt="Massimo AI Logo" className="w-32 h-auto" />;
}
