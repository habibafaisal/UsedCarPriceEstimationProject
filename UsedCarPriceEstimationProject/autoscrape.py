from autoscraper import AutoScraper

url_to_scrape = "https://www.pakwheels.com"
WantedList = ["https://www.pakwheels.com/used-cars/search/-/mk_suzuki/md_alto/"]

Scraper = AutoScraper()
ScrapedData = Scraper.build(url_to_scrape, wanted_list=WantedList)
print(ScrapedData)