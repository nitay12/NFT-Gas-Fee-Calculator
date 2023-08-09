import os

from dotenv import load_dotenv
from elasticsearch import Elasticsearch

load_dotenv()


class Config:
    SYSTEM_USERNAME = os.environ.get('SYSTEM_USERNAME')
    SYSTEM_PASSWORD = os.environ.get('SYSTEM_PASSWORD')
    CRYPTOPUNKS_ADDRESS = os.environ.get('CRYPTOPUNKS_ADDRESS')
    MUTANTAPE_ADDRESS = os.environ.get('MUTANTAPE_ADDRESS')
    COINGECKO_URL = os.environ.get('COINGECKO_URL')
    ETHERSCAN_URL = os.environ.get('ETHERSCAN_URL')
    ETHERSCAN_KEY = os.environ.get('ETHERSCAN_KEY')
    ES_USERNAME = os.environ.get('ES_USERNAME')
    ES_PASSWORD = os.environ.get('ES_PASSWORD')
    ES_CLOUD_ID = os.environ.get('ES_CLOUD_ID')


class ElasticsearchConfig:
    def __init__(self):
        self.es = Elasticsearch(
            cloud_id=Config.ES_CLOUD_ID,
            basic_auth=(Config.ES_USERNAME, Config.ES_PASSWORD),
            verify_certs=False
        )

        try:
            self.info = self.es.info()
        except ConnectionError as e:
            self.info = None
