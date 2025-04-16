from base import BaseApiFetcher
from configs import settings


class SeoulApiFetcher(BaseApiFetcher):
    def __init__(self, api_key=None, timeout=settings.REQUESTS_TIMEOUT):
        super().__init__(timeout=timeout)
        self.api_key = api_key


    def fetch_population(self, area_code):
        url = f"{settings.SEOUL_API_BASE_URL}/{self.api_key}/xml/citydata_ppltn/1/5/{area_code}"
        soup = self.get_data(url)
        area_info = soup.find("SeoulRtd.citydata_ppltn")
        data = {
            "area_name" : area_info.find("AREA_NM").text,
            "congest_lvl" : area_info.find("AREA_CONGEST_LVL").text,
            "population_min" : int(area_info.find("AREA_PPLTN_MIN").text),
            "population_max" : int(area_info.find("AREA_PPLTN_MAX").text)
        }
        print(data)
        return 
    