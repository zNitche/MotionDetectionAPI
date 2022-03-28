from flask import Blueprint, current_app


content_ = Blueprint("content", __name__, template_folder='template', static_folder='static')


@content_.route("/")
def home():
    current_app.motion_notifier.send_message("TEST")
