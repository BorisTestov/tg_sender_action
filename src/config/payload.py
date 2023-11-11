from pydantic_settings import BaseSettings, SettingsConfigDict


class PayloadSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="TG_SENDER_PAYLOAD_")
    message: str | None = None
    file_path: str | None = None


payload_settings = PayloadSettings()
