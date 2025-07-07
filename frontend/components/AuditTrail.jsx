import React from "react";

const AuditTrail = ({ logs = [] }) => (
  <div className="bg-black/60 rounded-2xl shadow-xl p-4 mt-6">
    <h2 className="text-lg text-gold mb-2 font-semibold">Audit Trail</h2>
    <ul className="text-white text-sm max-h-48 overflow-y-auto">
      {logs.map((log, i) => (
        <li key={i} className="border-b border-violet-800 py-1">
          <span className="text-cyan-400">{log.timestamp}</span>
          {" – "}
          <span>{log.action}</span>
          {" (user: "}
          <span className="text-gold">{log.user}</span>
          {")"}
        </li>
      ))}
    </ul>
  </div>
);

export default AuditTrail;
