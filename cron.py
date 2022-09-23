import datetime

f = open("./cron.txt", "a")
f.write(f'{datetime.datetime.now()}')
f.close()
