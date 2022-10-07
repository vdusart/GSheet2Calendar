import shutil
import os
import requests
from ics import Calendar

from Parser import Parser
from models.db import Timetables
from utils.base import Base, Session, engine
from upload import upload_files

Base.metadata.create_all(engine)
session = Session()

folder_name = os.environ.get('ICS_FOLDER_NAME')
shutil.rmtree(f'./{folder_name}/', ignore_errors=True)
os.mkdir(folder_name)

timetables = session.query(Timetables).all()
for timetable in timetables:
    print(f"[+] Getting timetable: {timetable.name}")
    url = f"https://docs.google.com/spreadsheets/d/{timetable.spreadsheet_id}/export?format=csv&gid={timetable.gid}"
    r = requests.get(url)

    parser = Parser(r.content.decode("utf-8"))
    lessons = parser.parse()

    c = Calendar()
    for lesson in lessons:
        c.events.add(lesson.to_ical_event())

    with open(f'./{folder_name}/{timetable.name}.ics'.replace(" ", ""), 'w') as f:
        lines = c.serialize_iter()
        lines = lines[:-1] + ["REFRESH-INTERVAL;VALUE=DURATION:P1H\n"] + lines[-1:]
        f.writelines(lines)
    print(f"[+] Saving calendar in file ./{folder_name}/{timetable.name.replace(' ', '')}.ics")

upload_files()