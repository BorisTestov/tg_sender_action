from config.payload import payload_settings
from logger.logger import get_logger
from services.telegram import TelegramService

logger = get_logger(__name__)


def main():
    tg_service = TelegramService()
    message = payload_settings.message
    file_path = payload_settings.file_path
    if payload_settings.file_path is not None:
        tg_service.send_file(file_path, message)
    elif message is not None:
        tg_service.send_message(message)
    else:
        logger.error("No message or file provided")


if __name__ == "__main__":
    main()
