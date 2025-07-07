import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

export default function AnalyticsChart({ data }) {
  return (
    <div className="w-full bg-black rounded-xl p-8 shadow-xl border-2 border-yellow-400 my-6">
      <ResponsiveContainer width="100%" height={240}>
        <BarChart data={data}>
          <XAxis dataKey="label" stroke="#FFD85C" />
          <YAxis stroke="#FFD85C" />
          <Tooltip
            contentStyle={{
              background: "#000", border: "2px solid #FFD85C", color: "#FFD85C", fontFamily: "Playfair Display"
            }}
          />
          <Bar dataKey="value" fill="url(#kpiBar)" />
          <defs>
            <linearGradient id="kpiBar" x1="0" y1="0" x2="1" y2="0">
              <stop offset="0%" stopColor="#8B5CFF" />
              <stop offset="60%" stopColor="#FFD85C" />
              <stop offset="100%" stopColor="#4EC9FF" />
            </linearGradient>
          </defs>
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
