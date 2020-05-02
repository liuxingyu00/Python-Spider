import requests
from fake_useragent import UserAgent
import random

ua = UserAgent()
headers = {'User-Agent':ua.random}
proxies = [{'https':'//14.115.106.121:808'},
           {'https':'//14.20.235.97:9797'},
           {'https':'//59.36.10.74:3128'},
           {'https':'//59.38.60.188:9797'},
           {'https':'//14.115.107.169:808'}]
proxy = random.choice(proxies)
print(headers)
print(proxy)
