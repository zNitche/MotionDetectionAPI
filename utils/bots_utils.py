import multiprocessing
from modules.motion_detector_bot import MotionDetectorBOT
from config import DiscordConfig
from utils import log_utils
from modules.motion_detection_notifier import MotionDetectionNotifier


def init_bot_webhook():
    return MotionDetectionNotifier()


def start_bot_process():
    bot_process = multiprocessing.Process(target=run_bot)
    bot_process.start()


def run_bot():
    try:
        bot = MotionDetectorBOT()
        bot.run(DiscordConfig.DISCORD_BOT_TOKEN)

    except Exception as e:
        log_utils.log_bot(f"Error while initializing bot {e}")
