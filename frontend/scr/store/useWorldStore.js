import create from "zustand";
import { persist, devtools } from "zustand/middleware";

export const useWorldStore = create(
  devtools(
    persist(
      (set) => ({
        worlds: [],
        loading: false,
        error: null,

        fetchWorlds: async () => {
          set({ loading: true, error: null });
          try {
            const res = await fetch("/api/worlds");
            if (!res.ok) throw new Error("Errore caricamento mondi");
            const data = await res.json();
            set({ worlds: data, loading: false });
          } catch (err) {
            set({ error: err.message, loading: false });
          }
        },

        addWorld: async (world) => {
          try {
            const res = await fetch("/api/worlds", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify(world),
            });
            if (!res.ok) throw new Error("Errore aggiunta mondo");
            await useWorldStore.getState().fetchWorlds();
          } catch (err) {
            set({ error: err.message });
          }
        },

        updateWorld: async (id, updates) => {
          try {
            const res = await fetch(`/api/worlds/${id}`, {
              method: "PUT",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify(updates),
            });
            if (!res.ok) throw new Error("Errore aggiornamento mondo");
            await useWorldStore.getState().fetchWorlds();
          } catch (err) {
            set({ error: err.message });
          }
        },

        deleteWorld: async (id) => {
          try {
            const res = await fetch(`/api/worlds/${id}`, { method: "DELETE" });
            if (!res.ok) throw new Error("Errore eliminazione mondo");
            await useWorldStore.getState().fetchWorlds();
          } catch (err) {
            set({ error: err.message });
          }
        },
      }),
      {
        name: "massimo-ai-worlds-store",
      }
    )
  )
);
