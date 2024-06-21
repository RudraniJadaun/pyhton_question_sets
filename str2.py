#lenght of str in 4 ways
#1 way
it_str="hello everyone how are you "
print(len(it_str)," is the length of the string")

# 2way
it_str="hello everyone"
i=0
for x in it_str:
    i+=1
print(i," is the length of the string")

# 3 way
it_str="hello everyone"
count=0
while it_str[count:]:
    count+=1
print(count,"is the length of the string")