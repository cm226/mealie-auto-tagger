from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=('.env', '.env.dev')
    )
    # required
    host : str
    mealie_url : str
    mealie_api_token : str

    db_url: str = Field(default="sqlite:///./database.db.sqlite3")
    production: bool = Field(default=False)
# Instantiate the settings
settings = Settings()
