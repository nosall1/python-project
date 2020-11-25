#-*- coding:utf-8 -*-
import re
import ssl

import requests
from pprint import pprint



url='https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9017'
response=requests.get(url,verify=False)
station=re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',response.text)
pprint(dict(station),indent=4)
