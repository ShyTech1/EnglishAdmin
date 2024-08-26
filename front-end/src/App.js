
import TopNavBar from "./components/TopNavBar";
import Table from "./components/Table";
import StudentCard from "./components/StudentCard";
import Api from "./api/api";

Api()
function App() {

  return (
    <div>
      <TopNavBar />
      <Table  />
      <StudentCard />
    </div>

  );
}

export default App;
