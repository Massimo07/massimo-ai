import React from "react";

const AgentStatusTable = ({ agents = [] }) => (
  <div className="overflow-x-auto bg-black/60 rounded-2xl shadow-lg p-4">
    <table className="min-w-full text-gold">
      <thead>
        <tr>
          <th className="px-3 py-2 text-left">Nome</th>
          <th className="px-3 py-2 text-left">Tipo</th>
          <th className="px-3 py-2 text-left">Stato</th>
          <th className="px-3 py-2 text-left">Ultimo Check</th>
        </tr>
      </thead>
      <tbody>
        {agents.map((agent, i) => (
          <tr key={i}>
            <td className="px-3 py-2">{agent.name}</td>
            <td className="px-3 py-2">{agent.type}</td>
            <td className={`px-3 py-2 ${agent.status === "OK" ? "text-green-400" : "text-red-400"}`}>{agent.status}</td>
            <td className="px-3 py-2">{agent.last_check}</td>
          </tr>
        ))}
      </tbody>
    </table>
  </div>
);

export default AgentStatusTable;
