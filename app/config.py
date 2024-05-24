from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = 'FastApiDDD'
    db_host: str
    db_user: str
    db_password: str
    db_port: int
    db_name: str
