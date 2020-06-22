# -*- coding: utf-8 -*-
import scrapy
import json
from COVID19.items import CountryItem, ProvinceItem, DayListItem


def render_null(data):
    if not data:
        return 0
    else:
        return data


class Covid19Spider(scrapy.Spider):
    name = 'covid19'
    allowed_domains = ['c.m.163.com']
    start_urls = ['https://c.m.163.com/ug/api/wuhan/app/data/list-total']

    def parse(self, response):
        r = json.loads(response.text)
        # 源数据
        d = r['data']
        # 处理国际疫情数据
        data_intl = d['areaTree']
        for country in data_intl:
            item = CountryItem()
            item['name'] = country['name']
            item['total_confirm'] = country['total']['confirm']
            item['total_suspect'] = country['total']['suspect']
            item['total_heal'] = country['total']['heal']
            item['total_dead'] = country['total']['dead']
            item['total_severe'] = country['total']['severe']
            if 'input' in country['total'].keys():
                item['total_input'] = country['total']['input']
            else:
                item['total_input'] = 0
            item['lastUpdateTime'] = country['lastUpdateTime']
            yield item

        # 处理国内疫情数据
        data_prov = d['areaTree'][2]['children']
        for province in data_prov:
            item = ProvinceItem()
            item['name'] = province['name']
            item['today_confirm'] = render_null(province['today']['confirm'])
            item['today_suspect'] = render_null(province['today']['suspect'])
            item['today_heal'] = render_null(province['today']['heal'])
            item['today_dead'] = render_null(province['today']['dead'])
            item['today_dead'] = render_null(province['today']['dead'])
            item['today_severe'] = render_null(province['today']['severe'])
            item['total_confirm'] = province['total']['confirm']
            item['total_suspect'] = province['total']['suspect']
            item['total_heal'] = province['total']['heal']
            item['total_dead'] = province['total']['dead']
            item['total_severe'] = province['total']['severe']
            if 'input' in province['total'].keys():
                item['total_input'] = province['total']['input']
            else:
                item['total_input'] = 0
            item['lastUpdateTime'] = province['lastUpdateTime']
            yield item

        # 处理每日疫情数据
        data_dayList = d['chinaDayList']
        for dayList in data_dayList:
            item = DayListItem()
            item['date'] = dayList['date']
            item['today_confirm'] = render_null(dayList['today']['confirm'])
            item['today_suspect'] = render_null(dayList['today']['suspect'])
            item['today_heal'] = render_null(dayList['today']['heal'])
            item['today_dead'] = render_null(dayList['today']['dead'])
            item['today_dead'] = render_null(dayList['today']['dead'])
            item['today_severe'] = render_null(dayList['today']['severe'])
            item['total_confirm'] = dayList['total']['confirm']
            item['total_suspect'] = dayList['total']['suspect']
            item['total_heal'] = dayList['total']['heal']
            item['total_dead'] = dayList['total']['dead']
            item['total_severe'] = dayList['total']['severe']
            if 'input' in dayList['total'].keys():
                item['total_input'] = dayList['total']['input']
            else:
                item['total_input'] = 0
            yield item

