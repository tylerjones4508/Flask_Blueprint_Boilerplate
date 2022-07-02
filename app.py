from flask import Flask
from dotenv import load_dotenv
from general.general import general
import os

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.register_blueprint(general)
    return app

