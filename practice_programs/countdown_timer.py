import time


my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1): # countdown from my_time to 1
    seconds = x % 60 # calculate seconds. The remainder when divided by 60
    minutes = int(x/60) % 60 # calculate minutes. Divide by 60 and take the remainder when divided by 60
    hours = int(x/3600) # calculate hours. Divide by 3600
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1) # wait for 1 second

print("TIME'S UP!")
