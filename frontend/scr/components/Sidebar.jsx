export default function Sidebar() {
  return (
    <aside className="fixed top-0 left-0 h-full w-64 bg-black border-r-2 border-yellow-400 shadow-xl flex flex-col pt-20">
      <nav className="flex-1 flex flex-col space-y-6 px-6">
        <a href="/dashboard" className="text-xl font-serif font-bold text-yellow-400 hover:gradient-text">Dashboard</a>
        <a href="/users" className="text-xl font-serif text-yellow-400">Utenti</a>
        <a href="/worlds" className="text-xl font-serif text-yellow-400">Mondi</a>
        <a href="/agents" className="text-xl font-serif text-yellow-400">Agents</a>
        <a href="/subscriptions" className="text-xl font-serif text-yellow-400">Abbonamenti</a>
        <a href="/payments" className="text-xl font-serif text-yellow-400">Pagamenti</a>
        <a href="/analytics" className="text-xl font-serif text-yellow-400">Analytics</a>
      </nav>
    </aside>
  );
}
