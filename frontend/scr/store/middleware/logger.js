export const logger = (config) => (set, get, api) =>
  config(
    (args) => {
      console.log("[ZUSTAND] State change:", args);
      set(args);
      console.log("[ZUSTAND] New state:", get());
    },
    get,
    api
  );
