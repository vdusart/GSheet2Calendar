import requests

from Parser import Parser

from env import SPREADSHEET_ID, GIDS
from ics import Calendar


for GID in GIDS:
	url = "https://docs.google.com/spreadsheets/d/{0}/export?format=csv&gid={1}".format(SPREADSHEET_ID, GIDS[GID])
	r = requests.get(url)

	parser = Parser(r.content.decode("utf-8"))
	lessons = parser.parse()

	c = Calendar()
	for lesson in lessons:
		c.events.add(lesson.to_ical_event())

	with open('groupeA.ics', 'w') as f:
		f.writelines(c.serialize_iter())
