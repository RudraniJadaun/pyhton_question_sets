# print even leters of the string
mystr="hello everyone"
a=[]
i=0
for x in mystr:
    l=i%2
    if(l==0):
        a.append(x)
        i+=1
    else:
        i+=1
print(a,"these are the even values")