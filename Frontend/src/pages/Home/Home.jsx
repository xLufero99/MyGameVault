import TestBackendButton from "../../components/ui/TestBackendButton";

function Home() {
  return (
    <div className="p-8 max-w-7xl mx-auto">
      <h1 className="font-pixel text-2xl text-[#e040fb] mb-6">Home</h1>
      
      {/* Botón de prueba temporal */}
      <TestBackendButton />
      
      <p className="text-[#55556e]">Aquí irá el diseño de la página principal...</p>
    </div>
  );
}

export default Home;