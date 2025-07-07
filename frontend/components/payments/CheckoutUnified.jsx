// /frontend/components/payments/CheckoutUnified.jsx

import React, { useState } from "react";
import CheckoutStripeButton from "./CheckoutStripeButton";
import CheckoutPaypalButton from "./CheckoutPaypalButton";

export default function CheckoutUnified({ amount, userId, planId, onSuccess, onError }) {
  const [method, setMethod] = useState(null);

  return (
    <div className="max-w-md mx-auto p-6 rounded-2xl shadow-lg bg-white flex flex-col gap-6 border border-gray-100">
      <h2 className="text-2xl font-bold mb-2 text-center tracking-tight">Scegli come pagare</h2>
      <div className="flex justify-center gap-6 my-3">
        <button
          onClick={() => setMethod("stripe")}
          className={`px-5 py-2 rounded-xl text-white font-semibold transition-all ${method === "stripe" ? "bg-blue-600" : "bg-blue-400 hover:bg-blue-600"}`}
        >
          💳 Carta (Stripe)
        </button>
        <button
          onClick={() => setMethod("paypal")}
          className={`px-5 py-2 rounded-xl text-white font-semibold transition-all ${method === "paypal" ? "bg-yellow-500" : "bg-yellow-400 hover:bg-yellow-500"}`}
        >
          🅿️ PayPal
        </button>
      </div>

      <div className="mt-6">
        {method === "stripe" && (
          <CheckoutStripeButton
            amount={amount}
            userId={userId}
            planId={planId}
            onSuccess={onSuccess}
            onError={onError}
          />
        )}
        {method === "paypal" && (
          <CheckoutPaypalButton
            amount={amount}
            userId={userId}
            planId={planId}
            onSuccess={onSuccess}
            onError={onError}
          />
        )}
        {!method && (
          <p className="text-center text-gray-500">Seleziona un metodo di pagamento per proseguire.</p>
        )}
      </div>
    </div>
  );
}
