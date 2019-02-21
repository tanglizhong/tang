import random as r
list =[]
while True:
    if len(list) <6:
        a=r.randint(1,49)
        if a not in list:
               list.append(a)
    else:
        break
while True:
    if len(list)<7:
        b=r.randint(1,10)
        if b not in list:
            list.append(b)
    else:
        break

list1=[str(x) for x in list]
print " ".join(list1)


