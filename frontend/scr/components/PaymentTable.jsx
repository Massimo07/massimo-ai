export default function PaymentTable({ payments }) {
  return (
    <table className="min-w-full bg-black text-white rounded-xl shadow-lg border-separate border-spacing-y-2">
      <thead>
        <tr>
          <th className="px-4 py-2 text-yellow-400 font-serif text-lg">Utente</th>
          <th className="px-4 py-2 text-yellow-400 font-serif text-lg">Importo</th>
          <th className="px-4 py-2 text-yellow-400 font-serif text-lg">Data</th>
          <th className="px-4 py-2 text-yellow-400 font-serif text-lg">Stato</th>
        </tr>
      </thead>
      <tbody>
        {payments.map((p) => (
          <tr key={p.id} className="border-b-2 border-yellow-400 hover:bg-violet-900/30">
            <td className="px-4 py-2 font-serif">{p.user}</td>
            <td className="px-4 py-2 font-serif">€{p.amount}</td>
            <td className="px-4 py-2 font-serif">{p.date}</td>
            <td className="px-4 py-2 font-serif">
              <span className={`rounded-xl px-3 py-1 ${p.status === "success" ? "bg-green-600" : "bg-red-600"}`}>
                {p.status}
              </span>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
