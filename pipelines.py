# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


##class GplaycrawlerPipeline(object):
##    def process_item(self, item, spider):
##        return item

from scrapy import log  
from twisted.enterprise import adbapi  
from scrapy.http import Request  
from scrapy.exceptions import DropItem  
#from scrapy.contrib.pipeline.images import ImagesPipeline  
import time  
import psycopg2 

  
  
class GplayPipeline(object):  
  
    def __init__(self):  
        self.conn = psycopg2.connect("dbname='gplay' user='postgres' host='localhost' password=''")
##        self.links_seen = []
        
    def process_item(self, item, spider):
        if str(item['Link']).find('details?id') != - 1:
##        if item['Link'] in self.links_seen:
##            raise DropItem("Duplicate item found: %s" % item)
##        else:
##            self.links_seen.append(item['Link'])
          try:
              cur = self.conn.cursor()
##        cur.execute("insert into apps (link, item_name, updated, author, filesize, downloads, version, compatibility, content_rating, author_link, author_link_test, genre, price, rating_value, review_number, description, iap, developer_badge, physical_address, video_url, developer_id) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (item["Link"], item["Item_name"], item["Updated"], item["Author"], item["Filesize"], item["Downloads"], item["Version"], item["Compatibility"], item["Content_rating"], item["Author_link"], item["Author_link_test"], item["Genre"], item["Price"], item["Rating_value"], item["Review_number"], item["Description"], item["IAP"], item["Developer_badge"], item["Physical_address"], item["Video_URL"], item["Developer_ID"]))
              cur.execute("insert into apps (app_id, item_name, updated, author, filesize, downloads, version, compatibility, content_rating, author_link, genre, price, rating_value, review_number, description, iap, developer_badge, physical_address, video_url, developer_id) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (item["Link"][46:], item["Item_name"], item["Updated"], item["Author"], item["Filesize"], item["Downloads"], item["Version"], item["Compatibility"], item["Content_rating"], item["Author_link"], item["Genre"], item["Price"], item["Rating_value"], item["Review_number"], item["Description"], item["IAP"], item["Developer_badge"], item["Physical_address"], item["Video_URL"], item["Developer_ID"]))
              self.conn.commit()
          except:
              self.conn.rollback()
        return item  
