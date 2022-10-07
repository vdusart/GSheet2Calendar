import csv
from io import StringIO
from models.ParsedLesson import ParsedLesson


class Parser:
    def __init__(self, _csv_content):
        self.csvContent = StringIO(_csv_content)

    def parse_week(self, week_lines):
        dates, content = week_lines
        lessons = []
        try:
            for i in range(len(dates)):
                if dates[i] == "":
                    continue
                new_lesson = self.parse_day(dates[i], content[i])
                if new_lesson:
                    lessons.append(new_lesson)
        except Exception:
            print("An exception occurred during the parsing process")
        return lessons

    def parse_day(self, date, description):
        if description == "":
            return None
        name = ""
        day = date.split(" ")[1]
        start_time = None
        end_time = None
        company = None
        if "\n" not in description:
            name = description
        else:
            content = description.split("\n")
            company = content[0]
            name = content[1].split("(")[0]
            hours = content[-1].split("à")
            if len(hours) == 2:
                start_time = hours[0].split("de")[1]
                end_time = hours[1]

        return ParsedLesson(name, day, start_time, end_time, company)

    def parse(self):
        lessons = []
        rows = csv.reader(self.csvContent, delimiter=',')
        week_lines = []
        for (i, row) in enumerate(rows):
            if all(s == '' for s in row):
                continue
            if len(week_lines) == 1:
                week_lines.append(row)
                lessons += self.parse_week(week_lines)
                week_lines = []
            if "lundi" in row[1]:
                week_lines.append(row)

        return lessons
