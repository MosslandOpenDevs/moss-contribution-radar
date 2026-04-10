from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "moss-contribution-radar"


settings = Settings()
