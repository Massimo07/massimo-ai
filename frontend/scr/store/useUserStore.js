import create from "zustand";
import { persist, devtools } from "zustand/middleware";

export const useUserStore = create(
  devtools(
    persist(
      (set) => ({
        users: [],
        loading: false,
        error: null,

        fetchUsers: async () => {
          set({ loading: true, error: null });
          try {
            const res = await fetch("/api/users");
            if (!res.ok) throw new Error("Errore caricamento utenti");
            const data = await res.json();
            set({ users: data, loading: false });
          } catch (err) {
            set({ error: err.message, loading: false });
          }
        },

        addUser: async (user) => {
          try {
            const res = await fetch("/api/users", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify(user),
            });
            if (!res.ok) throw new Error("Errore aggiunta utente");
            await useUserStore.getState().fetchUsers();
          } catch (err) {
            set({ error: err.message });
          }
        },

        updateUser: async (id, updates) => {
          try {
            const res = await fetch(`/api/users/${id}`, {
              method: "PUT",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify(updates),
            });
            if (!res.ok) throw new Error("Errore aggiornamento utente");
            await useUserStore.getState().fetchUsers();
          } catch (err) {
            set({ error: err.message });
          }
        },

        deleteUser: async (id) => {
          try {
            const res = await fetch(`/api/users/${id}`, { method: "DELETE" });
            if (!res.ok) throw new Error("Errore eliminazione utente");
            await useUserStore.getState().fetchUsers();
          } catch (err) {
            set({ error: err.message });
          }
        },
      }),
      {
        name: "massimo-ai-users-store",
      }
    )
  )
);
