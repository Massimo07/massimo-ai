import React from "react";

const KPIWidget = ({ title, value, icon }) => (
  <div className="bg-gradient-to-br from-violet-900 to-black rounded-2xl shadow-xl p-5 text-center min-w-[180px] border-2 border-gold">
    <div className="text-4xl mb-2">{icon}</div>
    <div className="text-lg font-semibold text-gold mb-1">{title}</div>
    <div className="text-3xl font-bold text-white">{value}</div>
  </div>
);

export default KPIWidget;
