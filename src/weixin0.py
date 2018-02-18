# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: weixin0.py
@time: 2018/2/17 下午11:38
"""
import urllib
import json

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
def getinfo(info):
    key = '4a54abfe57804df0bf5a5a8e97ab45f6'
    api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='

    request = api + info
    response = getHtml(request)
    dic_json = json.loads(response)
    return dic_json['text']

if __name__ == '__main__':

    key = '4a54abfe57804df0bf5a5a8e97ab45f6'
    api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='

    while True:
        info = raw_input('我: ')
        print type(info)
        # request = api + info
        # response = getHtml(request)
        # dic_json = json.loads(response)
        print '贾维斯：'.decode('utf-8') +getinfo(info)








