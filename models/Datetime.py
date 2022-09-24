import datetime


class Datetime:

    def __init__(self, date, time=None):
        day, month, year = [int(el) for el in date.split("/")]
        if time.split("h")[1] != "":
            hour, minute = [int(el) for el in time.split("h")]
        else:
            hour = int(time[:-1])
            minute = None
        self.dt = datetime.datetime(year, month, day)
        if hour is not None:
            self.dt += datetime.timedelta(hours=hour)
        if minute is not None:
            self.dt += datetime.timedelta(minutes=minute)

    def __str__(self):
        return f'[{self.dt.strftime("%x@%X")}]'
