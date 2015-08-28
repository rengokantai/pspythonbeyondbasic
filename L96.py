__author__ = 'Hernan Y.Ke'
class B1:
    def __init__(self):
        print('B1')

class B2:
    def __init__(self):
        print('B2')

class Sub(B2,B1):
    pass

s=Sub()

print (Sub.__bases__)
print (Sub.__mro__)#return tuple
print (Sub.mro())#return list