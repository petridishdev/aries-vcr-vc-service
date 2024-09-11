from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    aries_vcr_url: str = "http://host.docker.internal:8080"


settings = Settings()
