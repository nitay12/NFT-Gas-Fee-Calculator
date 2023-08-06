from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from app.auth import auth_bp
from app.models import User
from app.routes import main_bp

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize Flask Login Manager and Bcrypt
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(main_bp)


# Load user from session
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


if __name__ == '__main__':
    app.run(debug=True)
