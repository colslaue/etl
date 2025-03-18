import hubspot
from config import CONFIG


class HubspotConn:
    _singleton = None
    conn = None

    def __init__(self):
        self.conn = hubspot.Client.create(access_token=CONFIG.HUBSPOT_API_TOKEN)

    @classmethod
    def get_instance(cls):
        if cls._singleton is None:
            cls._singleton = cls()
        return cls._singleton.conn
