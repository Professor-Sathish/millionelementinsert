def insertionsort(alist):
    for i in range(1,len(alist)):
        while i  and alist[i - 1] >alist[i] :
            alist[i - 1], alist[i] = alist[i] , alist[i - 1]
            i -=1
    return alist
print(insertionsort([1]*10000000+[0]))