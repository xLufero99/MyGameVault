import { createBrowserRouter } from "react-router";
import AppLayout from "../components/layout/AppLayout";
import Home from "../pages/Home/Home";
import Games from "../pages/Games/Games"; // Este será nuestro "Search/Explorar"
import GameDetails from "../pages/GameDetails/GameDetails";
import MyVault from "../pages/MyVault/MyVault"; // Este será nuestro "Mis Listas"
import Profile from "../pages/Profile/Profile";
import Login from "../pages/Login/Login";

const router = createBrowserRouter([
  {
    path: "/",
    element: <AppLayout />,
    children: [
      { index: true, element: <Home /> },
      { path: "games", element: <Games /> }, // Explorar
      { path: "games/:id", element: <GameDetails /> },
      { path: "vault", element: <MyVault /> }, // Mis Listas
      { path: "profile", element: <Profile /> },
      { path: "login", element: <Login /> },
    ],
  },
]);

export default router;