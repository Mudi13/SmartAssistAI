from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    MODEL: str = "gpt-5-mini"

    NEWS_API_KEY: str
    DATABASE_URL: str
    
    model_config = SettingsConfigDict(
        env_file = ".env",
        extra="ignore"
    )
    
settings = Settings()