import requests

from Parser import Parser

from env import SPREADSHEET_ID, GIDS
from models.Datetime import Datetime

# for GID in GIDS:
# 	url = "https://docs.google.com/spreadsheets/d/{0}/export?format=csv&gid={1}".format(SPREADSHEET_ID, GIDS[GID])
# 	r = requests.get(url)



parser = Parser('./edt.csv')
lessons = parser.parse()
for lesson in lessons:
	print(lesson)

from models.ParsedLesson import ParsedLesson
from ics import Event, Calendar

lesson = ParsedLesson("RE", "10/09/2022", "05h20", "16h29")
print(lesson)

event = lesson.to_ical_event()
print(event.serialize())
# open('./edt.csv', 'wb').write(r.content)
c = Calendar()
c.events.add(event)

with open('groupeA.ics', 'w') as f:
    f.writelines(c.serialize_iter())