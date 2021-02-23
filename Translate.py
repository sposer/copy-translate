#-*- coding:utf-8 -*-
from typing import Any
import requests
import random
import hashlib
import json

from requests.api import get


class Translate():
    def __init__(self, txt) -> None:
        self.appid = "20181223000251520"
        self.appkey = "Qn9_yLNTnUzde2Hk2Fqg"
        self.salt = str(random.randint(00000000,99999999))
        self.txt = txt
        pass


    def encodeStr(self) -> Any:
        try:
            txt = self.txt.encode("utf-8")
            return txt
        except UnicodeEncodeError:
            return 'ERROR'


    def getMd5(self):
        mMd5 = hashlib.md5()
        mMd5.update((self.appid + self.txt + self.salt + self.appkey).encode("utf8"))
        return mMd5.hexdigest()


    def doPost(self) -> Any:
        url = "https://fanyi-api.baidu.com/api/trans/vip/translate"
        data = {}
        data["q"] = self.encodeStr()
        data["from"] = "auto"
        data["to"] = "zh"
        data["appid"] = self.appid
        data["salt"] = self.salt
        data["sign"] = self.getMd5()
        #print(data)
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        res = requests.post(url=url, data=data, headers=headers)
        #print(json.loads(res.text)["trans_result"][0]["dst"])
        try:
            return json.loads(res.text)["trans_result"][0]["dst"]
        except:
            return "Error"
