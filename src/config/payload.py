from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from logger.logger import get_logger
from utils.parse_modes import ParseMode

logger = get_logger(__name__)


class PayloadSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="TG_SENDER_PAYLOAD_")
    message: str | None = None
    file_path: str | None = None
    parse_mode: ParseMode | None = None

    @field_validator("parse_mode", mode="before")
    @classmethod
    def validate_parse_mode(cls, value: str | None) -> str | None:
        if value is not None and value not in ParseMode.__members__:
            logger.warning("Invalid parse mode: %s", value)
            logger.warning("Using default parse mode: %s", None)
            return
        return value


payload_settings = PayloadSettings()
