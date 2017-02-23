# -*- coding: utf-8 -*-
from connection import connection

class Api():
    def __init__(self):
        self.connection = connection.Connection()

    def appdetails(self,appid):
        req = self.connection.request("?request=appdetails&appid={}".format(appid))
        return Response(req.status_code, req.json())

    def genre(self,genre):
        req = self.connection.request("?request=appdetails&appid={}".format(genre))
        return Response(req.status_code, req.json())

    def top100in2weeks(self):
        req = self.connection.request("?request=top100in2weeks")
        return Response(req.status_code, req.json())

    def top100forever(self):
        req = self.connection.request("?request=top100forever")
        return Response(req.status_code, req.json())

    def top100owned(self):
        req = self.connection.request("?request=top100owned")
        return Response(req.status_code, req.json())

    def all(self):
        req = self.connection.request("?request=all")
        return Response(req.status_code, req.json())
