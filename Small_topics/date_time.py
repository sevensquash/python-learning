from datetime import datetime, date

date1 = date(2026,7,12)
today = date.today() # gives date
now = datetime.now() # gives time
#strftime = stringformattime truns time object into readable format 
now = now.strftime("%m-%d-%Y, %H:%M:%S")
# dates are stored in a structured data
# python first compares year if same compares month if same compares date
target_date = date(2024,7,19)
today_date = date.today()

if target_date < today_date:
    print(today_date)
    print("YEAR already passed")
else:
    print("year hasnt passed.")

print(now)
print(date1)
print(today)
