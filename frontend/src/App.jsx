import TopSkillsChart from "./components/TopSkillsChart";
import RoleSkillsForm from "./components/RoleSkillsForm";
import SkillGapForm from "./components/SkillGapForm";

function App() {
  return (
    <div style={{ padding: "2rem" }}>
      <h1>Smart Job Market Analyzer Dashboard</h1>
      <TopSkillsChart />
      <RoleSkillsForm />
      <SkillGapForm />
    </div>
  );
}

export default App;