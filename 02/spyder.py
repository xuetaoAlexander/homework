#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup
from urllib import request
import requests
import ssl
import re
from collections import defaultdict
import json
import io

#gcontext = ssl._create_unverified_context()
#
#url = "https://www.bjsubway.com/e/action/ListInfo/?classid=39&ph=1"
##url = " https://www.bjsubway.com/station/xltcx/"
#        
#header  = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
#        
#rq = request.Request(url, headers = header)
#res = request.urlopen(rq, context = gcontext)
#html = res.read().decode("gbk")
#        
#soup =  BeautifulSoup(html, features = 'lxml')
#print(soup)
#

def get_coordinate(my_address):
    """
    "7951a54f65672be938cd83a4cd871aa2"
    """
    gaode_url = "https://restapi.amap.com/v3/place/text?"
    params = {
         "keywords" : my_address,
         "key": "cdcb3787a7146c39b936e3f67a7a9217",
         "city": "北京",
         "types": "150500",
         "offset": "1"
      
    } 
    data = requests.get(gaode_url, params).text
    data = json.loads(data)
    print(data)
      
    return data['pois'][0]['location']
      
      
#subway_content = soup.find_all('div', {"class": "line_content"})
      
      
pattern1 = re.compile("(\s+(详询|数据).+)")
pattern2 = re.compile("(.+线)")
       
       
station_locate = defaultdict()
lines = defaultdict(list)
       
fs = open('./subway.csv', 'r',encoding = 'utf8')
fl = open('./location.csv', 'w+',encoding = 'utf8')
       
       
#for content in subway_content:
#    stations = content.get_text()
#    for st in stations.split('\n'):
#         if st.strip() == "": continue
#         if pattern1.search(st):
#             st = pattern1.sub("", st)
#         if pattern2.search(st):
#             key = pattern2.search(st).group(0)
#             continue
#         if key != "":
#             lines[key].append(st)
#            station_locate[st] = get_coordinate(st)
#            print(st + ":" + station_locate[st] + "\n")
#            fl.write(st + ":" + station_locate[st] + "\n")
#            

for line in fs:
    sts = line.split(":")[1].split(",")
    for st in sts:
        st = st.strip("\n")
        station_locate[st] = get_coordinate(st)
        print(st + ":" + station_locate[st] + "\n")
        fl.write(st + ":" + station_locate[st] + "\n")

#for key, value in lines.items():
#    print(value)
#    fs.write(key + ":" + ",".join(value) + "\n")
#    

