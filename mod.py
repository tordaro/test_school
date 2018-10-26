import numpy as np
import os


def sinc2d(x, y):
    if x == 0.0 and y == 0.0:
        return 1.0
    elif x == 0.0:
        return np.sin(y) / y
    elif y == 0.0:
        return np.sin(x) / x
    else:
        return (np.sin(x) / x) * (np.sin(y) / y)


def mean(num_list):
    for num in num_list:
        if type(num) == complex:
            return NotImplemented
    return sum(num_list)/len(num_list)


def fib(n):
    if type(n) == float or n < 0:
        return NotImplemented
    elif n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def std(vals):
    # a little better
    if len(vals) == 0:      # Special case the empty list.
        return 0.0
    mean = sum(vals)/len(vals)
    dev = [(num - mean)**2/len(vals) for num in vals]
    return np.sqrt(sum(dev))


def f():
    files = os.listdir('.')
    if 'no.txt' not in files:
        with open('yes.txt', 'w') as fhandle:
            fhandle.write(42)
