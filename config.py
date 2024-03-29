from pydantic import BaseSettings

class Settings(BaseSettings):
    database_hostname:str
    database_port:str
    database_username:str
    database_password:str
    database_name:str
    algorithm:str
    youtube_api_key:str
    class Config:
        env_file = ".env"


settings=Settings()