from flask import Flask
from flask_jwt_extended import JWTManager
from config import SQLALCHEMY_DATABASE_URI, JWT_SECRET_KEY
from models import db
from controllers.auth_controller import auth_bp
from controllers.episode_controller import episode_bp
from controllers.guest_controller import guest_bp
from controllers.appearance_controller import appearance_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY

db.init_app(app)
jwt = JWTManager(app)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(episode_bp)
app.register_blueprint(guest_bp)
app.register_blueprint(appearance_bp)

if __name__ == '__main__':
    app.run(debug=True)
