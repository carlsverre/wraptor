from functools import wraps
from wraptor import context

class throttle(object):
    """ Throttle a function to execute at most 1 time per <seconds> seconds
        The function is executed on the forward edge.
    """
    def __init__(self, seconds=1):
        self.throttler = context.throttle(seconds=seconds)

    def __call__(self, fn):
        @wraps(fn)
        def wrapped(*args, **kwargs):
            with self.throttler:
                return fn(*args, **kwargs)
        return wrapped
