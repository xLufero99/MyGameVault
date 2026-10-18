// src/components/ui/TestBackendButton.jsx
import { useState } from "react";
import { checkHealth } from "../../services/api"; // Importamos el servicio

export default function TestBackendButton() {
  const [status, setStatus] = useState("idle");
  const [data, setData] = useState(null);

  const testConnection = async () => {
    setStatus("loading");
    setData(null);

    try {
      // Usamos la función del servicio
      const json = await checkHealth();
      
      setData(json);
      setStatus("success");
    } catch (error) {
      setData(error.message);
      setStatus("error");
    }
  };

  return (
    <div className="p-4 border border-[#23233a] bg-[#10101a] my-4 font-mono-custom text-sm">
      <p className="mb-2 text-[#00e5ff]">PRUEBA DE CONEXIÓN AL BACKEND (/health)</p>
      
      <button
        onClick={testConnection}
        disabled={status === "loading"}
        className="px-4 py-2 border border-[#e040fb] text-[#e040fb] hover:bg-[#e040fb] hover:text-[#08080f] transition-colors disabled:opacity-50"
      >
        {status === "loading" ? "PROBANDO..." : "PROBAR CONEXIÓN ▶"}
      </button>

      {status === "success" && (
        <div className="mt-4 p-2 bg-[#18182a] border border-[#69ff47] text-[#69ff47]">
          <p className="font-bold mb-1">¡ÉXITO! Datos recibidos:</p>
          <pre className="text-xs overflow-auto max-h-40">
            {JSON.stringify(data, null, 2)}
          </pre>
        </div>
      )}

      {status === "error" && (
        <div className="mt-4 p-2 bg-[#18182a] border border-[#ff4757] text-[#ff4757]">
          <p className="font-bold mb-1">ERROR:</p>
          <p className="text-xs">{data}</p>
        </div>
      )}
    </div>
  );
}