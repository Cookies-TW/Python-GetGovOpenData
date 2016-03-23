import time
import urllib3
import datetime
import requests
import urllib.request
import re

#REF: https://docs.python.org/2/library/xml.etree.elementtree.html

response = urllib.request.urlopen("http://opendata.epa.gov.tw/webapi/api/rest/datastore/355000000I-000001/?format=xml&limit=1&offset=0")
'''soup = beautifulsoup4(response)
print(soup)
if response.read().decode('utf_8') is '麥寮':
    print(response.read().decode('utf_8'))''' 
print(response.read().decode('utf_8'))
if re.match("雲林縣",response.read().decode('utf_8')):
    print(response.read().decode('utf_8'))
