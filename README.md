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




