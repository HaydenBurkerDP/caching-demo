from routes.user_routes import user_routes
from routes.cache_routes import cache_routes


def register_blueprints(app):
    app.register_blueprint(user_routes)
    app.register_blueprint(cache_routes)
