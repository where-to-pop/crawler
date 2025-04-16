from datetime import datetime
from elasticsearch_dsl import Index
from database import PopplyPopup
from base import BaseUploader
from constants import ESIndex

class PopplyUploader(BaseUploader):
    def __init__(self, client):
        super().__init__(client)
        self.index_name = ESIndex.POPPLY_POPUPS

    def upload(self, data_list):
        print(f"[DEBUG] Elasticsearch 인덱스 이름: {self.index_name}")  # 디버깅용 출력
        if not Index(self.index_name, using=self.client).exists():
            PopplyPopup.init(using=self.client)

        for data in data_list:
            popup = PopplyPopup(
                title=data["title"],
                location=data["location"],
                period=data["period"],
                link=data["link"],
                created_at=datetime.now()
            )
            popup.save(using=self.client)
        print(f"[+] {len(data_list)}개의 데이터를 Elasticsearch에 업로드 완료")