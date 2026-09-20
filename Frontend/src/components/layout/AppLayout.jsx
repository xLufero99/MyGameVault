import { Outlet } from "react-router";
import Navbar from "./Navbar";

function AppLayout() {
  return (
    <>
      <Navbar />
      <main>
        <Outlet />
      </main>
    </>
  );
}

export default AppLayout;   