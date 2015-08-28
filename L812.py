__author__ = 'Hernan Y.Ke'
#extended iter
import datetime
import time


#Ex1

it = iter(datetime.datetime.now, None)

for i in range(3):
    time.sleep(1)
    print(next(it))

#Ex2

with open('./text.txt','r+') as f:
    for i in iter(lambda: f.readline().strip(), 'END'): #Anoy func
        print(i)