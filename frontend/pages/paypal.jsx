// /frontend/pages/Billing.jsx – aggiungi il pulsante "Paga con PayPal"
const startPayPalCheckout = async () => {
  const res = await fetch("/api/paypal/checkout", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      plan: selectedPlan,
      success_url: window.location.origin + "/billing?paypal=success",
      cancel_url: window.location.origin + "/billing?paypal=cancel"
    }),
  });
  const { url } = await res.json();
  window.location.href = url; // Redirect all’interfaccia di pagamento PayPal
};
