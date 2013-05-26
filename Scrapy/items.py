# encoding:utf8

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
from scrapy.contrib.djangoitem import DjangoItem
from Robot.models import WeiboUser


class ScrapyItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass


class WeiboUserItem(DjangoItem):
    django_model = WeiboUser