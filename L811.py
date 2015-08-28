__author__ = 'Hernan Y.Ke'
#__getitem__()

class AlterIter:
    def __init__(self):
        self.data =[1,2,3]
    def __getitem__(self, item):
        return self.data[item]


print(list(i for i in AlterIter()))