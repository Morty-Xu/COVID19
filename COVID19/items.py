# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Covid19Item(scrapy.Item):
    # define the fields for your item here like:
    pass


class CountryItem(scrapy.Item):
    name = scrapy.Field() # 国家名

    total_confirm = scrapy.Field() # 总计确诊

    total_suspect = scrapy.Field() # 总计疑似

    total_heal = scrapy.Field() # 总计治愈

    total_dead = scrapy.Field() # 总计死亡

    total_severe = scrapy.Field() # 总计重症

    total_input = scrapy.Field() # 总计境外输入

    lastUpdateTime = scrapy.Field() # 上次更新时间


class ProvinceItem(scrapy.Item):
    name = scrapy.Field() # 省份名

    today_confirm = scrapy.Field()  # 今日确诊

    today_suspect = scrapy.Field()  # 今日疑似

    today_heal = scrapy.Field()  # 今日治愈

    today_dead = scrapy.Field()  # 今日死亡

    today_severe = scrapy.Field()  # 今日重症

    total_confirm = scrapy.Field() # 总计确诊

    total_suspect = scrapy.Field() # 总计疑似

    total_heal = scrapy.Field() # 总计治愈

    total_dead = scrapy.Field() # 总计死亡

    total_severe = scrapy.Field() # 总计重症

    total_input = scrapy.Field() # 总计境外输入

    lastUpdateTime = scrapy.Field() # 上次更新时间


class DayListItem(scrapy.Item):
    date = scrapy.Field() # 日期

    today_confirm = scrapy.Field() # 当日确诊

    today_suspect = scrapy.Field() # 当日疑似

    today_heal = scrapy.Field() # 当日治愈

    today_dead = scrapy.Field() # 当日死亡

    today_severe = scrapy.Field() # 当日重症

    total_confirm = scrapy.Field()  # 总计确诊

    total_suspect = scrapy.Field()  # 总计疑似

    total_heal = scrapy.Field()  # 总计治愈

    total_dead = scrapy.Field()  # 总计死亡

    total_severe = scrapy.Field()  # 总计重症

    total_input = scrapy.Field()  # 总计境外输入