import { useMemo } from "react";
import useAuth from "./useAuth";

export default function usePermission(requiredRoles = []) {
  const { user } = useAuth();

  // Verifica se l'utente ha almeno un ruolo richiesto
  const hasAccess = useMemo(() => {
    if (!user || !user.roles) return false;
    return requiredRoles.some(role => user.roles.includes(role));
  }, [user, requiredRoles]);

  return hasAccess;
}
import { useState, useEffect } from "react";

export default function useDebounce(value, delay = 300) {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const handler = setTimeout(() => setDebouncedValue(value), delay);

    return () => clearTimeout(handler);
  }, [value, delay]);

  return debouncedValue;
}
