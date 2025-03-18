from airflow.decorators import task
from connectors.bigquery import BigQueryClient
from google.cloud import bigquery


@task
def load_table_from_json(data, destination):
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )
    client = BigQueryClient().get_instance()
    client.load_table_from_json(
        json_rows=data
        ,destination=destination
        ,job_config=job_config
    )