from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal

class Settings(BaseSettings):
    ENVIRONMENT: Literal["local", "stsging", "production"] = "local"
    
    model_config = SettingsConfigDict(
        env_file="../../.envs/.env.local",
        env_ignore_empty=True,
        extra="ignore"
    )
    
    API_V1_STR: str
    PROJECT_NAME: str
    PROJECT_DESCRIPTION: str
    SITE_NAME: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_POST: str
    DATABASE_URL: str
    
settings = Settings()