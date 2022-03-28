from flask import Flask
import os
import bots_utils


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.AppConfig")
    app.secret_key = os.urandom(25)

    app.motion_notifier = bots_utils.init_bot_webhook()

    with app.app_context():
        from routes import api, errors

        app.register_blueprint(api.api_)
        app.register_blueprint(errors.errors_)

        return app
