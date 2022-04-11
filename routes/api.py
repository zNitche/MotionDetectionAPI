from flask import Blueprint, current_app, request, jsonify, make_response, abort
from config import ApiConfig
from utils import log_utils
import json
from datetime import datetime


api_ = Blueprint("api", __name__)


@api_.route("/api/notify", methods=["POST"])
def notify():
    response = make_response(jsonify(status="Failed"), 400)

    data = request.data

    if data:
        try:
            parsed_data = json.loads(data.decode("utf-8"))

            if parsed_data[ApiConfig.TOKEN_KEY_NAME] == ApiConfig.AUTH_TOKEN:
                notification_message = parsed_data[ApiConfig.SENSOR_NAME_KEY_NAME]

                current_app.motion_notifier.send_message(f"[{datetime.now()}] {notification_message}")

                log_utils.log_message(notification_message)

                response = make_response(jsonify(status="OK"), 200)

            else:
                abort(401)

        except:
            pass

    return response
