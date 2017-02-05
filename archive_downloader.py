import os
import json
import http.client
from pprint import pprint
import urllib.request

site = "edoclib.gasrb.ru"
img = "http://" + site + "/imgo.jpg?id="
attrib = "&rH=059d0024b12efbc1e9a4faaf21435d6d&sID=G9sGCjjUWKoe2OpTF2VNP9bqOc60JuXwMkz+AvRh5JuiN86omg1O0/0dNqj2SiaE"

def fix_str(n):
	n = n.replace("/","")
	n = n.replace("?","")
	return n

def save_file(p, dir, file):
	pprint("Saving to " + dir + file)
	os.makedirs(os.path.dirname(dir), exist_ok=True)
	urllib.request.urlretrieve(p, dir + file)

def save_note(dir, note):
	note = fix_str(note)
	if (note != ''):
		open(dir + note, 'a').close()

def save(ps, n, d, i, note):
	ID = 0
	nf = fix_str(n)
	folder = 'D://other/test2/{}/{}/{}/'.format(d, nf, i)
	save_note(folder, note)
	for p in ps:
		filename = '{}.jpg'.format(ID)
		save_file(p, folder, filename)
		ID += 1

def get_id(data, name, district, interval, place_id):
	ID = 0
	for place in data["places"]:
		if place["name"] == name and place["district"] == district and place["interval"] == interval:
			if place["id"] == place_id:
				return ID
			ID += 1
	return 0

def start(query):
	conn = http.client.HTTPConnection(site)
	conn.request("GET", query)
	r1 = conn.getresponse()
	data = json.load(r1)

	if not 'places' in data:
		pprint("Skipping this name since it has to places")
		return
	
	for place in data["places"]:
		if not 'pictures' in place:
			pprint("Skipping {} since it has to pictures".format(place))
			continue
		name = place["name"]
		district = place["district"]
		interval = place["interval"]
		place_id = place["id"]
		note = ""
		if 'note' in place:
			note = place["note"]
		ID = get_id(data, name, district, interval, place_id)
		if ID > 0:
			interval += " " + str(ID + 1)
		pictures = []
		for picture in place["pictures"]:
			ID = picture["id"]
			URL = img + ID + attrib
			pictures.append(URL)
		save(pictures, name, district, interval, note)	