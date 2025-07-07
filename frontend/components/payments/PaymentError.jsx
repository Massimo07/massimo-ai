import React from "react";
import { XCircle } from "lucide-react";

export default function PaymentError({ message }) {
  return (
    <div className="flex flex-col items-center py-16">
      <XCircle size={64} className="text-red-500 mb-4" />
      <h1 className="text-3xl font-bold mb-3">Errore di pagamento</h1>
      <p className="text-lg text-gray-700 mb-2 text-center">
        {message || "Si è verificato un problema durante il pagamento. Riprova o contatta il supporto."}
      </p>
      <a
        href="/checkout"
        className="mt-6 px-6 py-3 bg-gray-300 rounded-xl text-black font-bold hover:bg-gray-400 transition"
      >
        Torna al pagamento
      </a>
    </div>
  );
}
