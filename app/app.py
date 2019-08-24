from flask import Flask
from app.blueprints import orders

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(orders.bp)

    return app
