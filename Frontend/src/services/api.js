// src/services/api.js

const API_URL = import.meta.env.VITE_API_URL;

/**
 * Prueba la conexión con el endpoint /health del backend
 */
export async function checkHealth() {
  try {
    // Aquí hacemos la concatenación de la variable de entorno + la ruta
    const response = await fetch(`${API_URL}/health`);
    
    if (!response.ok) {
      throw new Error(`Error HTTP: ${response.status}`);
    }
    
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error en checkHealth:", error);
    throw error;
  }
}