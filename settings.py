from pprint import pprint

from pydantic_settings import BaseSettings
from dotenv import load_dotenv, find_dotenv


class Settings(BaseSettings):
    OPENAI_API_KEY: str


    class Config:
        _env_file = None



settings = Settings(_env_file=find_dotenv())

pprint(settings.model_dump())

