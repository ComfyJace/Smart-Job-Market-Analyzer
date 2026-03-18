import { useState } from "react";
import api from "../services/api";

function RoleSkillsForm() {
  const [role, setRole] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await api.get(`/analytics/role-skills?role=${encodeURIComponent(role)}`);
      setResult(response.data);
    } catch (error) {
      console.error("Error fetching role skills:", error);
    }
  };

  return (
    <div>
      <h2>Role Skills Viewer</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={role}
          onChange={(e) => setRole(e.target.value)}
          placeholder="Enter role"
        />
        <button type="submit">Analyze</button>
      </form>

      {result && (
        <div>
          <h3>{result.role}</h3>
          <p>Job Count: {result.job_count}</p>
          <ul>
            {Object.entries(result.top_skills).map(([skill, count]) => (
              <li key={skill}>
                {skill}: {count}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default RoleSkillsForm;