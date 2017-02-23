# -*- coding: utf-8 -*-
import requests

class Connection():
    base_url = 'https://steamspy.com/api.php'
    def request(self,url):
        body = requests.get(self.base_url + url)
        return body

class Response():
    def __init__(self,status,data):
        self.status = status
        self.data = data
