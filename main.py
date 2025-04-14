from src.popply_crawler import PopplyCrawler

def main():
    crawler = PopplyCrawler()
    try:
        crawler.crawl_popups()
        crawler.save_to_json()
    finally:
        crawler.quit()

if __name__ == "__main__":
    main()
