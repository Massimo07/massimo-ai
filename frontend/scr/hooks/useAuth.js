import { useState, useEffect, useCallback } from "react";
import jwt_decode from "jwt-decode";

const TOKEN_STORAGE_KEY = "massimoAI_token";

export default function useAuth() {
  const [token, setToken] = useState(() => localStorage.getItem(TOKEN_STORAGE_KEY));
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Decodifica il token JWT per estrarre user info e scadenza
  const decodeToken = useCallback((jwt) => {
    try {
      return jwt_decode(jwt);
    } catch {
      return null;
    }
  }, []);

  // Verifica se il token è ancora valido (non scaduto)
  const isTokenValid = useCallback((jwt) => {
    const decoded = decodeToken(jwt);
    if (!decoded || !decoded.exp) return false;
    return decoded.exp * 1000 > Date.now();
  }, [decodeToken]);

  // Salva token su localStorage e stato
  const saveToken = useCallback((jwt) => {
    localStorage.setItem(TOKEN_STORAGE_KEY, jwt);
    setToken(jwt);
    const decoded = decodeToken(jwt);
    setUser(decoded?.user || null);
  }, [decodeToken]);

  // Rimuove token e resetta stato
  const clearAuth = useCallback(() => {
    localStorage.removeItem(TOKEN_STORAGE_KEY);
    setToken(null);
    setUser(null);
  }, []);

  // Login: chiama API, salva token
  const login = useCallback(async (email, password) => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch("/api/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.message || "Login failed");
      saveToken(data.token);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, [saveToken]);

  // Logout: cancella token e resetta stato
  const logout = useCallback(() => {
    clearAuth();
  }, [clearAuth]);

  // Effetto per auto logout se token scade
  useEffect(() => {
    if (!token) return;

    const decoded = decodeToken(token);
    if (!decoded || !decoded.exp) {
      clearAuth();
      return;
    }

    const expiresIn = decoded.exp * 1000 - Date.now();
    if (expiresIn <= 0) {
      clearAuth();
      return;
    }

    const timeout = setTimeout(() => {
      clearAuth();
    }, expiresIn);

    return () => clearTimeout(timeout);
  }, [token, decodeToken, clearAuth]);

  // Effetto per inizializzare user da token se presente
  useEffect(() => {
    if (token && !user) {
      const decoded = decodeToken(token);
      setUser(decoded?.user || null);
    }
  }, [token, user, decodeToken]);

  return {
    user,
    token,
    loading,
    error,
    login,
    logout,
    isAuthenticated: Boolean(user),
  };
}
