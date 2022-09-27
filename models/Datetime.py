class Datetime:

    def __init__(self, date, time):
        self.day, self.month, self.year = date.split("/")
        if time.split("h")[1] != "":
            self.hour, self.minute = time.split("h")
        else:
            self.hour = time[:-1]
            self.minute = "00"

    def to_str(self):
        return f'{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}:00'
