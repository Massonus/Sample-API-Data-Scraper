BOT_NAME = "code_resources"

SPIDER_MODULES = ["code_resources.spiders"]
NEWSPIDER_MODULE = "code_resources.spiders"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'code_resources.pipelines.MongoPipeline': 1,
}

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
