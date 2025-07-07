import create from "zustand";
import { persist, devtools } from "zustand/middleware";

export const useAgentStore = create(
  devtools(
    persist(
      (set) => ({
        agents: [],
        loading: false,
        error: null,

        fetchAgents: async () => {
          set({ loading: true, error: null });
          try {
            const res = await fetch("/api/agents");
            if (!res.ok) throw new Error("Errore caricamento agenti");
            const data = await res.json();
            set({ agents: data, loading: false });
          } catch (err) {
            set({ error: err.message, loading: false });
          }
        },

        addAgent: async (agent) => {
          try {
            const res = await fetch("/api/agents", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify(agent),
            });
            if (!res.ok) throw new Error("Errore aggiunta agente");
            await useAgentStore.getState().fetchAgents();
          } catch (err) {
            set({ error: err.message });
          }
        },

        updateAgent: async (id, updates) => {
          try {
            const res = await fetch(`/api/agents/${id}`, {
              method: "PUT",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify(updates),
            });
            if (!res.ok) throw new Error("Errore aggiornamento agente");
            await useAgentStore.getState().fetchAgents();
          } catch (err) {
            set({ error: err.message });
          }
        },

        deleteAgent: async (id) => {
          try {
            const res = await fetch(`/api/agents/${id}`, { method: "DELETE" });
            if (!res.ok) throw new Error("Errore eliminazione agente");
            await useAgentStore.getState().fetchAgents();
          } catch (err) {
            set({ error: err.message });
          }
        },
      }),
      {
        name: "massimo-ai-agents-store",
      }
    )
  )
);
