import json
from datetime import datetime
from base import BaseApiFetcher
from configs.settings import REQUESTS_TIMEOUT, SEOUL_API_BASE_URL

class SeoulApiFetcher(BaseApiFetcher):
    def __init__(self, api_key=None, timeout=REQUESTS_TIMEOUT):
        super().__init__(timeout=timeout)
        self.api_key = api_key


    def fetch_population(self, area_code):
        url = f"{SEOUL_API_BASE_URL}/{self.api_key}/xml/citydata_ppltn/1/5/{area_code}"
        soup = self.get_data(url)
        area_info = soup.find("SeoulRtd.citydata_ppltn")
        data = {
            "area_code": area_code,
            "area_name": area_info.find("AREA_NM").text,
            "congest_lvl": area_info.find("AREA_CONGEST_LVL").text,
            "congest_msg": area_info.find("AREA_CONGEST_MSG").text,
            "population_min": int(area_info.find("AREA_PPLTN_MIN").text),
            "population_max": int(area_info.find("AREA_PPLTN_MAX").text),
            "male_rate": float(area_info.find("MALE_PPLTN_RATE").text),
            "female_rate": float(area_info.find("FEMALE_PPLTN_RATE").text),
            "age_rate_0": float(area_info.find("PPLTN_RATE_0").text),
            "age_rate_10": float(area_info.find("PPLTN_RATE_10").text),
            "age_rate_20": float(area_info.find("PPLTN_RATE_20").text),
            "age_rate_30": float(area_info.find("PPLTN_RATE_30").text),
            "age_rate_40": float(area_info.find("PPLTN_RATE_40").text),
            "age_rate_50": float(area_info.find("PPLTN_RATE_50").text),
            "age_rate_60": float(area_info.find("PPLTN_RATE_60").text),
            "age_rate_70": float(area_info.find("PPLTN_RATE_70").text),
            "resident_rate": float(area_info.find("RESNT_PPLTN_RATE").text),
            "non_resident_rate": float(area_info.find("NON_RESNT_PPLTN_RATE").text),
            "replace_yn": area_info.find("REPLACE_YN").text,
            "population_time": area_info.find("PPLTN_TIME").text
        }
        return data
    
    def fetch_and_save_all(self, area_codes):
        all_data = []
        cnt = 0
        for area_code in area_codes:
            if cnt == 5:break
            cnt += 1
            try:
                data = self.fetch_population(area_code)
                all_data.append(data)
            except Exception as e:
                print(f"[!] {area_code} 데이터 가져오기 실패: {e}")

        self.save_to_json(all_data)
    
    def save_to_json(self, data):
        today = datetime.today().strftime("%Y%m%d")
        output_path = f"data/seoul_population/{today}_population_data.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"[+] 저장 완료: {output_path}")
    