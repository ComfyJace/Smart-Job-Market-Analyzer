import { useState } from "react";

type RoleSkillsResult = {
  role: string;
  job_count: number;
  top_skills: Record<string, number>;
} | null;

function RoleSkills() {
  const [role, setRole] = useState("");
  const [result, setResult] = useState<RoleSkillsResult>(null);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    // Simulate an API call
    try {
      const response = await fetch(
        `/analytics/role-skills?role=${encodeURIComponent(role)}`,
      );

      if (!response.ok) {
        throw new Error(`HTTP error: ${response.status}`);
      }

      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error("Error fetching role skills:", error);
    }
  };

  return (
    <div className="w-full max-w-xl rounded-3xl border border-white/60 bg-white/90 backdrop-blur shadow-2xl p-8 md:p-10">
      <div className="mb-8">
        <h2 className="text-3xl font-semibold tracking-tight text-gray-900 sm:text-3xl">
          Role Skills Viewer
        </h2>
        <p className="mt-2 text-sm leading-6 text-gray-500 max-w-md">
          This component displays the skills associated with a selected role.
        </p>
      </div>

      <form className="space-y-6" onSubmit={handleSubmit}>
        <label
          htmlFor="role"
          className="block text-sm font-medium text-gray-700 mb-2"
        >
          Select Role
        </label>

        <select
          id="role"
          className="w-full rounded-xl border border-gray-200 bg-gray-50 px-4 -4 py-3 text-gray-800 shadow-sm transition duration-200 outline-none focus:border-blue-500 focus:bg-white focus:ring-4 focus:ring-blue-100"
          value={role}
          onChange={(e) => setRole(e.target.value)}
        >
          <option value="">-- Select a Role --</option>
          <option value="Machine Learning Engineer">
            Machine Learning Engineer
          </option>
        </select>

        <button
          type="submit"
          className="w-full rounded-xl bg-blue-600 px-4 py-3 text-sm-semibold text-white shadow-md transition duration-200 hover:bg-blue-700 hover:shadow-lg focus:outline-none focus:ring-4 focus:ring-blue-200 active:scale-[.98]"
        >
          Analyze
        </button>
      </form>
      {result && (
        <div className="mt-8 rounded-2xl border border-gray-200 bg-gray-50/70 p-6 shadow-inner">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">
            Top Skills for <span className="text-blue-600">{result.role}</span>
          </h3>

          <div className="space-y-3">
            {Object.entries(result.top_skills)
              .sort((a, b) => b[1] - a[1])
              .slice(0, 3)
              .map(([skill, count], index) => (
                <div
                  key={skill}
                  className="flex items-center justify-between rounded-xl bg-white px-4 py-3 shadow-sm hover:shadow-md transition"
                >
                  <div className="flex items-center gap-3">
                    {/* Rank badge */}
                    <span className="flex h-7 w-7 items-center justify-center rounded-full bg-blue-100 text-blue-600 text-xs font-semibold">
                      {index + 1}
                    </span>

                    {/* Skill name */}
                    <span className="font-medium text-gray-800">{skill}</span>
                  </div>

                  {/* Count */}
                  <span className="text-sm text-gray-500">{count} jobs</span>
                </div>
              ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default RoleSkills;
