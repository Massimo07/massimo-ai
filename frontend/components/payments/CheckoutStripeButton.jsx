import React from "react";

export default function CheckoutStripeButton({ amount, userId, planId, onSuccess, onError }) {
  const handleClick = async () => {
    try {
      const res = await fetch("/api/payments/stripe/create-session", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_id: userId, plan_id: planId }),
      });
      const data = await res.json();
      if (data.checkout_url) {
        window.location.href = data.checkout_url;
      } else {
        throw new Error(data.detail || "Errore Stripe");
      }
    } catch (err) {
      onError && onError(err);
    }
  };

  return (
    <button
      onClick={handleClick}
      className="w-full py-3 bg-blue-600 text-white rounded-xl font-bold text-lg hover:bg-blue-700 transition"
    >
      Paga con Carta (Stripe)
    </button>
  );
}
