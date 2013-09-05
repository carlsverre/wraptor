import time

from wraptor.decorators import memoize

def test_basic_noargs():
    arr = []

    @memoize()
    def fn():
        arr.append(1)

    fn()
    fn()

    assert arr == [1]

def test_basic_args():
    arr = []

    @memoize()
    def fn(*args, **kwargs):
        arr.append(1)

    s_args = [1, 2, 3]
    fn(*s_args)
    fn(*s_args)
    c_args = [[1], "asdjf", {'a': 5}]
    fn(*c_args)
    fn(*c_args)
    kw_args = {'a': 234, 'b': [1, 2, "asdf"], 'c': [5, 6]}
    kw_args_2 = {'a': 234, 'b': [1, 3, "asdf"], 'c': [5, 6]}
    fn(*c_args, **kw_args)
    fn(*c_args, **kw_args_2)
    fn(*c_args, **kw_args)

    fn(fn)
    fn(fn)

    assert arr == [1, 1, 1, 1, 1]

def test_timeout():
    arr = []

    @memoize(timeout=.1)
    def fn(*args, **kwargs):
        arr.append(1)

    fn(1, 2, 3)
    time.sleep(.2)
    fn(1, 2, 3)

    assert arr == [1, 1]

def test_auto_flush():
    memoize_inst = memoize(timeout=.1)

    @memoize_inst
    def fn(*args, **kwargs):
        pass

    fn(1, 2, 3)
    assert len(memoize_inst.cache.keys()) == 1
    time.sleep(.2)
    fn(1, 2, 3)
    assert len(memoize_inst.cache.keys()) == 1

def test_manual_flush():
    memoize_inst = memoize(timeout=.1, manual_flush=True)

    @memoize_inst
    def fn(*args, **kwargs):
        pass

    fn(1, 2, 3)
    assert len(memoize_inst.cache.keys()) == 1
    time.sleep(.2)
    fn(3, 4, 5)
    assert len(memoize_inst.cache.keys()) == 2
    time.sleep(.2)
    fn.flush_cache()
    assert len(memoize_inst.cache.keys()) == 0
