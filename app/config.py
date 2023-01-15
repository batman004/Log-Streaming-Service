from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME: str = "Log-Streaming-Service"
    DEBUG_MODE: bool = True


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    workers: int = 4


class Settings(CommonSettings, ServerSettings):
    pass


settings = Settings()
