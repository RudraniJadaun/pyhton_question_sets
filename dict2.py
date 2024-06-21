#python program to find the size of a dictionary
a_dict={
    "a":1,
    "b":2,
    "c":3
}
x=a_dict.__sizeof__()
print(x,"byte is the size of this dict")