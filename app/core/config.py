from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://semi_user:semi_pass@localhost:5432/semi_db"

    model_config = {"env_file": ".env"}


settings = Settings()
