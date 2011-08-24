# Scrapy settings for scrapyapp1 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'scrapyapp1'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['scrapyapp1.spiders']
NEWSPIDER_MODULE = 'scrapyapp1.spiders'
DEFAULT_ITEM_CLASS = 'scrapyapp1.items.ScrapyappItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

