__author__ = 'Hernan Y.Ke'
#Must implement this import to use index-related method
from collections import Sequence
from bisect import bisect_left
class SortedSet(Sequence):
    def __init__(self, items=None):
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        #return item in self._items
        try:
            self.index(item)
            return  True
        except ValueError:
            return False

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)
    def __getitem__(self,item):
        result = self._items[item]
        return SortedSet(result) if isinstance(item, slice) else result

    def __repr__(self):
        return "SortedSet({})".format(repr(self._items)if self._items else '')

    def __eq__(self,rhs):
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items ==rhs._items

    def __ne__(self,rhs):
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items !=rhs._items

    def index(self, item):
        index = bisect_left(self._items, item)
        if (index != len(self._items))and(self._items[index]!=item):
            return index
        raise ValueError("{} not found".format(repr(item)))

    def count(self, item):
        return  int(item in self)

#10_13
from random import randrange
s = SortedSet(randrange(100) for _ in range(10) )

print(s)

from timeit import timeit
ti =timeit(setup='from __main__ import s', stmt='[s.count(i) for i in range(10)]', number=100)
print(ti)