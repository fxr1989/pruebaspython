from datetime import date, datetime 

my_time_local = datetime.now()
my_time_utc = datetime.utcnow()
my_time_today = datetime.today()

print(my_time_local)
print(my_time_utc)
print(my_time_today)
print(my_time_today.year)
print(my_time_today.month)
print(my_time_today.day)
print("Formato fecha 1: " + my_time_local.strftime('%d/%m/%y'))
print("Formato fecha 2 iso : " + my_time_local.strftime('%Y%m%d'))
print("Formato fecha 3 : " + my_time_local.strftime('%m-%d-%y'))
print("Formato fecha 4 hora : " + my_time_local.strftime('%H:%m:%S'))
