import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BIGQUERY_APPLICATION_CREDENTIALS=os.environ.get("BIGQUERY_APPLICATION_CREDENTIALS")
    HUBSPOT_API_TOKEN=os.environ.get("HUBSPOT_API_TOKEN")

CONFIG = Config()