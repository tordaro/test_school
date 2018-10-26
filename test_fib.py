from mod import fib


def test_ints():
    obs = fib(1.0)
    exp = NotImplemented
    assert obs == exp


def test_negative():
    obs = fib(-1)
    exp = NotImplemented
    assert obs == exp


def test_fib0():
    # test edge 0
    obs = fib(0)
    assert obs == 1


def test_fib1():
    # test edge 1
    obs = fib(1)
    assert obs == 1


def test_fib6():
    # test internal point
    obs = fib(5)
    assert obs == 8
