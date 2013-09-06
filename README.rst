===========
Wraptor
===========

.. image:: https://github.com/carlsverre/wraptor/raw/master/docs/images/raptor.jpg

Testing
=======

.. image:: https://travis-ci.org/carlsverre/wraptor.png
    :target: https://travis-ci.org/carlsverre/wraptor

Run tests by executing :code:`python setup.py test`.

Decorators
==========

Memoize
-------
Add a cache to a function such that multiple calls with the same args
will return cached results.  Supports an optional cache timeout which
will flush items from the cache after a set interval for
recomputation.

.. code:: python

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

.. code:: python

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

Supports attaching to an instance method!

.. code:: python

    class foo(object):
        @memoize(instance_method=True)
        def bar(self, a, b):
            return random()

    f = foo()
    f2 = foo()

    # they don't share a cache!
    f.bar(1,2) != f2.bar(1,2)

Throttle
--------
Throttle a function to firing at most 1 time per interval.  The function
is fired on the forward edge (meaning it will fire the first time you
call it).

.. code:: python

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

.. code:: python

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

.. code:: python

    @timeout(1)
    def heavy_workload():
        try:
            # simulate heavy work
            time.sleep(10)
        except TimeoutException:
            print('workload timed out')

Context Managers
================

Throttle
--------
Throttle a with statement to executing its body at most 1 time per
interval.  The body is fired on the forward edge (meaning it will
fire the first time you call it).

.. code:: python

    from wraptor.context import throttle
    import time

    throttler = throttle(seconds=3)

    def foo():
        with throttler:
            print 'bar'

    foo()
    # prints bar
    sleep(2)
    foo()
    # does nothing
    sleep(2)
    foo()
    # prints bar

Maybe
-----
Execute a with block based on the results of a predicate.

.. code:: python

    from wraptor.context import maybe

    def foo(cond):
        with maybe(lambda: cond == 5):
            print 'bar'

    foo(5)
    # prints bar
    foo(3)
    # does nothing

Timer
-----
Time a block of code.

.. code:: python

    from wraptor.context import timer

    def foo(cond):
        with timer('my slow method') as t:
            expensive_stuff()
        print t

    foo()
    # prints "my slow method took 435.694 ms"
