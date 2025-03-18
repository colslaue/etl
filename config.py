import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BIGQUERY_APPLICATION_CREDENTIALS=os.environ.get("BIGQUERY_APPLICATION_CREDENTIALS")
    HUBSPOT_API_TOKEN=os.environ.get("HUBSPOT_API_TOKEN")
    BIGQUERY_PROJECT_ID=os.environ.get("BIGQUERY_PROJECT_ID")
    BIGQUERY_HUBSPOT_DATASET=os.environ.get("BIGQUERY_HUBSPOT_DATASET")

CONFIG = Config()