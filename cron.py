import datetime

f = open("./cron.txt", "w")
f.write(f'{datetime.datetime.now()}')
f.close()
