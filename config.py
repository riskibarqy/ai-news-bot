from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str

    TWITTER_BEARER_TOKEN: str
    TWITTER_API_KEY: str
    TWITTER_API_SECRET: str
    TWITTER_ACCESS_TOKEN: str
    TWITTER_ACCESS_SECRET: str

    class Config:
        env_file = ".env"

settings = Settings()
