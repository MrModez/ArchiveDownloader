import os
import json
import http.client
from pprint import pprint
import urllib.request

site = "edoclib.gasrb.ru"
img = "http://" + site + "/imgo.jpg?id="
query = "/?places=%D0%B1%D0%B5%D0%B3%D0%B5%D0%BD%D1%8F%D1%88&mode=1&tm=1486196983106&fe=1&_y0=&_y1=&_p=&_d=&_dn=&_n=&pNo=1&cnt=1&pSz=100&rc=9"
attrib = "&rH=059d0024b12efbc1e9a4faaf21435d6d&sID=G9sGCjjUWKoe2OpTF2VNP9bqOc60JuXwMkz+AvRh5JuiN86omg1O0/0dNqj2SiaE"

def save(ps, n, d, i):
	ID = 0
	for p in ps:
		folder = 'D://other/test2/{}/{}/{}/'.format(d, n, i)
		filename = '{}.jpg'.format(ID)
		os.makedirs(os.path.dirname(folder), exist_ok=True)
		pprint("Saving to " + folder + filename)
		urllib.request.urlretrieve(p, folder + filename)
		ID += 1

def get_id(data, name, district, interval, place_id):
	ID = 0
	for place in data["places"]:
		if place["name"] == name and place["district"] == district and place["interval"] == interval:
			if place["id"] == place_id:
				return ID
			ID += 1
	return 0

conn = http.client.HTTPConnection(site)
conn.request("GET", query)
r1 = conn.getresponse()
data = json.load(r1)

for place in data["places"]:
	if not 'pictures' in place:
		continue
	name = place["name"]
	district = place["district"]
	interval = place["interval"]
	place_id = place["id"]
	ID = get_id(data, name, district, interval, place_id)
	if ID > 0:
		interval += " " + str(ID + 1)
	pictures = []
	for picture in place["pictures"]:
		ID = picture["id"]
		URL = img + ID + attrib
		pictures.append(URL)
	save(pictures, name, district, interval)