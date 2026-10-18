import { Outlet } from "react-router";
import Navbar from "./Navbar";

function AppLayout() {
  // Por ahora false, luego conectaremos esto a la autenticación real
  const isLoggedIn = false; 
  const handleLogout = () => console.log("Logout");

  return (
    <div className="min-h-screen bg-[#08080f]">
      <Navbar isLoggedIn={isLoggedIn} onLogout={handleLogout} />
      <main className="pt-14">
        <Outlet />
      </main>
    </div>
  );
}

export default AppLayout;