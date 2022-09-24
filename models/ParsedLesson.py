from datetime import datetime
from ics import Event

from models.Datetime import Datetime

class ParsedLesson:
    def __init__(self, name: str, date: str, start_time: str = None, end_time: str = None, company: str = None):
        self.name = name.strip()
        self.date = date.strip()
        self.start_time = start_time.strip() if start_time != None else start_time
        self.end_time = end_time.strip() if end_time != None else end_time
        self.company = company.strip() if company != None else company

    def to_ical_event(self):
        e = Event()
        e.name = ("[WARNING] " if self.start_time == None or self.end_time == None else "" )+ self.name

        potentialErrors = "Hours unknown\n" if self.start_time == None else ""
        e.description = f'[{self.company if self.company != None else "Unknown"}]\n{potentialErrors}Last update:{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'''

        valid_start_time = self.start_time if self.start_time != None else "00h01"
        valid_end_time = self.end_time if self.end_time != None else "23h59"

        e.begin = Datetime(self.date, valid_start_time).toStr()
        e.end = Datetime(self.date, valid_end_time).toStr()

        return e

    def __str__(self):
        return f'Lesson {self.name} given by {self.company} the {self.date} starts at {self.start_time} and ends at {self.end_time}'
