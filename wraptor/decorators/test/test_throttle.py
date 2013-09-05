import time

from wraptor.decorators import throttle

def test_basic():
    arr = []

    @throttle(.1)
    def test():
        arr.append(1)

    test()
    test()
    time.sleep(.2)
    test()

    assert arr == [1, 1]
