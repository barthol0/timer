from datetime import datetime
from datetime import timedelta
from time import sleep

def countdown(eta):
    while eta > timedelta(seconds = 0):
        sleep(1)
        eta = eta - timedelta(seconds = 1)
        print(str(eta), end='\r')

pomodoro_time = 25
short_break_time = 5
long_break_time = 15

#testing values
# pomodoro_time = 0.1
# short_break_time = 0.1
# long_break_time = 0.1

pomodoro_eta = timedelta(seconds = 60 * pomodoro_time)
short_break_eta = timedelta(seconds = 60 * short_break_time)
long_break_eta = timedelta(seconds = 60 * long_break_time)

target_time = datetime.now() + pomodoro_eta

print('##### POMODORO TIMER #####')
while True:
    for i in range(4):
        print('Counting down...')
        countdown(pomodoro_eta)
        print('Take a short break!')
        countdown(short_break_eta) 
        input('Press [ENTER] to continue')
    print('Take a longer break. You deserve it :)')
    countdown(long_break_eta)
    input('Press [ENTER] to continue.')