from configs.settings import SEOUL_DATA_API_KEY, ELASTICSEARCH_HOST
from database import ElasticsearchClient

def main():
    try:
        es_client = ElasticsearchClient()
        client = es_client.get_client()

        print("Elasticsearch 연결 성공!")
        print(client.info())
    except Exception as e:
        print(f"Elasticsearch 연결 실패: {e}")

    # api_fetcher = SeoulApiFetcher(SEOUL_DATA_API_KEY)

    # test_area_code = "POI068"
    # api_fetcher.fetch_population(test_area_code)
    print(ELASTICSEARCH_HOST)

if __name__ == "__main__":
    main()
