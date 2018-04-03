from datetime import datetime

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
        return str(self.stop - self.start)
    
    def now(self):
        """Returns the current time with a message"""
        return str(datetime.now())
    
    def elapsed(self):
        """Time elapsed since start was called"""
        return str(datetime.now() - self.start)
