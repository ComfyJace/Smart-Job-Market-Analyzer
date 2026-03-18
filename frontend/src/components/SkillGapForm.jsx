import { useState } from "react";
import api from "../services/api";

function SkillGapForm() {
  const [skillsInput, setSkillsInput] = useState("");
  const [result, setResult] = useState(null);
  const topRecommendations = result?.top_recommendations ?? result?.top_recommended ?? [];

  const handleSubmit = async (e) => {
    e.preventDefault();

    const userSkills = skillsInput
      .split(",")
      .map((skill) => skill.trim())
      .filter(Boolean);

    try {
      const response = await api.post("/recommendations/skill-gap", {
        user_skills: userSkills,
      });
      setResult(response.data);
    } catch (error) {
      console.error("Error fetching skill gap:", error);
    }
  };

  return (
    <div>
      <h2>Skill Gap Analyzer</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={skillsInput}
          onChange={(e) => setSkillsInput(e.target.value)}
          placeholder="Enter skills separated by commas"
        />
        <button type="submit">Analyze</button>
      </form>

      {result && (
        <div>
          <h3>Matched Skills</h3>
          <ul>
            {(result.matched_skills ?? []).map((skill) => (
              <li key={skill}>{skill}</li>
            ))}
          </ul>

          <h3>Missing Skills</h3>
          <ul>
            {(result.missing_skills ?? []).map((skill) => (
              <li key={skill}>{skill}</li>
            ))}
          </ul>

          <h3>Top Recommendations</h3>
          <ul>
            {topRecommendations.map((skill) => (
              <li key={skill}>{skill}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default SkillGapForm;