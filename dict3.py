#handling the missing key in dict
my_dict={
    "name":"max",
    "age":"27",
    "salary":"$246,300",
    "post":"district-judge"
}
key=input("enter the key name: ")
if key in my_dict:
    print("key is found")
else:
    print("key not found!")    