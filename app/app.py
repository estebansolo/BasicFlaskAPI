from flask import Flask
from app.blueprints import orders, products

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(orders.bp)
    app.register_blueprint(products.bp)

    return app
