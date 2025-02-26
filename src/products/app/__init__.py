from flask import Flask
from app.core.config import Config
from app.core.routes import register_routes
from app.core.database import init_db

def create_app(config = Config):
    app = Flask(__name__)
    app.config.from_object(config)
    
    init_db(app)
    register_routes(app)

    return app