from __future__ import print_function

import requests

from Parser import Parser

from env import SPREADSHEET_ID, GIDS

# for GID in GIDS:
# 	url = "https://docs.google.com/spreadsheets/d/{0}/export?format=csv&gid={1}".format(SPREADSHEET_ID, GIDS[GID])
# 	r = requests.get(url)



parser = Parser('./edt.csv')
lessons = parser.parse()
for lesson in lessons:
	print(lesson)

# open('./edt.csv', 'wb').write(r.content)