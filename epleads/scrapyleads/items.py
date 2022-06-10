# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from ast import Add
import scrapy


class ScrapyleadsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Address(scrapy.Item):
    address_lines = scrapy.Field()
    city = scrapy.Field()
    district = scrapy.Field()
    postcode = scrapy.Field()

class ContactPerson(scrapy.Item):
    name = scrapy.Field()
    position = scrapy.Field()
    primary_contact = scrapy.Field(serializer=bool)

class Centre(scrapy.Item):
    name = scrapy.Field()
    group = scrapy.Field()
    address = scrapy.Field(serializer=Address)
    opening_days = scrapy.Field()
    opening_hours = scrapy.Field()
    persons = scrapy.Field()
