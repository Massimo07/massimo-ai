// /frontend/pages/Billing.jsx (Aggiungi nel bottone "Attiva con Stripe")
const startStripeCheckout = async () => {
  const res = await fetch("/api/stripe/checkout", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      user_id: userId,
      plan: selectedPlan,
      success_url: window.location.origin + "/billing?success=true",
      cancel_url: window.location.origin + "/billing?canceled=true"
    }),
  });
  const { url } = await res.json();
  window.location.href = url; // Redirect alla pagina di pagamento Stripe!
};
