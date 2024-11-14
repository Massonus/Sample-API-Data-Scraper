import json

import pytest
from scrapy.http import TextResponse, Request

from code_resources.code_resources.spiders.coding_resources_spider import CodingResourcesSpider


@pytest.fixture
def mock_response():
    data = [
        {
            "id": 1,
            "description": "A sample coding resource",
            "url": "https://example.com",
            "types": ["tutorial"],
            "topics": ["web development"],
            "levels": ["beginner"]
        },
        {
            "id": 2,
            "description": "Another coding resource",
            "url": "https://example2.com",
            "types": ["documentation"],
            "topics": ["data science"],
            "levels": ["intermediate"]
        }
    ]

    url = "https://api.sampleapis.com/codingresources/codingResources"
    request = Request(url=url)
    response = TextResponse(url=url, request=request, body=json.dumps(data), encoding='utf-8')
    return response


def test_parse(mock_response):
    spider = CodingResourcesSpider()
    parsed_items = list(spider.parse(mock_response))

    assert len(parsed_items) == 2

    assert parsed_items[0]["id"] == 1
    assert parsed_items[0]["description"] == "A sample coding resource"
    assert parsed_items[0]["url"] == "https://example.com"
    assert parsed_items[0]["types"] == ["tutorial"]
    assert parsed_items[0]["topics"] == ["web development"]
    assert parsed_items[0]["levels"] == ["beginner"]

    assert parsed_items[1]["id"] == 2
    assert parsed_items[1]["description"] == "Another coding resource"
    assert parsed_items[1]["url"] == "https://example2.com"
    assert parsed_items[1]["types"] == ["documentation"]
    assert parsed_items[1]["topics"] == ["data science"]
    assert parsed_items[1]["levels"] == ["intermediate"]
