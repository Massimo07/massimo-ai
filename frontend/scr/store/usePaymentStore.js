import create from "zustand";
import { persist, devtools } from "zustand/middleware";

export const usePaymentStore = create(
  devtools(
    persist(
      (set) => ({
        payments: [],
        loading: false,
        error: null,

        fetchPayments: async () => {
          set({ loading: true, error: null });
          try {
            const res = await fetch("/api/payments");
            if (!res.ok) throw new Error("Errore caricamento pagamenti");
            const data = await res.json();
            set({ payments: data, loading: false });
          } catch (err) {
            set({ error: err.message, loading: false });
          }
        },

        addPayment: async (payment) => {
          try {
            const res = await fetch("/api/payments", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify(payment),
            });
            if (!res.ok) throw new Error("Errore aggiunta pagamento");
            await usePaymentStore.getState().fetchPayments();
          } catch (err) {
            set({ error: err.message });
          }
        },

        updatePayment: async (id, updates) => {
          try {
            const res = await fetch(`/api/payments/${id}`, {
              method: "PUT",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify(updates),
            });
            if (!res.ok) throw new Error("Errore aggiornamento pagamento");
            await usePaymentStore.getState().fetchPayments();
          } catch (err) {
            set({ error: err.message });
          }
        },

        deletePayment: async (id) => {
          try {
            const res = await fetch(`/api/payments/${id}`, { method: "DELETE" });
            if (!res.ok) throw new Error("Errore eliminazione pagamento");
            await usePaymentStore.getState().fetchPayments();
          } catch (err) {
            set({ error: err.message });
          }
        },
      }),
      {
        name: "massimo-ai-payments-store",
      }
    )
  )
);
