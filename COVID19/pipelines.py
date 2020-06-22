# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import datetime
from COVID19.items import CountryItem, ProvinceItem, DayListItem


class Covid19Pipeline(object):
    def __init__(self):
        now_time = datetime.datetime.now().strftime('%Y%m%d%H')

        country_file_name = str(now_time) + 'country' + '.csv'
        self.country_file = open(country_file_name, 'a+', encoding='utf-8', newline='')
        self.country_writer = csv.writer(self.country_file)

        province_file_name = str(now_time) + '-' + 'province' + '.csv'
        self.province_file = open(province_file_name, 'a+', encoding='utf-8', newline='')
        self.province_writer = csv.writer(self.province_file)

        dayList_file_name = str(now_time) + '-' + 'dayList' + '.csv'
        self.dayList_file = open(dayList_file_name, 'a+', encoding='utf-8', newline='')
        self.dayList_writer = csv.writer(self.dayList_file)

    def open_spider(self, spider):
        self.country_writer.writerow(['国家名', '总计确诊', '总计疑似', '总计治愈', '总计死亡', '总计重症', '总计境外输入', '上次更新时间'])
        self.province_writer.writerow(['省份名', '今日确诊', '今日疑似', '今日治愈', '今日死亡', '今日重症', '总计确诊', '总计疑似',
                                       '总计治愈', '总计死亡', '总计重症', '总计境外输入', '上次更新时间'])
        self.dayList_writer.writerow(['日期', '当日确诊', '当日疑似', '当日治愈', '当日死亡', '当日重症', '总计确诊', '总计疑似',
                                      '总计治愈', '总计死亡', '总计重症', '总计境外输入'])

    def process_item(self, item, spider):
        # print(type(item))
        if isinstance(item, CountryItem):
            self.country_writer.writerow([
                item['name'], item['total_confirm'], item['total_suspect'], item['total_heal'], item['total_dead'],
                item['total_severe'], item['total_input'], item['lastUpdateTime']
            ])
            return item
        elif isinstance(item, ProvinceItem):
            self.province_writer.writerow([
                item['name'], item['today_confirm'], item['today_suspect'], item['today_heal'], item['today_dead'],
                item['today_severe'], item['total_confirm'], item['total_suspect'], item['total_heal'],
                item['total_dead'], item['total_severe'], item['total_input'], item['lastUpdateTime']
            ])
            return item
        elif isinstance(item, DayListItem):
            self.dayList_writer.writerow([
                item['date'], item['today_confirm'], item['today_suspect'], item['today_heal'], item['today_dead'],
                item['today_severe'], item['total_confirm'], item['total_suspect'], item['total_heal'],
                item['total_dead'], item['total_severe'], item['total_input']
            ])
            return item

    def close_spider(self, spider):
        self.country_file.close()
        self.province_file.close()
        self.dayList_file.close()
