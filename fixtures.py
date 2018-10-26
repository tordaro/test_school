import os
from mod import f


def f_setup(func):
    '''Ensure that neither yes.txt or no.txt exist.'''
    files = os.listdir('.')
    if 'no.txt' in files:
        os.remove('no.txt')
    if 'yes.txt' in files:
        os.remove('yes.txt')


def f_teardown(func):
    '''Removes yes.
    txt if it was created'''
    files = os.listdir('.')
    if 'yes.txt' in files:
        os.remove('yes.txt')


def test_f():
    '''Make sure the filesystem is clean'''
    exp = 42
    f()
    with open('yes.txt', 'r') as fhandle:
        obs = int(fhandle.read())
    assert obs = exp
