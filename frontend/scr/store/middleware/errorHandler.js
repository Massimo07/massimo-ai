export const errorHandler = (config) => (set, get, api) =>
  config(
    (args) => {
      try {
        set(args);
      } catch (error) {
        console.error("[ZUSTAND] State update error:", error);
        // Puoi integrare alert o log esterni qui
      }
    },
    get,
    api
  );
