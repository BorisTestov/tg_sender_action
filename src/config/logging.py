from pydantic_settings import BaseSettings, SettingsConfigDict


class LoggingSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="TG_SENDER_LOG_")
    level: str = "INFO"
    format: str = "%(asctime)s,%(msecs)03d %(levelname)-8s %(name)s: %(message)s"
    datefmt: str = "%b-%d-%Y %H:%M:%S"


logging_settings = LoggingSettings()
