__author__ = 'Hernan Y.Ke'
import time
#map vs list comprehensions
#Example1
start1 =time.time()
print(list(str(i)for i in range(50)))
end1 = time.time()
print("time1 %r" % (end1-start1))

start2 =time.time()
print(list(map(str,range(50))))
end2 = time.time()
print("time2 %r" % (end2-start2))