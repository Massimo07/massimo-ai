import React from "react";
import SubscriptionStatusBadge from "./SubscriptionStatusBadge";

export default function AccountPanel({ user }) {
  if (!user) return null;
  return (
    <div className="bg-white shadow-lg rounded-2xl p-6 max-w-md mx-auto flex flex-col gap-4 items-center border">
      <div className="text-2xl font-bold">{user.name || user.email}</div>
      <SubscriptionStatusBadge level={user.subscription_level} />
      <div className="text-gray-500 text-sm">ID: {user.id}</div>
      <div className="mt-4">
        <a
          href="/pricing"
          className="px-4 py-2 rounded-xl bg-gradient-to-r from-blue-600 to-purple-500 text-white font-bold shadow hover:from-blue-700 hover:to-purple-700 transition"
        >
          Cambia o aggiorna abbonamento
        </a>
      </div>
    </div>
  );
}
