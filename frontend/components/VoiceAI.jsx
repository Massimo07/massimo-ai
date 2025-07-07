// Massimo AI – VoiceAI.jsx
// Voice assistant pronto per Smart Glasses, mobile, desktop
import React, { useState, useRef } from "react";
import KITTBar from "./KITTBar";

export default function VoiceAI({ onResult }) {
  const [listening, setListening] = useState(false);
  const recognitionRef = useRef(null);

  const startListening = () => {
    if (!("webkitSpeechRecognition" in window)) {
      alert("Voice recognition non supportata");
      return;
    }
    const recognition = new window.webkitSpeechRecognition();
    recognition.lang = "auto";
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.onstart = () => setListening(true);
    recognition.onresult = e => {
      setListening(false);
      if (e.results[0][0].transcript)
        onResult(e.results[0][0].transcript);
    };
    recognition.onend = () => setListening(false);
    recognition.onerror = () => setListening(false);
    recognitionRef.current = recognition;
    recognition.start();
  };

  return (
    <div className="flex flex-col items-center">
      <KITTBar active={listening} />
      <button
        className="mt-4 px-4 py-2 bg-blue-700 rounded-xl text-white font-bold"
        onClick={startListening}
      >
        {listening ? "Sto ascoltando..." : "Parla con Massimo AI"}
      </button>
    </div>
  );
}
