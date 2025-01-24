from pydantic import PostgresDsn, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from pydantic import BaseModel

BASE_DIR = Path(__file__).parent.parent.parent
ENV_PATH = BASE_DIR / '.env'


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_PATH, extra='ignore')
    db_url_scheme: str = Field(..., alias="DB_URL_SCHEME")
    db_host: str = Field(..., alias="POSTGRES_HOST")
    db_port: str = Field(..., alias="POSTGRES_PORT")
    db_name: str = Field(..., alias="POSTGRES_DB_NAME")
    db_user: str = Field(..., alias="POSTGRES_USER")
    db_password: str = Field(..., alias="POSTGRES_PASSWORD")

    @property
    def database_url(self) -> str:
        """ URL для подключения (DSN)"""
        return (
            f"{self.db_url_scheme}://{self.db_user}:{self.db_password}@"
            f"{self.db_host}:{self.db_port}/{self.db_name}?async_fallback=True"
        )


settings = Settings()
