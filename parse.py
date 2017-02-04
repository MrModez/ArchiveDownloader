import os
import json
from pprint import pprint
import urllib.request

with open('places.json') as data_file:    
    data = json.load(data_file)

attrib = "&rH=059d0024b12efbc1e9a4faaf21435d6d&sID=G9sGCjjUWKoe2OpTF2VNP9bqOc60JuXwMkz+AvRh5JuiN86omg1O0/0dNqj2SiaE"
img = "http://edoclib.gasrb.ru/imgo.jpg?id="

def save(ps, d, i):
	ID = 0
	for p in ps:
		folder = 'D://other/test2/{}/{}/'.format(d, i)
		filename = '{}.jpg'.format(ID)
		os.makedirs(os.path.dirname(folder), exist_ok=True)
		pprint("Saving to " + folder + filename)
		urllib.request.urlretrieve(p, folder + filename)
		ID += 1

def get_id(data, district, interval, place_id):
	ID = 0
	for place in data["places"]:
		if place["district"] == district and place["interval"] == interval:
			if place["id"] == place_id:
				return ID
			ID += 1
	return 0

for place in data["places"]:
	if not 'pictures' in place:
		continue
	district = place["district"]
	interval = place["interval"]
	place_id = place["id"]
	ID = get_id(data, district, interval, place_id)
	if ID > 0:
		interval += " " + str(ID + 1)
	pictures = []
	for picture in place["pictures"]:
		ID = picture["id"]
		URL = img + ID + attrib
		pictures.append(URL)
	save(pictures, district, interval)