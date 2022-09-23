from __future__ import print_function

import requests
import csv

from env import SPREADSHEET_ID, GIDS

# for GID in GIDS:
# 	url = "https://docs.google.com/spreadsheets/d/{0}/export?format=csv&gid={1}".format(SPREADSHEET_ID, GIDS[GID])
# 	r = requests.get(url)

with open('./edt.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for (i,row) in enumerate(spamreader):
		if not all(s == '' for s in row):
			print(row)

		if i == 40: break

# open('./edt.csv', 'wb').write(r.content)