import React from "react";
import logo from "../assets/copertina1.png";

export default function AppNavbar() {
  return (
    <nav className="w-full flex items-center justify-between px-8 py-4 bg-black shadow-lg z-50">
      <div className="flex items-center">
        <img src={logo} alt="Logo" className="h-14 mr-6 drop-shadow-lg" />
        <span className="text-3xl font-serif font-bold" style={{ color: "#FFD85C" }}>
          MASSIMO AI
        </span>
      </div>
      <div className="flex items-center space-x-8">
        <a href="/" className="text-lg font-serif" style={{ color: "#FFD85C" }}>Home</a>
        <a href="/dashboard" className="text-lg font-serif gradient-text">Dashboard</a>
        <a href="/login" className="text-lg font-serif" style={{ color: "#FFD85C" }}>Login</a>
      </div>
    </nav>
  );
}
