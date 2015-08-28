__author__ = 'Hernan Y.Ke'
#Example, map multiple lists
ls1=[1,2,3]
ls2=[4,5,6]
ls3=[7,8,9]

def combine(a,b,c):
    return '{}{}{}'.format(a,b,c)

print(list(map(combine,ls1,ls2,ls3)))