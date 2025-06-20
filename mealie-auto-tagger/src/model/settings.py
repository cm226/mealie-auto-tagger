from typing import List, Optional

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    host : str = ""
    mealie_url : str = ""
    mealie_user: str = ""
    mealie_pw: str = ""

    labels: List[str] = []

    class Config:
        env_file = ".env"  # This tells Pydantic to load from .env
        env_file_encoding = 'utf-8'  # Optional: use utf-8 encoding

# Instantiate the settings
settings = Settings()
