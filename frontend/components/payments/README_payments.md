// /frontend/components/account/SubscriptionStatusBadge.jsx

import React from "react";
import { BadgeCheck, Gem, User, Crown } from "lucide-react";

const levelConfig = {
  free:  { label: "Free",      color: "bg-gray-200 text-gray-700", icon: User        },
  premium: { label: "Premium",   color: "bg-blue-500 text-white",    icon: BadgeCheck },
  pro:  { label: "Pro",       color: "bg-purple-500 text-white",  icon: Gem         },
  enterprise: { label: "Enterprise", color: "bg-yellow-400 text-black", icon: Crown },
};

export default function SubscriptionStatusBadge({ level = "free" }) {
  const { label, color, icon: Icon } = levelConfig[level] || levelConfig["free"];
  return (
    <span className={`inline-flex items-center gap-2 px-3 py-1 rounded-2xl text-sm font-bold shadow-sm ${color}`}>
      <Icon size={18} className="inline-block" />
      {label}
    </span>
  );
}
