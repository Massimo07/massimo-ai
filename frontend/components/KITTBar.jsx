// Massimo AI – KITTBar.jsx
import React from "react";
export default function KITTBar({ active }) {
  return (
    <div
      className={`w-44 h-6 rounded-full shadow-lg my-2 transition-all duration-300 ${
        active
          ? "bg-gradient-to-r from-cyan-400 via-violet-600 to-orange-400 animate-pulse"
          : "bg-gray-600 opacity-60"
      }`}
    />
  );
}
