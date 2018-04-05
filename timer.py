from datetime import datetime
from datetime import timedelta
from time import sleep

# values taken from user input
pomodoros = 0
pomodoro_time = 25
break_time = 5

eta = timedelta(seconds = 60 * pomodoro_time)
target_time = datetime.now() + eta

print("##### POMODORO TIMER #####")
while True:
    if target_time <= datetime.now():
        print("Pomodoro!") 
        pomodoros += 1
        if pomodoros == 4:
            #long break
            print('Take a longer break. You deserve it :)')
            pomodoros = 0
        break
    else:
        sleep(1)
        eta = eta - timedelta(seconds=1)
        print(str(eta), end='\r')

