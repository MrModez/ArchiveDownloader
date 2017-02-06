import archive_downloader
import codecs
import datetime
import json
from pprint import pprint
import urllib.request

with open('data.json') as data_file:    
    data = json.load(data_file)

y0 = data["y0"]
y1 = data["y0"]
province_raw = data["province"]
province = urllib.parse.quote_plus(province_raw)
dist_raw = data["district"]
dist = urllib.parse.quote_plus(dist_raw)
key = data["key"]

names_raw = data["places"]
names = []
for name in names_raw:
	names.extend(name.split(', '))

for name_raw in names:
	name_fix = name_raw[:-2]
	name = urllib.parse.quote_plus(name_fix)
	query = "/?places={}&mode=1&fe=1&_y0={}&_y1={}&_p={}&_d={}&_dn=&_n=&pNo=1&cnt=1&pSz=100&rc=4".format(name, y0, y1, province, dist)
	pprint("Checking {}".format(name_raw))
	date = datetime.datetime.now()
	st = date.strftime("%Y-%m-%d %H-%M-%S")  
	archive_downloader.start(query, key, st)
