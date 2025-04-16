from dotenv import load_dotenv
import os
load_dotenv()

HEADLESS = True
IMPLICIT_WAIT = 5
SCROLL_PAUSE = 2
POPPLY_BASE_URL = "https://www.popply.co.kr"
POPPLY_POPUP_LIST_URL = f"{POPPLY_BASE_URL}/popup"

REQUESTS_TIMEOUT=5
SEOUL_API_BASE_URL="http://openapi.seoul.go.kr:8088"
SEOUL_DATA_API_KEY=os.getenv("SEOUL_DATA_API_KEY")

ELASTICSEARCH_HOST=os.getenv("ELASTICSEARCH_HOST")