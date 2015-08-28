__author__ = 'Hernan Y.Ke'
import unittest
from collections.abc import (Container, Sized, Iterable, Sequence)  #Parentheses)
from L101 import SortedSet

class TestConst(unittest.TestCase):
    def test_empty(self):
        s = SortedSet([])

    def test_from_seq(self):
        s = SortedSet([5,7])

    def test_dup(self):
        s = SortedSet([7,7])

    def test_from_iter(self):
        def gen67():
            yield 6
            yield 7
        g =gen67()
        s=sorted(g)

    def test_deff(self):
        s = SortedSet()


class TestContainer(unittest.TestCase):

    def setUp(self):
        self.s = SortedSet([4,3,5,9,7,6])
    def test_posi_conta(self):
        self.assertTrue(6 in self.s)
    def test_neg_conta(self):
        self.assertTrue(2 not in self.s)


class TestSize(unittest.TestCase):
    def test_empty(self):
        s=SortedSet
        self.assertEqual(len(s),0)

    def test_empty(self):
        s=SortedSet([3,3,3])
        self.assertEqual(len(s),1)

class TestIter(unittest.TestCase):
    def setUp(self):
        self.s=SortedSet([1,2])


    def test_iter(self):
        i = iter(self.s)
        self.assertEqual(next(i),1)
        self.assertEqual(next(i),2)
        self.assertRaises(StopIteration, lambda :next(i))  #Syntax

    def test_indx(self):
        index = 0
        expected =[1,2,5]
        for item in self.s:
            self.assertEqual(item,expected[index])
            index+=1

class TestSeq(unittest.TestCase):
    def setUp(self):
        self.s=SortedSet([1,2])

    def test_index(self):
        self.assertEqual(self.s[0],1)
    def test_arise(self):
        with self.assertRaises(IndexError):
            self.s[3]       # Because only 2 elems exist, hence it raises error. Syntax!


    def test_slice(self):
         self.assertEqual(self.s[:1],SortedSet([1]))

    def test_index_positive(self):
        s = SortedSet([1,3,8,9])
        self.assertEqual(s.index(1),0)

    def test_index_positive_err(self):
        s = SortedSet([1,3,8,9])
        with self.assertRaises(ValueError):
            s.index(2)

    def test_reversed(self):
        s =SortedSet([1,3])
        r=reversed(s)
        self.assertEqual(next(r),3)
        self.assertEqual(next(r),1)
        with self.assertRaises(StopIteration):
            next(r)

    def test_count_one(self):
        s = SortedSet([1,3])
        self.assertEqual(s.count(1),1)


class TestRepr(unittest.TestCase):
    def test_repr_empy(self):
        s = SortedSet()
        self.assertEqual(repr(s),"SortedSet()")


class TestEq(unittest.TestCase):
    def test_eq(self):
        self.assertTrue(SortedSet([1,2])==SortedSet([1,2]))
    def test_idential(self):
        s=SortedSet([1,2])
        self.assertTrue(s==s)

    def test_not_idential(self):
        s=SortedSet([1,2])
        self.assertFalse(s!=s)


if __name__ == '__main__':
    unittest.main()