import archive_downloader
import codecs
from pprint import pprint
import urllib.request

y0 = "1795"
y1 = "1811"
dist_raw = "Уфимский"
dist = urllib.parse.quote_plus(dist_raw)

fileObj = codecs.open("names.txt", "r", "utf_8_sig")
text = fileObj.read().splitlines() # или читайте по строке
names = []
for tx in text:
	names.extend(tx.split(', '))
fileObj.close()

for name_raw in names:
	name_fix = name_raw[:-2]
	name = urllib.parse.quote_plus(name_fix)
	query = "/?places={}&mode=1&tm=1486276305228&fe=1&_y0={}&_y1={}&_p=&_d={}&_dn=&_n=&pNo=1&cnt=1&pSz=100&rc=4".format(name, y0, y1, dist)
	pprint("Checking {}".format(name_raw))
	archive_downloader.start(query)