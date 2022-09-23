import csv
from models.ParsedLesson import ParsedLesson

class Parser:
	def __init__(self, _fileName):
		self.fileName = _fileName
	
	def parseWeek(self, weekLines):
		dates, content = weekLines
		lessons = []
		try:
			for i in range(len(dates)):
				if (dates[i] == ""):
					continue
				newLesson = self.parseDay(dates[i], content[i])
				lessons.append(newLesson)
		except:
			print("An exception occurred during the parsing process")
		return lessons

	def parseDay(self, date, description):
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
			start_time = hours[0].split("de")[1]
			end_time = hours[1]

		return ParsedLesson(name, day, start_time, end_time, company)

	def parse(self):
		lessons = []
		with open(self.fileName, newline='') as csvfile:
			rows = csv.reader(csvfile, delimiter=',')
			weekLines = []
			for (i, row) in enumerate(rows):
				if all(s == '' for s in row):
					continue
				if (len(weekLines) == 1):
					weekLines.append(row)
					lessons += self.parseWeek(weekLines)
					weekLines = []
				if ("lundi" in row[1]):
					weekLines.append(row)

				if i >= 40: break
		return lessons