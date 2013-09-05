from functools import wraps
import time
from hashlib import md5
import threading

class memoize(object):
    """ Memoize the results of a function.  Supports an optional timeout
        for automatic cache expiration.

        If the optional manual_flush argument is True, a function called
        "flush_cache" will be added to the wrapped function.  When
        called, it will remove all the timed out values from the cache.

        This decorator is thread safe.
    """
    def __init__(self, timeout=None, manual_flush=False):
        self.timeout = timeout
        self.cache = {}
        self.manual_flush = manual_flush
        self.cache_lock = threading.RLock()

    def __call__(self, fn):
        def flush_cache():
            with self.cache_lock:
                for key in self.cache.keys():
                    if (time.time() - self.cache[key][1]) > self.timeout:
                        del(self.cache[key])

        @wraps(fn)
        def wrapped(*args, **kwargs):
            kw = kwargs.items()
            kw.sort()
            key_str = repr((args, kw))
            key = md5(key_str).hexdigest()

            with self.cache_lock:
                try:
                    result, cache_time = self.cache[key]
                    if self.timeout is not None and (time.time() - cache_time) > self.timeout:
                        raise KeyError
                except KeyError:
                    result, _ = self.cache[key] = (fn(*args, **kwargs), time.time())

            if not self.manual_flush and self.timeout is not None:
                flush_cache()

            return result

        if self.manual_flush:
            wrapped.flush_cache = flush_cache

        return wrapped
