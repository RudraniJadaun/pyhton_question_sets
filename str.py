#reverse word in the given python string
my_str="such a bright day"
# def ltor():
s = my_str.split()[::-1]
a=[]
for x in s:
    a.append(x)
print(" ".join(a))