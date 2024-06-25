import os
from http import HTTPStatus

import requests

from config.payload import payload_settings
from config.telegram import telegram_settings
from logger.logger import get_logger

logger = get_logger(__name__)


class TelegramService:
    def __init__(self):
        self.chat_id = telegram_settings.chat_id
        self.parse_mode = (
            None
            if not payload_settings.parse_mode
            else payload_settings.parse_mode.value
        )
        self.base_url = f"https://api.telegram.org/bot{telegram_settings.bot_token}"

    def send_message(self, message: str) -> None:
        payload = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": self.parse_mode,
        }
        response = requests.post(self.base_url + "/sendMessage", data=payload)
        if response.status_code != HTTPStatus.OK:
            logger.error(
                "Error sending message\n\nStatus code: %s\n\nMessage: %s",
                response.status_code,
                response.text,
            )
            return
        logger.info("Message sent")

    def send_file(self, file_path: str, caption: str | None) -> None:
        if not os.path.exists(file_path):
            logger.error("File not found: %s", file_path)
            return
        if not os.path.isfile(file_path):
            logger.error("Not a file: %s", file_path)
            return
        payload = {
            "chat_id": self.chat_id,
            "parse_mode": self.parse_mode,
        }
        if caption is not None:
            payload["caption"] = caption
        with open(file_path, "rb") as file:
            files = {"document": file}
            response = requests.post(
                self.base_url + "/sendDocument", data=payload, files=files
            )
        if response.status_code != HTTPStatus.OK:
            logger.error("Error sending file: %s", response.text)
            return
        logger.info("File sent")
