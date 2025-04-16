from elasticsearch import Elasticsearch
from threading import Lock
from configs.settings import ELASTICSEARCH_HOST

class ElasticsearchClient:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """
        Elasticsearch 클라이언트 초기화
        """
        if not hasattr(self, "client"):
            self.hosts = [ELASTICSEARCH_HOST]
            self.timeout = 30
            self.client = Elasticsearch(hosts=self.hosts, timeout=self.timeout)
            if not self.client.ping():
                raise ValueError("Elasticsearch 연결 실패")

    def get_client(self):
        return self.client
