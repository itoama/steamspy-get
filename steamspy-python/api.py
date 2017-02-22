#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 17:50:54 2017

@author: TakahiroKONNO
"""
import requests
import bs4
import json
from time import sleep 
import pandas as pd

#get list of indie appid
url = "http://steamspy.com/genre/Indie"
resp = requests.get(url)
html = resp.text.encode(resp.encoding)

soup = bs4.BeautifulSoup(html,"lxml")
apps = soup.find('tbody').find_all('tr')

appid = []
for tag in apps:
    id = tag.find('a')['href'].replace("/app/","")
    appid.append(id)

#get appdetails    
d = []
i = 0
for id in appid:
    apiurl = 'http://steamspy.com/api.php?request=appdetails&appid=' + id
    apiresp = requests.get(apiurl)
    data = json.loads(apiresp.text)
    d.append(data)
    sleep(0.25)
    print(i)
    i += 1

#dict to csv     
n = 0
df = pd.DataFrame(d[n], index = [n,])
for appdetail in d:
    if n == len(appid) - 1:
        break
    n += 1
    df2 = pd.DataFrame(d[n], index = [n,])
    df = df.append(df2)
    
df.to_csv("data.csv", sep=',')
    
    