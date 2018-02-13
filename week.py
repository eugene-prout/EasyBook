import datetime

today = datetime.datetime.strptime('11/02/2018', '%d/%m/%Y').date()
day = today.weekday()

start = today - datetime.timedelta(days=day)

print(start)
