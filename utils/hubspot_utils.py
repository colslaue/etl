from airflow.decorators import task
from connectors.hubspot_api import HubspotConn

@task
def fetch_deals():
    conn = HubspotConn().get_instance()
    data = conn.crm.deals.basic_api.get_page(limit=10, archived=False)
    dict = data.to_dict()

    return dict


@task
def flatten_deals(data):
    data = data.get('results')
    json_data = []
    for deal in data:
        properties = deal.get('properties')
        data = {
            "id": properties.get('hs_object_id')
            ,"dealname": properties.get('dealname')
        }
        json_data.append(data)

    return json_data
