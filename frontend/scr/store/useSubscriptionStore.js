import create from "zustand";
import { persist, devtools } from "zustand/middleware";

export const useSubscriptionStore = create(
  devtools(
    persist(
      (set) => ({
        subscriptions: [],
        loading: false,
        error: null,

        fetchSubscriptions: async () => {
          set({ loading: true, error: null });
          try {
            const res = await fetch("/api/subscriptions");
            if (!res.ok) throw new Error("Errore caricamento abbonamenti");
            const data = await res.json();
            set({ subscriptions: data, loading: false });
          } catch (err) {
            set({ error: err.message, loading: false });
          }
        },

        addSubscription: async (subscription) => {
          try {
            const res = await fetch("/api/subscriptions", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify(subscription),
            });
            if (!res.ok) throw new Error("Errore aggiunta abbonamento");
            await useSubscriptionStore.getState().fetchSubscriptions();
          } catch (err) {
            set({ error: err.message });
          }
        },

        updateSubscription: async (id, updates) => {
          try {
            const res = await fetch(`/api/subscriptions/${id}`, {
              method: "PUT",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify(updates),
            });
            if (!res.ok) throw new Error("Errore aggiornamento abbonamento");
            await useSubscriptionStore.getState().fetchSubscriptions();
          } catch (err) {
            set({ error: err.message });
          }
        },

        deleteSubscription: async (id) => {
          try {
            const res = await fetch(`/api/subscriptions/${id}`, { method: "DELETE" });
            if (!res.ok) throw new Error("Errore eliminazione abbonamento");
            await useSubscriptionStore.getState().fetchSubscriptions();
          } catch (err) {
            set({ error: err.message });
          }
        },
      }),
      {
        name: "massimo-ai-subscriptions-store",
      }
    )
  )
);
