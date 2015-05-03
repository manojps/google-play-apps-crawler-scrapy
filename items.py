# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

#from scrapy.item import Item, Field
import scrapy

class GplaycrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = Field()
    Link = scrapy.Field()
    Item_name = scrapy.Field()
    Updated = scrapy.Field()
    Author = scrapy.Field()
    Filesize = scrapy.Field()
    Downloads = scrapy.Field()
    Version = scrapy.Field()
    Compatibility = scrapy.Field()
    Content_rating = scrapy.Field()
    Author_link = scrapy.Field()
##    Author_link_test = scrapy.Field()
    Genre = scrapy.Field()
    Price = scrapy.Field()
    Rating_value = scrapy.Field()
    Review_number = scrapy.Field()
    Description = scrapy.Field()
    IAP = scrapy.Field()
    Developer_badge = scrapy.Field()
    Physical_address = scrapy.Field()
    Video_URL = scrapy.Field()
    Developer_ID = scrapy.Field()


