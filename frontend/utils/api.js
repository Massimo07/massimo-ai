// frontend/utils/api.js
export async function aiPredict(prompt, model = "gpt-4o", token) {
  const res = await fetch("/api/ai/predict", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${token}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ prompt, model }),
  });
  return res.json();
}

export async function getDashboardStats(token) {
  const res = await fetch("/api/dashboard/stats", {
    headers: { "Authorization": `Bearer ${token}` }
  });
  return res.json();
}
