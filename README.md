# pspythonbeyondbasic
## 13 Introspection

### 1. Object Types in Depth
```
i=7
type(i)  #class 'int'
repr(int) #class 'int'
type(i) is int #true
type(i)(78) #78
```

```
i.__class__ #int
i.__class__.__class__ #type
i.__class__.__class__.__class__ #type
issubclass(type,object) #True
```


### 2. Introspecting Objects
```
i = 7
dir(i)
getattr(i,'denominator')
a.denominator
```


## 12. Defining Context Managers
### 1 What is a Context Manager
A context-manager ensures that resources are properly and automatically managed.

### 2 The Context Manager Protocol
```
with expression as x:
  body
```
important: the value of ```expression.__enter__``` is bound to x, not the value of expression.



