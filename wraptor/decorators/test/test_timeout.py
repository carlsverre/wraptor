import time

from wraptor.decorators import timeout, TimeoutException

def test_basic():
    @timeout(1)
    def fn():
        try:
            time.sleep(2)
            assert False
        except TimeoutException:
            pass
    fn()

def test_cancels_signal():
    @timeout(1)
    def fn():
        pass
    fn()
    time.sleep(1)
