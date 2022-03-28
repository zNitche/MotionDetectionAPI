from flask import Blueprint, current_app, request, jsonify
from config import ApiConfig
import json
from datetime import datetime


api_ = Blueprint("api", __name__, template_folder='template', static_folder='static')


@api_.route("/api/notify", methods=["POST"])
def notify():
    data = request.data

    if data:
        parsed_data = json.loads(data.decode("utf-8"))

        if parsed_data[ApiConfig.TOKEN_KEY_NAME] == ApiConfig.AUTH_TOKEN:
            current_app.motion_notifier.send_message(f"[{datetime.now()}]"
                                                     f" {parsed_data[ApiConfig.SENSOR_NAME_KEY_NAME]}")

    return jsonify(status="OK")
