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
