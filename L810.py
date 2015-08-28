__author__ = 'Hernan Y.Ke'
class ExIterator:
    def __init__(self,data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self

    def  __next__(self):
        if(self.index>=len(self.data)):
            raise StopIteration()

        result = self.data[self.index]
        self.index +=1
        return result

class ExIteration:
    def __init__(self):
        self.data = [1,2,3]

    def __iter__(self):
        return ExIterator(self.data)

print (list(i for i in ExIteration()))