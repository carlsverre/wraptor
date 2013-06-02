===========
Wraptor
===========

.. image:: https://github.com/carlsverre/wraptor/raw/master/docs/images/raptor.jpg

Decorators
==========

Memoize
-------
Add a cache to a function such that multiple calls with the same args
will return cached results.  Supports an optional cache timeout which
will flush itmes from the cache after a set interval for recomputation.

    from wraptor.decorators import memoize

    @memoize()
    def foo(bar, baz):
        print(bar, baz)

    foo(1, 2)
    # prints (1, 2)
    foo(3, 4)
    # prints (3, 4)
    foo(1, 2)
    # no-op

Supports timeouts!

    @memoize(timeout=.5)
    def foo(bar, baz):
        print(bar, baz)

    foo(1, 2)
    # prints (1, 2)
    foo(1, 2)
    # no-op

    import time
    time.sleep(2)

    foo(1, 2)
    # prints (1, 2)

Throttle
--------
Throttle a function to firing at most 1 time per interval.  The function
is fired on the forward edge (meaning it will fire the first time you
call it).

    from wraptor.decorators import throttle
    import time

    @throttle(.5)
    def foo(bar, baz):
        print(bar, baz)

    foo(1, 2)
    # prints (1, 2)
    foo(3, 4)
    # no-op
    time.sleep(1)
    foo(5, 6)
    # prints (1, 2)

Timeout
-------
Timeout uses signal under the hood to allow you to add timeouts to any
function.  The only caveat is that `signal.alarm` can only be used in the
main thread of execution (so multi-threading programs can't use this
decorator in sub-threads).

The timeout value must be a positive integer.

    from wraptor.decorators import timeout, TimeoutException
    import time

    @timeout(1)
    def heavy_workload():
        # simulate heavy work
        time.sleep(10)

    try:
        heavy_workload()
    except TimeoutException:
        print('workload timed out')

You can also catch the timeout exception from inside the function:

    @timeout(1)
    def heavy_workload():
        try:
            # simulate heavy work
            time.sleep(10)
        except TimeoutException:
            print('workload timed out')
