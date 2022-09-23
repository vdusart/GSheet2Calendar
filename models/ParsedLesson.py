from ics import Event

from models import Datetime

# minuit - 23h59
class ParsedLesson:
    def __init__(self, name: str, day: str, start_time: str = None, end_time: str = None, company: str = None):
        self.name = name.strip()
        self.day = day.strip()
        self.start_time = start_time.strip() if start_time != None else start_time
        self.end_time = end_time.strip() if end_time != None else end_time
        self.company = company.strip() if company != None else company

    def to_ical_event(self):
        e = Event()
        e.name = self.name

    def __str__(self):
        return f'Lesson {self.name} given by {self.company} the {self.day} starts at {self.start_time} and ends at {self.end_time}'
