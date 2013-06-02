from functools import wraps
import time

class throttle():
    """ Throttle a function to execute at most 1 time per <seconds> seconds
        The function is executed on the forward edge.
    """
    def __init__(self, seconds=1):
        self.seconds = seconds
        self.last_run = 0

    def __call__(self, fn):
        @wraps(fn)
        def wrapped(*args, **kwargs):
            now = time.time()
            if now > self.last_run + self.seconds:
                self.last_run = now
                return fn(*args, **kwargs)
        return wrapped
