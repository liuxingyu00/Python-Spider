import requests
from lxml import etree
from fake_useragent import UserAgent
#伪装
ua = UserAgent()
headers = {'User-Agent':ua.random}
def get_ip():
    ip_list = []
    #路径
    url = 'https://www.xicidaili.com/nt/' #ip是有时效的，只爬取第一页
    #请求
    response = requests.get(url=url,headers=headers)
    #设置编码
    response.encoding = response.apparent_encoding
    response = response.text

    response = etree.HTML(response)

    tr_list = response.xpath('//tr[@class="odd"]')
    for i in tr_list:
        #ip
        ip = i.xpath('./td[2]/text()')[0]
        #端口号
        port = i.xpath('./td[3]/text()')[0]
        #协议
        agreement = i.xpath('./td[6]/text()')[0]
        agreement = agreement.lower()
        #拼装完整路径
        ip = agreement + '://' + ip + ':' + port
        ip_list.append(ip)
    return ip_list

if __name__ == '__main__':
    ip_list = get_ip()
    print(ip_list)

