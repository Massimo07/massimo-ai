import React from "react";
import { CheckCircle2 } from "lucide-react";

export default function PaymentSuccess() {
  return (
    <div className="flex flex-col items-center py-16">
      <CheckCircle2 size={64} className="text-green-500 mb-4" />
      <h1 className="text-3xl font-bold mb-3">Pagamento riuscito!</h1>
      <p className="text-lg text-gray-700 mb-2 text-center">
        Grazie per aver scelto <span className="font-semibold">Massimo AI</span>.<br />
        Hai ora accesso completo ai tuoi servizi.
      </p>
      <a
        href="/dashboard"
        className="mt-6 px-6 py-3 bg-blue-600 rounded-xl text-white font-bold hover:bg-blue-700 transition"
      >
        Vai alla Dashboard
      </a>
    </div>
  );
}
