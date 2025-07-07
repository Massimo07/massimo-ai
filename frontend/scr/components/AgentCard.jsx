export default function AgentCard({ agent }) {
  return (
    <div className="bg-black border-2 border-yellow-400 rounded-2xl shadow-xl p-6 flex flex-col items-center mb-4">
      <div className="mb-2 text-2xl font-serif font-bold" style={{ color: "#FFD85C" }}>
        {agent.name}
      </div>
      <div className="gradient-text mb-2">{agent.role}</div>
      <div className="text-white">{agent.description}</div>
      <span className="inline-block mt-4 px-4 py-1 rounded-xl bg-gradient-to-r from-purple-500 to-yellow-400 text-white font-bold">
        {agent.status}
      </span>
    </div>
  );
}
