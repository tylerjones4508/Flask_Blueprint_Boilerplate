from flask import Blueprint, render_template, request, redirect, url_for, current_app
import datetime

general = Blueprint("home", __name__, template_folder="templates", static_folder="static")

@general.route('/')
def index():
    return "<H1>Hello World</H1>"
