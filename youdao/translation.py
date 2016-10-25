#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import urllib.request
import json
import os
content=input("请输入你要翻译的内容:")
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link"
headers={"User-Agent":"test"}
data = {}
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = "json"
data['xmlVersion'] = "1.8"
data['keyfrom'] = "fanyi.web"
data['ue'] = "UTF-8"
data['action'] = "FY_BY_CLICKBUTTON"
print(type(data))
print(data)
data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url, data)
req.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36")
respone = urllib.request.urlopen(req)
html = respone.read().decode("utf-8")
print(req.headers)
target = json.loads(html)
print(target['translateResult'][0][0]['tgt'])
