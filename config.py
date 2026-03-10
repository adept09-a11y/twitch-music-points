from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_base_url: str = "http://localhost:8000"
    public_webhook_base_url: str | None = None

    twitch_client_id: str
    twitch_client_secret: str
    twitch_redirect_uri: str

    app_secret: str = "change_me"
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()
