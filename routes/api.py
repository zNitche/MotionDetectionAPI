from flask import Blueprint, current_app, request, jsonify, make_response, abort
from config import ApiConfig
from utils import log_utils
import json
from datetime import datetime


api = Blueprint("api", __name__)


@api.route("/api/notify", methods=["POST"])
def notify():
    response = make_response(jsonify(status=ApiConfig.POST_FAILED_MESSAGE), 400)

    data = request.data

    if data:
        try:
            parsed_data = json.loads(data.decode(ApiConfig.POST_DATA_ENCODING))

            if parsed_data[ApiConfig.TOKEN_KEY_NAME] == ApiConfig.AUTH_TOKEN:
                notification_message = parsed_data[ApiConfig.SENSOR_NAME_KEY_NAME]

                current_app.motion_notifier.send_message(f"[{datetime.now()}] {notification_message}")

                log_utils.log_message(notification_message)

                response = make_response(jsonify(status=ApiConfig.POST_SUCCESS_MESSAGE), 200)

            else:
                abort(401)

        except (json.decoder.JSONDecodeError, KeyError):
            pass

    return response
