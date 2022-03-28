import os


class AppConfig:
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    APP_PORT = 8080
    APP_HOST = "0.0.0.0"
    DEBUG_MODE = False


class DiscordConfig:
    BOT_COMMAND_PREFIX = "!"

    DISCORD_WEBHOOK_URL = ""

    DISCORD_BOT_TOKEN = ""
    DISCORD_TARGET_GUILD = ""
    DISCORD_TARGET_CHANNEL = ""


class BotConfig:
    MESSAGE_TYPE_KEY_NAME = "type"
    MESSAGE_CONTENT_KEY_NAME = "content"

    MESSAGE_TYPE_MESSAGE_KEY_NAME = "message"
    FILE_TYPE_MESSAGE_KEY_NAME = "file"

    LOG_FILES_DIR_PATH = os.path.join(AppConfig.CURRENT_DIR, "logs")
    BOT_LOGS_FILE = os.path.join(LOG_FILES_DIR_PATH, "bot.txt")

