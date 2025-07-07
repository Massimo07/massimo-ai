import { useState, useCallback, useEffect } from "react";

export default function useNotification(timeout = 5000) {
  const [queue, setQueue] = useState([]);
  const [current, setCurrent] = useState(null);

  const push = useCallback((message, priority = 1) => {
    setQueue(q => [...q, { id: Date.now(), message, priority }]);
  }, []);

  // Ordina la coda per priorità alta e prende il primo
  useEffect(() => {
    if (!current && queue.length) {
      const sorted = [...queue].sort((a, b) => b.priority - a.priority);
      setCurrent(sorted[0]);
      setQueue(q => q.filter(item => item.id !== sorted[0].id));
    }
  }, [queue, current]);

  // Auto-dismiss dopo timeout
  useEffect(() => {
    if (!current) return;
    const timer = setTimeout(() => setCurrent(null), timeout);
    return () => clearTimeout(timer);
  }, [current, timeout]);

  const dismiss = useCallback(() => setCurrent(null), []);

  return {
    current,
    push,
    dismiss,
    queueLength: queue.length,
  };
}
