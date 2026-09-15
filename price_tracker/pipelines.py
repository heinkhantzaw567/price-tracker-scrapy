import csv
import os
from datetime import datetime, timezone


class CsvExportPipeline:
    """Writes every scraped item straight to a timestamped CSV.

    Clients almost never want a database -- they want a file they can
    open. Timestamping the filename also means re-running the job
    tomorrow never overwrites today's delivery.
    """

    def open_spider(self, spider):
        os.makedirs("output", exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        self.filepath = f"output/products_{stamp}.csv"
        self.file = open(self.filepath, "w", newline="", encoding="utf-8")
        self.writer = None

    def process_item(self, item, spider):
        row = dict(item)
        row["scraped_at"] = datetime.now(timezone.utc).isoformat()
        if self.writer is None:
            self.writer = csv.DictWriter(self.file, fieldnames=row.keys())
            self.writer.writeheader()
        self.writer.writerow(row)
        return item

    def close_spider(self, spider):
        self.file.close()
        spider.logger.info(f"Saved results to {self.filepath}")
