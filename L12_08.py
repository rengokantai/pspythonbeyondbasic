__author__ = 'Hernan Y.Ke'
import contextlib
import sys

@contextlib.contextmanager
def logging_context():
    print('before enter')
    try:
        yield 'in the block'
        print('in enter')
    except Exception:
        print('in error block',sys.exc_info())
    raise

with logging_context() as x:
    raise ValueError('Wrong')