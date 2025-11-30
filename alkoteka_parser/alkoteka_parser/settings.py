# Scrapy settings for alkoteka_parser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import os
from datetime import datetime

LOG_ENABLED = True
LOG_LEVEL = 'INFO'

log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
LOG_FILE = os.path.join(log_dir, f'alkoteka_{current_time}.log')

BOT_NAME = "alkoteka_parser"

SPIDER_MODULES = ["alkoteka_parser.spiders"]
NEWSPIDER_MODULE = "alkoteka_parser.spiders"

# Убедитесь, что это значение не используется, если не требуется
ADDONS = {}

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'alkoteka_parser.pipelines.AlkotekaParserPipeline': 1,  # Убедитесь, что путь к пайплайну правильный
}

DOWNLOAD_DELAY = 1.5
RANDOMIZE_DOWNLOAD_DELAY = True
CONCURRENT_REQUESTS = 1

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# Set settings whose default value is deprecated to a future-proof value
FEED_EXPORT_ENCODING = "utf-8"
