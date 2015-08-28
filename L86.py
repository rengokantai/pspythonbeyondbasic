__author__ = 'Hernan Y.Ke'

print(list(filter(lambda x:x>0,[1,3,-5,7])))

#If first arg is none,remove all falsy values
print(list(filter(None,[True, False,{},0,[],None,(),(0,),object])))