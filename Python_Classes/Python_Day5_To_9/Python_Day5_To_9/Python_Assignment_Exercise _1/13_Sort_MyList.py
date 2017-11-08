# 13)	WAP to Sort the list using lambda function
# mylist = [["john", 1, "a"], ["larry", 0, "b"]]. Sort the list by second item
# 1 and 0

mylist = [["john", 1, "a"], ["larry", 0, "b"]]
# mylist.sort(key=lambda mylist : mylist[0][1])

mylist.sort(key=lambda x : x[0][1])

# Both above statement will work

print mylist

    
