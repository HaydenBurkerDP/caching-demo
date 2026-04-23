
import time
import math
from flask import jsonify

from db import cache


def slow_factorial(n):
    time.sleep(1)
    return math.factorial(n)


def get_factorial(n):
    start_time = time.time()
    result = slow_factorial(n)
    end_time = time.time()
    return jsonify({
        'result': result,
        'time_taken': end_time - start_time,
        'cached': False
    })


def get_factorial_cached(n):
    cache_key = f"factorial:{n}"

    start_time = time.time()
    result = cache.get(cache_key)
    cached = result != None

    if not result:
        result = slow_factorial(n)
        cache.set(cache_key, result, timeout=300)

    end_time = time.time()
    return jsonify({
        'result': result,
        'time_taken': end_time - start_time,
        'cached': cached
    })


def invalidate_cache(n):
    cache_key = f"factorial:{n}"
    cache.delete(cache_key)
    return jsonify({"message": f"Cache invalidated for {cache_key}"})


def clear_cache():
    cache.clear()
    return jsonify({"message": "All cache cleared"})
