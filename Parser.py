import csv
from models.ParsedLesson import ParsedLesson

class Parser:
	def __init__(self, _csvContent):
		with open(_csvContent, newline='') as csvfile:
			rows = csv.reader(csvfile, delimiter=',')
			linesDuo = []
			for (i, row) in enumerate(rows):
				if all(s == '' for s in row):
					continue
				if (len(linesDuo) == 1):
					linesDuo.append(row)
					self.workWithDuo(linesDuo)
					linesDuo = []
				if ("lundi" in row[1]):
					linesDuo.append(row)

				if i >= 40: break
	
	def workWithDuo(self, linesDuo):
		dates, content = linesDuo
		print("-----------------------\n-----------------------")
		try:
			for i in range(len(dates)):
				if (dates[i] == ""):
					continue
				self.parseCourse(dates[i], content[i])
		except:
			print("An exception occurred")

	def parseCourse(self, date, description):
		print("#######")
		name = ""
		day = date.split(" ")[1]
		start_time = None
		end_time = None
		company = None
		# print(description)
		if "\n" not in description:
			name = description
		else:
			# print(description)
			content = description.split("\n")

			company = content[0]
			name = content[1].split("(")[0]
			hours = content[-1].split("à")
			start_time = hours[0].split("de")[1]
			end_time = hours[1]


		parsedLesson = ParsedLesson(name, day, start_time, end_time, company)
		print(parsedLesson)