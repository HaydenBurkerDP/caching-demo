from flask import Blueprint
from controllers import cache_controller

cache_routes = Blueprint("cache", __name__)


@cache_routes.route('/factorial/<int:n>')
def get_factorial(n):
    return cache_controller.get_factorial(n)


@cache_routes.route('/factorial-cached/<int:n>')
def get_factorial_cached(n):
    return cache_controller.get_factorial_cached(n)


@cache_routes.route('/invalidate-cache/<int:n>')
def invalidate_cache(n):
    return cache_controller.invalidate_cache(n)


@cache_routes.route('/clear-cache')
def clear_cache():
    return cache_controller.clear_cache()
