import { NavLink, Link, useNavigate } from "react-router";

const NAV_ITEMS = [
  { label: 'INICIO', path: '/' },
  { label: 'EXPLORAR', path: '/games' },
  { label: 'MIS LISTAS', path: '/vault' },
  { label: 'PERFIL', path: '/profile' },
];

export default function Navbar({ isLoggedIn, onLogout }) {
  return (
    <header className="fixed top-0 left-0 right-0 z-50 bg-[#08080f]/95 backdrop-blur-sm border-b border-[#23233a]">
      <div className="max-w-7xl mx-auto px-4 h-14 flex items-center gap-6">
        
        {/* Logo */}
        <Link to="/" className="flex items-center gap-2 shrink-0">
          <span className="text-[#e040fb] text-base font-mono-custom">▶</span>
          <span className="glow-primary font-pixel text-[#e040fb] tracking-widest text-xs">
            PIXELVAULT
          </span>
        </Link>

        {/* Nav items */}
        <nav className="hidden md:flex items-center gap-1 flex-1">
          {NAV_ITEMS.map((item) => (
            <NavLink
              key={item.label}
              to={item.path}
              className={({ isActive }) => 
                `px-3 py-1.5 text-xs font-medium transition-all duration-150 border border-transparent font-mono-custom tracking-wider flex items-center
                ${isActive ? 'text-[#e040fb]' : 'text-[#55556e] hover:text-[#e8e8f0]'}`
              }
            >
              {({ isActive }) => (
                <>
                  {isActive && <span className="mr-1.5">▶</span>}
                  {item.label}
                </>
              )}
            </NavLink>
          ))}
        </nav>

        {/* Right side */}
        <div className="ml-auto flex items-center gap-3">
          {isLoggedIn ? (
            <div className="flex items-center gap-3">
              <Link to="/profile" className="flex items-center gap-2 border border-[#23233a] px-3 py-1.5 hover:border-[#e040fb] transition-colors">
                <div className="w-6 h-6 flex items-center justify-center text-xs font-bold bg-[#e040fb] text-[#08080f] font-mono-custom">
                  C
                </div>
                <span className="text-xs hidden sm:block text-[#e8e8f0] font-mono-custom">
                  CyberSamurai_77
                </span>
              </Link>
              <button onClick={onLogout} className="text-xs px-2 py-1.5 border border-[#23233a] hover:border-[#ff4757] hover:text-[#ff4757] transition-colors font-mono-custom text-[#55556e]">
                SALIR
              </button>
            </div>
          ) : (
            <Link to="/login" className="flex items-center gap-2 px-4 py-1.5 border text-xs font-medium transition-all duration-200 hover:shadow-primary border-[#e040fb] text-[#e040fb] font-mono-custom tracking-wider">
              LOGIN <span>▶</span>
            </Link>
          )}
        </div>
      </div>
      {/* Accent line */}
      <div className="h-px bg-gradient-to-r from-[#e040fb] via-[#00e5ff] to-transparent opacity-40" />
    </header>
  );
}