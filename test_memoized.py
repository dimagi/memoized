import doctest
from itertools import count

from testil import eq

from memoized import memoized


def test_doctests():
    import memoized
    results = doctest.testmod(memoized)
    assert results.failed == 0, results


def test_memoized_function():
    func = make_counter()
    mem_func = memoized(func)

    eq(mem_func(0), 1)  # miss
    eq(func(0), 2)
    eq(func(0), 3)
    eq(mem_func(0), 1)  # hit
    eq(mem_func(1), 5)  # miss


def test_memoized_method():
    sub = Subject()
    eq(sub.mem_func(0), 1)
    eq(sub.func(0), 2)
    eq(sub.func(0), 3)
    eq(sub.mem_func(0), 1)
    eq(sub.mem_func(1), 5)


def test_memoized_class():
    @memoized
    class Class:
        def __init__(self, value=1):
            self.value = value

    assert Class() is Class()
    assert Class() is not Class(0)


def test_memoized_function_get_cache():
    func = make_counter()
    mem_func = memoized(func)

    eq(mem_func(0), 1)
    cache = mem_func.get_cache()
    eq(cache[(0,)], 1)


def test_memoized_method_get_cache():
    sub = Subject()
    eq(sub.mem_func(0), 1)
    cache = sub.mem_func.get_cache(sub)
    eq(cache[(0,)], 1)


def test_memoized_function_name():
    @memoized
    def a_rose(by_any, other_name):
        pass

    eq(a_rose.__name__, "a_rose")


def test_memoized_method_name():
    class Class:
        @memoized
        def a_rose(by_any, other_name):
            pass

    eq(Class.a_rose.__name__, "a_rose")


def test_memoized_class_name():
    @memoized
    class ARose:
        pass

    eq(ARose.__name__, "ARose")


def make_counter():
    """Make a counter function whose result increments on each call

    The returned function takes a single argument, which is added
    to the internal counter before returning the result.
    """
    def func(y):
        return next(numbers) + y
    numbers = count(1)
    return func


class Subject:
    x = 0

    def func(self, y):
        self.x += 1
        return self.x + y

    @memoized
    def mem_func(self, y):
        return self.func(y)
