import React from "react";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from "recharts";

const AnalyticsChart = ({ data }) => (
  <div className="w-full bg-black/70 rounded-2xl p-4 shadow-lg min-h-[250px]">
    <ResponsiveContainer width="100%" height={250}>
      <LineChart data={data}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="date" stroke="#FFD85C" />
        <YAxis stroke="#FFD85C" />
        <Tooltip />
        <Line type="monotone" dataKey="users" stroke="#FFD85C" strokeWidth={3} />
        <Line type="monotone" dataKey="agents" stroke="#4EC9FF" strokeWidth={2} />
        <Line type="monotone" dataKey="revenue" stroke="#FF8F00" strokeWidth={2} />
      </LineChart>
    </ResponsiveContainer>
  </div>
);

export default AnalyticsChart;
