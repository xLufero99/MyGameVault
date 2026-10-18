import { createBrowserRouter } from "react-router";
import AppLayout from "../components/layout/AppLayout";
import Home from "../pages/Home/Home";
import Games from "../pages/Games/Games";
import GameDetails from "../pages/GameDetails/GameDetails";
import MyVault from "../pages/MyVault/MyVault";
import Profile from "../pages/Profile/Profile";
import Login from "../pages/Login/Login";
import Register from "../pages/Register/Register";

const router = createBrowserRouter([
  {
    path: "/",
    element: <AppLayout />,
    children: [
      { index: true, element: <Home /> },
      { path: "games", element: <Games /> },
      { path: "games/:id", element: <GameDetails /> },
      { path: "vault", element: <MyVault /> },
      { path: "profile", element: <Profile /> },
      { path: "login", element: <Login /> },
      { path: "register", element: <Register /> },
    ],
  },
]);

export default router;