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

connect = Connection()

def appdetails(appid):
    req = connect.request("?request=appdetails&appid={}".format(appid))
    return Response(req.status_code, req.json())

def genre(genre):
    req = connect.request("?request=appdetails&appid={}".format(genre))
    return Response(req.status_code, req.json())

def top100in2weeks():
    req = connect.request("?request=top100in2weeks")
    return Response(req.status_code, req.json())

def top100forever():
    req = connect.request("?request=top100forever")
    return Response(req.status_code, req.json())

def top100owned():
    req = connect.request("?request=top100owned")
    return Response(req.status_code, req.json())

def all():
    req = connect.request("?request=all")
    return Response(req.status_code, req.json())
