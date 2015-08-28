__author__ = 'Hernan Y.Ke'
from functools import reduce
import operator

#basic
print(reduce(operator.add,[1,2,3]))#6 default=0
print(reduce(operator.mul,[1,2,3]))#6 default=1
#equal to
print(reduce(operator.mul,[1,2,3],1))#6
#Set to 2
print(reduce(operator.mul,[1,2,3],2))#12
#equivalent to
numbers=[1,2,3,4,5]

accumulator = operator.add(numbers[0],numbers[1])
for item in numbers[2:]:
    accumulator = operator.add(accumulator,item)
print(accumulator)