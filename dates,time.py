#DATE AND TIMR
import datetime

date = datetime.date(2026,11,2)
print(f"Sample date is {date}")

today = datetime.date.today()
print(f"Today is {today}")

time = datetime.time(12,30,22)
print(f"Sample time is {time}")
now = datetime.datetime.now()

print(f"the time now is {now}")
print()

#now = now.strftime("%H : %M : %S")
#print(f"TIME : {now}")
print("Month    day     Year    Time ")
now = now.strftime("%m      %d      %Y      %H:%M:%S")
print(now)