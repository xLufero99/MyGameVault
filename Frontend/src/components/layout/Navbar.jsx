import { NavLink } from "react-router";

function Navbar() {
  return (
    <nav>
      <NavLink to="/">MyGameVault</NavLink>
      <NavLink to="/games">Catálogo</NavLink>
      <NavLink to="/vault">Mi Vault</NavLink>
      <NavLink to="/profile">Perfil</NavLink>
      <NavLink to="/login">Login</NavLink>
    </nav>
  );
}

export default Navbar;