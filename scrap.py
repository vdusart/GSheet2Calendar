from env import SPREADSHEET_ID, GIDS
from ics import Calendar
from Parser import Parser
import requests

for GID in GIDS:
    url = "https://docs.google.com/spreadsheets/d/{0}/export?format=csv&gid={1}".format(SPREADSHEET_ID, GIDS[GID])
    r = requests.get(url)

    parser = Parser(r.content.decode("utf-8"))
    lessons = parser.parse()

    c = Calendar()
    for lesson in lessons:
        c.events.add(lesson.to_ical_event())

    with open(f'{GID}.ics'.replace(" ", ""), 'w') as f:
        lines = c.serialize_iter()
        lines = lines[:-2] + ["REFRESH-INTERVAL;VALUE=DURATION:P1H\n"] + lines[-1:]
        f.writelines(lines)
