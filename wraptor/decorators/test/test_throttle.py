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

    assert arr == [1,1]

def test_called_with_args():
    test_args = [1,2,[1,2,3],{'asdf':5}]
    test_kwargs = {'a': 1, 'b': [1,2,3]}
    @throttle(1)
    def fn(*args, **kwargs):
        assert tuple(test_args) == args
        assert test_kwargs == kwargs

    fn(*test_args, **test_kwargs)
