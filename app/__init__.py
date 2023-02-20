from flask import Flask

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)


from flask_mail import Mail
from .config import Config
from app import views