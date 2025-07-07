import React, { useState } from "react";
import logo from "../assets/copertina1.png";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  // handleSubmit qui...

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-black">
      <img src={logo} alt="Logo" className="w-40 mb-8 drop-shadow-2xl" />
      <h2 className="text-4xl font-serif font-bold mb-3" style={{ color: "#FFD85C" }}>
        Login
      </h2>
      <div className="text-xl mb-8 font-serif gradient-text">
        Your gateway to the future
      </div>
      <form className="w-full max-w-sm bg-black/80 p-8 rounded-2xl shadow-xl border border-yellow-400">
        <input
          className="w-full mb-4 p-3 rounded-xl bg-black text-white font-serif border-2 border-yellow-400 focus:ring-2 focus:ring-violet-500"
          placeholder="Email"
          value={email}
          onChange={e => setEmail(e.target.value)}
        />
        <input
          className="w-full mb-6 p-3 rounded-xl bg-black text-white font-serif border-2 border-yellow-400 focus:ring-2 focus:ring-violet-500"
          placeholder="Password"
          type="password"
          value={password}
          onChange={e => setPassword(e.target.value)}
        />
        <button
          type="submit"
          className="w-full py-3 rounded-2xl text-xl font-semibold font-serif bg-gradient-to-r from-yellow-400 via-orange-500 to-purple-500 text-white shadow-lg"
        >
          Entra
        </button>
      </form>
    </div>
  );
}
