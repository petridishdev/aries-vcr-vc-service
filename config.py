from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Settings(BaseSettings):
    project_title: str = "Aries VCR VC Service"

    aries_vcr_url: str = os.environ["ARIES_VCR_URL"]

    issuer_registry_url: str = os.environ["ISSUER_REGISTRY_URL"]


settings = Settings()
