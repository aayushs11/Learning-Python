import datetime

today= datetime.date.today()

#timedelta:Represents the difference between two dates or times
fifteen_days= datetime.timedelta(days=15)
forward= today + fifteen_days
backward= today + fifteen_days

print(f'Current Date: {today}')
print(f'Date after 15 days: {today}')
print(f'Date 15 days ago: {today}')