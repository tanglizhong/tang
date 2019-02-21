n=int(raw_input("Geben Sie eine Zahl:"))
list=[]
if n==0:
    list.append(0)
    print list
elif n==1:
    list.append(1)
    print list
else:
    for i in range (1,n):
        if n%i==0:
            list.append(i)
            i=i+1
    s=sum(list)
    if s==n:
        print "gleich"
    elif s<n:
        print "kleiner"
    else:
        print "groesser"
    list.append(n)
    print list
    
      

