from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    discord_token: str = Field(validation_alias="DISCORD_TOKEN")
    openai_api_key: str = Field(validation_alias="API_KEY")

    model_config = SettingsConfigDict(
        env_file=".env", case_sensitive=False, extra="ignore"
    )


settings = Settings()
