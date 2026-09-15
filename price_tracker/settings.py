BOT_NAME = "price_tracker"

SPIDER_MODULES = ["price_tracker.spiders"]
NEWSPIDER_MODULE = "price_tracker.spiders"

# Be a polite scraper: this single setting is often the difference
# between a client's target site staying reachable and getting your
# IP rate-limited or banned mid-job.
ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 1.0
RANDOMIZE_DOWNLOAD_DELAY = True
CONCURRENT_REQUESTS_PER_DOMAIN = 4

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1.0
AUTOTHROTTLE_MAX_DELAY = 10.0
AUTOTHROTTLE_TARGET_CONCURRENCY = 2.0

RETRY_ENABLED = True
RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 429]

ITEM_PIPELINES = {
    "price_tracker.pipelines.CsvExportPipeline": 300,
}

FEED_EXPORT_ENCODING = "utf-8"
LOG_LEVEL = "INFO"

USER_AGENT = "price-tracker-bot (+contact: your-email@example.com)"
