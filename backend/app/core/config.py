from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    MODEL: str = "gpt-5-mini"
    
    # Voice Settings 
    VOICE_RECORD_DURATION: int
    VOICE_NAME: str
    SAMPLE_RATE: int

    NEWS_API_KEY: str
    DATABASE_URL: str
    
    model_config = SettingsConfigDict(
        env_file = ".env",
        extra="ignore"
    )
    
    MAX_CONVERSATION_MESSAGES: int = 20
    
settings = Settings()