from datetime import date

today = date.today()
print("Today's date:", today)

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
print("date and time =", dt_string)

from datetime import datetime

now = datetime.now()

print('now =', now)
