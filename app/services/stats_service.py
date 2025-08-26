import threading
from statistics import mean
from typing import Iterable, Dict, Any

def threaded_stats(numbers: Iterable[int]) -> Dict[str, Any]:
    """Llogarit min/max/avg """
    numbers = [n for n in numbers if isinstance(n, int)]  # filter
    results, lock = {}, threading.Lock()

    def put(k, v):
        with lock:
            results[k] = v

    def fmin():
        put("min", min(numbers) if numbers else None)

    def fmax():
        put("max", max(numbers) if numbers else None)

    def favg():
        put("avg", mean(numbers) if numbers else None)

    threads = [threading.Thread(target=f) for f in (fmin, fmax, favg)]
    for t in threads: t.start()
    for t in threads: t.join()
    return results
