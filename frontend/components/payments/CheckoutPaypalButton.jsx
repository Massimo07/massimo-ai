import React from "react";

export default function CheckoutPaypalButton({ amount, userId, planId, onSuccess, onError }) {
  const handleClick = async () => {
    try {
      const res = await fetch("/api/payments/paypal/create-order", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_id: userId, plan_id: planId }),
      });
      const data = await res.json();
      if (data.checkout_url) {
        window.location.href = data.checkout_url;
      } else {
        throw new Error(data.detail || "Errore PayPal");
      }
    } catch (err) {
      onError && onError(err);
    }
  };

  return (
    <button
      onClick={handleClick}
      className="w-full py-3 bg-yellow-400 text-black rounded-xl font-bold text-lg hover:bg-yellow-500 transition"
    >
      Paga con PayPal
    </button>
  );
}
