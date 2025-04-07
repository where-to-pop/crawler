import time
import json
from datetime import datetime
from crawler.base_crawler import BaseCrawler
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from configs import settings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PopplyCrawler(BaseCrawler):
    def __init__(self):
        super().__init__()
        self.base_url = settings.POPPLY_POPUP_LIST_URL
        self.popup_list = []
        self.use_scroll = False

    def scroll_to_bottom(self, max_scrolls=10):
        scroll_count = 0
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while scroll_count < max_scrolls:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # 콘텐츠 로딩 기다림

            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print("[*] 더 이상 스크롤할 콘텐츠 없음. 중단.")
                break

            last_height = new_height
            scroll_count += 1
            print(f"[+] 스크롤 {scroll_count}회 완료")

        if scroll_count >= max_scrolls:
            print("[!] 최대 스크롤 횟수 도달. 강제 종료.")

    def crawl_popups(self):
        self.driver.get(self.base_url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.popup-info-wrap"))
        )

        if self.use_scroll:
            self.scroll_to_bottom()
        time.sleep(2)

        items = self.driver.find_elements(By.CSS_SELECTOR, "div.popup-info-wrap")
        print(f"[+] 팝업 항목 {len(items)}개 발견됨")

        seen_links = set()

        # 팝업 아이템들 추출
        items = self.driver.find_elements(By.CSS_SELECTOR, "a[href^='/popup/']")
        for item in items:
            try:
                title = item.find_element(By.CSS_SELECTOR, ".popup-name p").text.strip()
                location = item.find_element(By.CSS_SELECTOR, ".popup-location").text.strip()
                period = item.find_element(By.CSS_SELECTOR, ".popup-date").text.strip()
                link_tag = item.find_element(By.XPATH, "../a") 
                relative_url = link_tag.get_attribute("href")

                if not title or relative_url in seen_links:
                    continue
                seen_links.add(relative_url)

                self.popup_list.append({
                    "title": title,
                    "location": location,
                    "period": period,
                    "link": relative_url,
                })

            except NoSuchElementException:
                print("[!] popup-name 없음, 스킵")
                print(item.get_attribute("outerHTML"))
            except Exception as e:
                print(f"[!] 항목 파싱 실패: {e}")
                print(item.get_attribute("outerHTML"))

    def save_to_json(self):
        today = datetime.today().strftime("%Y%m%d")
        output_path = f"data/popply/{today}_popply_popups.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(self.popup_list, f, ensure_ascii=False, indent=2)
        print(f"[+] 저장 완료: {output_path}")
