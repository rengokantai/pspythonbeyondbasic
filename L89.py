__author__ = 'Hernan Y.Ke'
#an iterator must implement __next__ and __iter__

class ExIterator:
    def __init__(self):
        self.data = [1,2]
        self.index = 0
    def __iter__(self):
        return self

    def  __next__(self):
        if(self.index>=len(self.data)):
            raise StopIteration()

        result = self.data[self.index]
        self.index +=1
        return result
ex= ExIterator()
print(next(ex))
print(next(ex))
print(next(ex))
