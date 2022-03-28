from __init__ import create_app
import multiprocessing
from modules.discord_bot import MotionDetectorBOT
from config import DiscordConfig
import log_utils


def start_bot_process():
    bot_process = multiprocessing.Process(target=run_bot)
    bot_process.start()


def run_bot():
    try:
        bot = MotionDetectorBOT()
        bot.run(DiscordConfig.DISCORD_BOT_TOKEN)

    except Exception as e:
        log_utils.log_bot(f"Error while initializing bot {e}")


start_bot_process()
app = create_app()


if __name__ == "__main__":
    APP_PORT = app.config["APP_PORT"]
    APP_HOST = app.config["APP_HOST"]
    DEBUG_MODE = app.config["DEBUG_MODE"]

    app.run(debug=DEBUG_MODE, host=APP_HOST, port=APP_PORT, threaded=True)
