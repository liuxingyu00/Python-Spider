import requests
from multiprocessing.dummy import Pool
#获取爬取到的ip列表
from 搭建IP代理池.IPPool import get_ip
test_list = get_ip()
#定义一个全局列表，用来存放有效ip
ip_list = []
#ip测试网站
url = 'http://icanhazip.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'
}
def ip_test(ip):
    try:
        if ip.split(":")[0] == 'http':
            proxies = {
                'http': ip
            }
        else:
            proxies = {
                'https': ip
            }
        response = requests.get(url=url, headers=headers, proxies=proxies, timeout=3)
        ip_list.append(ip)
        print(ip + "可用")
    except:
        print(ip + "不可用")
if __name__ == '__main__':
    pool = Pool(4)
    pool.map(ip_test, test_list)
    print(ip_list)
    print("总共爬取%s个ip，可用ip为：%s，不可用ip为：%s"%(len(test_list),len(ip_list),len(test_list)-len(ip_list)))
