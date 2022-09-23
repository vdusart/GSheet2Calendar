import datetime


class Datetime:

    def __init__(self, year, month, day, hour=None, minute=None):
        self.dt = datetime.datetime(year, month, day)
        if hour is not None:
            self.dt += datetime.timedelta(hours=hour)
        if minute is not None:
            self.dt += datetime.timedelta(minutes=minute)

    def __str__(self):
        return f'[{self.dt.strftime("%x@%X")}]'
