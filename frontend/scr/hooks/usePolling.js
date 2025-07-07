import { useEffect, useRef, useState, useCallback } from "react";

export default function usePolling(callback, delay = 5000) {
  const savedCallback = useRef();
  const [isPolling, setIsPolling] = useState(true);

  // Salva il callback più recente
  useEffect(() => {
    savedCallback.current = callback;
  }, [callback]);

  // Setup intervallo
  useEffect(() => {
    if (!isPolling) return;

    function tick() {
      savedCallback.current();
    }
    const id = setInterval(tick, delay);

    return () => clearInterval(id);
  }, [delay, isPolling]);

  const stop = useCallback(() => setIsPolling(false), []);
  const start = useCallback(() => setIsPolling(true), []);

  return { stop, start, isPolling };
}
