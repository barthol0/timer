from datetime import datetime
from datetime import timedelta
from time import sleep

class Timer():
    """A simple timer class"""
    
    def __init__(self):
        pass
    
    def start_timer(self):
        """Starts the timer"""
        self.start = datetime.now()
        return self.start
    
    def stop_timer(self):
        """Stops the timer.  Returns the time elapsed"""
        self.stop = datetime.now()
        return self.stop - self.start
    
    def now(self):
        """Returns the current time"""
        return datetime.now()
    
    def elapsed(self):
        """Time elapsed since start was called"""
        return datetime.now() - self.start


# values taken from user input
pomodoros = 0
pomodoro_time = 25
break_time = 5

eta = timedelta(seconds = 60 * pomodoro_time)
target_time = datetime.now() + eta

while True:
    if target_time <= datetime.now():
        print("Pomodoro!") 
        break
    else:
        sleep(1)
        eta = eta - timedelta(seconds=1)
        print(str(eta), end='\r')

