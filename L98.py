__author__ = 'Hernan Y.Ke'
class A: pass
class B(A): pass
class C(A): pass
class D(B,A):pass   #must assign subclass first. The following are incorrect: A,B or B,A,C
print(D.__mro__)