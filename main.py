from sources import PopplyCrawler
from database import PopplyUploader, ElasticsearchClient

def main():
    # Step 1: 크롤링 수행
    crawler = PopplyCrawler()
    crawler.crawl_popups()

    # Step 2: Elasticsearch에 업로드
    es_client = ElasticsearchClient.get_client()
    uploader = PopplyUploader(client=es_client)
    uploader.upload(crawler.popup_list)  # 크롤링된 데이터를 바로 업로드

if __name__ == "__main__":
    main()
