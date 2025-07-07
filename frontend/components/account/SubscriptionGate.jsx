// /frontend/components/account/SubscriptionGate.jsx

import React from "react";
import SubscriptionStatusBadge from "./SubscriptionStatusBadge";

export default function SubscriptionGate({ user, children, requiredLevel = "premium", fallback = null }) {
  if (!user) return null;
  const levels = ["free", "premium", "pro", "enterprise"];
  const userLevelIdx = levels.indexOf(user.subscription_level || "free");
  const requiredIdx = levels.indexOf(requiredLevel);

  if (userLevelIdx < requiredIdx) {
    return fallback || (
      <div className="bg-yellow-50 p-6 rounded-xl border border-yellow-200 text-center">
        <SubscriptionStatusBadge level={user.subscription_level} />
        <div className="mt-2 mb-4 text-gray-700 text-sm">
          Questa funzione è riservata agli utenti <b>{requiredLevel}</b>.<br />
          <a href="/pricing" className="underline font-bold text-blue-700">Aggiorna il tuo abbonamento</a>
        </div>
      </div>
    );
  }

  return children;
}
