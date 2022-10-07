import os
import shutil
from os.path import isfile, join

import requests
from boto.s3.connection import OrdinaryCallingFormat, S3Connection
from boto.s3.key import Key
from ics import Calendar

from Parser import Parser
from models.db import Timetables
from utils.base import Base, Session, engine

api_key = os.environ.get('CELLAR_ADDON_KEY_ID')
secret_key = os.environ.get('CELLAR_ADDON_KEY_SECRET')
host = os.environ.get('CELLAR_ADDON_HOST')

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

cf = OrdinaryCallingFormat()  # Can't use uppercase name
conn = S3Connection(aws_access_key_id=api_key, aws_secret_access_key=secret_key, host=host, calling_format=cf)

bucket = conn.get_bucket(os.environ.get('BUCKET_NAME'))
bucket.set_acl('public-read')

directory = os.environ.get('ICS_FOLDER_NAME')
calendars = [f for f in os.listdir(directory) if isfile(join(directory, f))]

for calendar in calendars:
    key = Key(bucket)
    key.key = calendar
    key.set_contents_from_filename(f'{directory}/{calendar}')
    key.set_acl('public-read')
