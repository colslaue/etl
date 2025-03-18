from airflow.decorators import dag
from datetime import datetime, timedelta
from utils.bigquery_utils import load_table_from_json
from utils.hubspot_utils import fetch_deals, flatten_deals

default_args = {
    "owner": "colslaue",
    "retries": 1,
    "retry_delay": timedelta(seconds=5),
    "start_date": datetime(2025, 3, 15)
}

@dag(
    dag_id="fetch_deals",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
)

def load_deals():
    deal_data = fetch_deals()
    flattened_data = flatten_deals(deal_data)
    load_table_from_json(flattened_data, destination="airflow-test-453214.colslaue.test123")

load_deals()