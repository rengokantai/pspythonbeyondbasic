__author__ = 'Hernan Y.Ke'
import datetime
import itertools
import random

class S:
    def __iter__(self):
        return self
    def __next__(self):
        return random.random()# Return 0-1 float

s=S()

timestamps = iter(datetime.datetime.now, None)

for stamp, value in itertools.islice(zip(timestamps,s), 10):
    print(stamp,value)
