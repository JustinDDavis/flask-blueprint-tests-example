from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=False)
    with app.app_context():
        # Register Blueprints
        from application.blog import routes as blog_routes
        from application.information import routes as info_routes

        app.register_blueprint(blog_routes.bp)
        app.register_blueprint(info_routes.bp)

        return app