# coding: utf-8
def get_news():
    # coding:utf-8
    import requests
    from lxml import etree
    import os, sys, io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

    host = '192.168.56.167'
    port = 3306
    user = 'root'
    password = 'Sanchuang123#'

    import pymysql
    conn = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        db='omy',
        charset='utf8'
    )

    cursor = conn.cursor()
    sql = """drop table if exists news"""
    cursor.execute(sql)
    sql = """CREATE TABLE news (
             id INT NOT NULL AUTO_INCREMENT,
             title CHAR(50),
             url varchar(100),
             content text,
             ctime varchar(30),
             PRIMARY KEY (id))"""
    cursor.execute(sql)

    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }

    for i in range(20):
        page = i
        q = '新冠肺炎'
        size = 10
        url = f"""https://search.sina.com.cn/?q={q}&c=news&from=&col=&range=all&source=&country=&size={size}&stime=&etime=&time=&dpc=0&a=&ps=0&pf=0&page={page}"""
        response = requests.get(url=url)
        text = response.text
        text = text.replace("<font color='red'>", "")
        text = text.replace("</font>", "")
        html = etree.HTML(text, etree.HTMLParser())
        msg = html.xpath('//*[@id="result"]/div[@class="box-result clearfix"]')
        for j in range(len(msg)):
            title = html.xpath(f'//*[@id="result"]/div[@class="box-result clearfix"][{j + 1}]/h2/a/text()')
            if len(title) == 0:
                title = html.xpath(f'//*[@id="result"]/div[@class="box-result clearfix"][{j + 1}]/div/h2/a/text()')

            url = html.xpath(f'//*[@id="result"]/div[@class="box-result clearfix"][{j + 1}]/h2/a/@href')
            if len(url) == 0:
                url = html.xpath(f'//*[@id="result"]/div[@class="box-result clearfix"][{j + 1}]/div/h2/a/@href')

            content = html.xpath(
                f'//*[@id="result"]/div[@class="box-result clearfix"][{j + 1}]/div[@class="r-info"]/p[@class="content"]/text()')
            if len(content) == 0:
                content = html.xpath(f'//*[@id="result"]/div[@class="box-result clearfix"][{j + 1}]/div/p/text()')

            ctime = html.xpath(f'//*[@id="result"]/div[@class="box-result clearfix"][{j + 1}]/h2/span/text()')
            if len(ctime) == 0:
                ctime = html.xpath(f'//*[@id="result"]/div[@class="box-result clearfix"][{j + 1}]/div/h2/span/text()')
            print(f"""标题： {title}    链接: {url}   内容: {content}   时间: {ctime}""")

            sql = f"""INSERT INTO news(title,
                     url, content, ctime)
                     VALUES ('{title[0]}', '{url[0]}', '{content[0]}', '{ctime[0]}')"""
            try:
                # 执行sql语句
                cursor.execute(sql)
                # 执行sql语句
                conn.commit()
            except:
                # 发生错误时回滚
                conn.rollback()

    conn.close()


# def get_news_info():
