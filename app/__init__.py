from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.models import init_db

    from app.routes import claims_bp
    app.register_blueprint(claims_bp)
    return app