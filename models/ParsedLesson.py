from ics import Event

from models import Datetime

# minuit - 23h59
class ParsedLesson:
    def __init__(self, name: str, company: str = None, start_time: Datetime = None, end_time: Datetime = None):
        self.name = name
        self.company = company
        self.start_time = start_time
        self.end_time = end_time

    def to_ical_event(self):
        e = Event()
        e.name = self.name

    def __str__(self):
        return f'Lesson {self.name} given by {self.company} starts at {self.start_time} and ends at {self.end_time}'
