import scrapy


class ProductItem(scrapy.Item):
    """A single scraped product record.

    Kept flat and CSV-friendly on purpose -- most freelance clients
    open the output in Excel or Google Sheets, not a database.
    """
    title = scrapy.Field()
    price_gbp = scrapy.Field()
    in_stock = scrapy.Field()
    rating = scrapy.Field()
    product_url = scrapy.Field()
    scraped_at = scrapy.Field()
