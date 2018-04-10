from datetime import datetime
from datetime import timedelta
from time import sleep

def countdown(eta):
    while eta > timedelta(seconds = 0):
        sleep(1)
        eta = eta - timedelta(seconds = 1)
        print(str(eta), end='\r')

# values taken from user input
pomodoros = 0
pomodoro_time = 25
short_break_time = 5
long_break_time = 15

pomodoro_eta = timedelta(seconds = 60 * pomodoro_time)
short_break_eta = timedelta(seconds = 60 * short_break_time)
long_break_eta = timedelta(seconds = 60 * long_break_time)

target_time = datetime.now() + pomodoro_eta

print('##### POMODORO TIMER #####')
while True:
    for i in range(4):
        print('Counting down...')
        countdown(pomodoro_eta)
        print('Pomodoro!') 
        pomodoros += 1
        if pomodoros == 4:
            #long break
            print('Take a longer break. You deserve it :)')
            countdown(long_break_eta)
            pomodoros = 0
            input('Press [ENTER] to continue.')
        else:
            print('Take a short break!')
            countdown(short_break_eta) 
            input('Press [ENTER] to continue')