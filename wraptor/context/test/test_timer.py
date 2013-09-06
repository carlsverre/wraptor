from wraptor.context import timer
import time

def test_basic():
    with timer() as t:
        time.sleep(0.1000000)     # sleep 100 ms

    # allow for 2 ms of fudge room
    assert t.interval <= 102

def test_params():
    with timer('test') as t:
        pass

    assert t.name == 'test'
    assert str(t).startswith('test')
