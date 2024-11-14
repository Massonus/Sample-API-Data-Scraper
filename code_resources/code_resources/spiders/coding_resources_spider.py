import scrapy
import json

class CodingResourcesSpider(scrapy.Spider):
    name = "coding_resources_spider"
    start_urls = ["https://api.sampleapis.com/codingresources/codingResources"]

    def parse(self, response):
        data = json.loads(response.text)
        for item in data:
            yield {
                "id": item.get("id"),
                "description": item.get("description"),
                "url": item.get("url"),
                "types": item.get("types"),
                "topics": item.get("topics"),
                "levels": item.get("levels"),
            }
