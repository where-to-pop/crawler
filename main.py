from sources import PopplyCrawler
from sources import SeoulApiFetcher
from dotenv import load_dotenv
import os

def main():
    load_dotenv()  # 이거 위치가 여기가 괜찮으려나...

    SEOUL_DATA_API_KEY = os.environ.get("SEOUL_DATA_API_KEY")
    api_fetcher = SeoulApiFetcher(SEOUL_DATA_API_KEY)

    test_area_code = "POI068"
    api_fetcher.fetch_population(test_area_code)


if __name__ == "__main__":
    main()
