# 15)	WAP to reverse/inverse key:value like below. 
# dict1 = {‘a’: 1, 'b':2}
# Expected result: dict2 = {1: 'a', 2: ‘b’}

dict1 = {'a':1,'b':2}

# Output dict2 = {1:'a',2:'b'}

#print {i+1:j for i,j in enumerate(dict1)}
dict2 = {v: k for k, v in dict1.iteritems()}
print dict2
