mylist=[12,100,87,6,2]

for i in range(0, len(mylist)):
    minElement = 10000000
    minLocation = -1
    for j in range(i,len(mylist)):
        if minElement > mylist[j]:
            minElement=mylist[j]
            minLocation=j
            mylist[i], mylist[j] = mylist[j], mylist[i]
            print(mylist)

