# E-commerce Price Tracker (Scrapy)

A crawl-the-whole-catalog scraper: follows pagination automatically,
visits every product page, and exports a clean, timestamped CSV.

**What this demonstrates for a client-facing gig:**
- Full-site crawling with pagination, not just a single page
- Polite-scraper defaults (robots.txt respected, throttled, retries
  on transient errors) so the target site doesn't get hammered or
  the job doesn't die on one flaky request
- A pipeline architecture (`pipelines.py`) that separates *scraping*
  from *exporting* -- swapping CSV for a database or Google Sheets
  later is a pipeline change, not a rewrite

## Run it

```bash
pip install -r requirements.txt
scrapy crawl books
```

Output lands in `output/products_<timestamp>.csv`.

## Adapting for a real client job

1. Change `start_urls` and `allowed_domains` in `books_spider.py`
2. Update the CSS selectors in `parse()` / `parse_product()` to match
   the target site's HTML (use browser devtools to find them)
3. If the site requires a rendered browser (heavy JS), route requests
   through Splash or swap to the Selenium project in this portfolio
   instead

## Typical use case

Price monitoring, catalog audits, lead lists, or any "get me every
row of X from this site" request -- the highest-volume category of
freelance scraping gigs.
