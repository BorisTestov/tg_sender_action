from pydantic_settings import BaseSettings, SettingsConfigDict


class TelegramSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="TG_SENDER_TG_")
    bot_token: str
    chat_id: int


telegram_settings = TelegramSettings()
