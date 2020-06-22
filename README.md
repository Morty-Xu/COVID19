# COVID19

本项目使用 Scrapy 爬虫框架，实现爬取[网易实时播报平台数据](https://wp.m.163.com/163/page/news/virus_report/index.html?_nw_=1&_anw_=1)的新冠肺炎疫情数据。

数据分为三个板块：

- **世界疫情数据：**

  主要数据有：国家名，总计确诊，总计疑似，总计治愈，总计死亡，总计重症，总计境外输入，上次更新时间

- **国内疫情数据：**

  主要数据有：省份名，今日确诊，今日疑似，今日治愈，今日死亡，今日重症，总计确诊，总计疑似，总计治愈，总计死亡，总计重症，总计境外输入，上次更新时间

- **每日疫情数据：**

  主要数据有：日期，当日确诊，当日疑似，当日治愈，当日死亡，当日重症，总计确诊，总计疑似，总计治愈，总计死亡，总计重症，总计境外输入



### 运行本项目

0. 安装 Scrapy 爬虫框架。[如何安装 Scrapy](https://scrapy-chs.readthedocs.io/zh_CN/latest/intro/install.html)

1. clone 项目到本地

   `git clone git@github.com:Morty-Xu/COVID19.git`

2. 转至项目主目录，执行以下命令：

   `scrapy crawl covid19`

3. 待程序运行完毕，会在项目主目录下生成三个文件（xxx前缀代表爬取时间，精确到小时）：

   - xxx-country.csv  对应 **世界疫情数据**

   - xxx-province.csv 对应 **国内疫情数据**

   - xxx-dayList.csv 对应 **每日疫情数据**

     
