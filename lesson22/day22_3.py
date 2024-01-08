# @Time    : 2024/1/8 AM11:27
# @Author  : kang
# @File    : day22_3.py
# @Desc    :

import requests

resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
if resp.status_code == 200:
    data_model = resp.json()
    print("data resp===="+data_model)
    for news in data_model['newslist']:
        print(news['title'])
        print(news['url'])
        print('-' * 60)