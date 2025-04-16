import requests
from configs import settings
from bs4 import BeautifulSoup

class BaseApiFetcher:
    def __init__(self, timeout=settings.REQUESTS_TIMEOUT):
        self.timeout = timeout
        self.headers = {}

    def set_headers(self, headers):
        self.headers = headers

    def get_data(self, url, params=None):
        try:
            response = requests.get(url, params=params, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()

            content_type = response.headers.get('Content-Type')
            if content_type:
                if 'application/json' in content_type:
                    return response.json()
                elif 'application/xml' in content_type or 'text/xml' in content_type:
                    soup = BeautifulSoup(response.content, 'lxml-xml')
                    return soup
                else:
                    return response.text
            else:
                return response.text
        except requests.exceptions.RequestException as e:
            print(f"API 요청 실패: {e}")
            return None