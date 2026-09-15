import scrapy

from price_tracker.items import ProductItem


class BooksSpider(scrapy.Spider):
    """Scrapes product listings from books.toscrape.com.

    This site is a public sandbox built specifically for practicing
    scrapers, so it's used here as a stand-in for a real client target
    (e.g. a competitor's storefront or a supplier catalog). Swap
    `start_urls` and the CSS selectors in `parse` / `parse_product` to
    point this at a real site -- the pagination and pipeline logic
    stays the same.
    """

    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        for book in response.css("article.product_pod"):
            relative_url = book.css("h3 a::attr(href)").get()
            yield response.follow(relative_url, callback=self.parse_product)

        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_product(self, response):
        item = ProductItem()
        item["title"] = response.css("h1::text").get(default="").strip()

        price_text = response.css("p.price_color::text").get(default="")
        item["price_gbp"] = price_text.replace("£", "").strip()

        availability = response.css("p.availability::text").getall()
        item["in_stock"] = "In stock" in "".join(availability)

        rating_class = response.css("p.star-rating::attr(class)").get(default="")
        item["rating"] = rating_class.replace("star-rating", "").strip()

        item["product_url"] = response.url
        yield item
