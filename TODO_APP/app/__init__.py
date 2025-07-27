from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "your-secret-key"
    
    # Configure database URI
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'instance', 'todo.db')}"
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Ensure instance folder exists
    instance_path = os.path.join(basedir, 'instance')
    if not os.path.exists(instance_path):
        os.makedirs(instance_path)
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        
    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    return app