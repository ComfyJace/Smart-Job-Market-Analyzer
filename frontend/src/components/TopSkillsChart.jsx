import { useEffect, useState } from "react";
import api from "../services/api";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from "recharts";

function TopSkillsChart() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchTopSkills = async () => {
      try {
        const response = await api.get("/analytics/top-skills");
        const formatted = Object.entries(response.data).map(([skill, count]) => ({
          skill,
          count,
        }));
        setData(formatted);
      } catch (error) {
        console.error("Error fetching top skills:", error);
      }
    };

    fetchTopSkills();
  }, []);

  return (
    <div>
      <h2>Top Skills in Job Market</h2>
      <div style={{ width: "100%", height: 300 }}>
        <ResponsiveContainer>
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="skill" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="count" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

export default TopSkillsChart;