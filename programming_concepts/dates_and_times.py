# introduction to dates and times in python 

import datetime 

date = datetime.date(2025, 12, 2)                    # year, month, day  
today = datetime.date.today()                        # todays date 
time = datetime.time(12,30,0)                        # hours, minutes, seconds 
now = datetime.datetime.now()                        # returns todays date and the time now 

now = now.strftime("%H:%M:%S %d-%m-%Y")              # hour, minute, second, d, month, year 


target_datetime = datetime.datetime(2020,1,2,12,30,1) 
current_datetime = datetime.datetime.now() 

if target_datetime < current_datetime: 
    print("Target date has passed") 
else: 
    print("Target date has not passed") 


