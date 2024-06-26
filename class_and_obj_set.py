# class user:
#         print("upper side")
#         x=5
#         print("lower side")

# print(user().x)

# class person:
#     def __init__(self,name,email) -> None:
#         self.name=name
#         self.email=email

# p=person("max","max23@gmail.com")
# print(p.name)
# print(p.email)


class company:
    name="meta"
    product="facebook"

    def func(it):
        print(it.name)
        print(it.product)

a=company()
a.func()

class school:
    def __init__(self,name,stander):
        self.name=name
        self.stander=stander
        print(self.name)
        print(self.stander)

x=school("max",9)

class user1:
    print("hey everyone!")

o=user1()

class unknown_class():
    def __init__(self,n):
        self.n=n
        str1=n.capitalize()
        print(str1)
    x="hello"


obj=unknown_class("hello")
print(obj.x)
b=unknown_class()
print(b.x)

# # del obj.x
# print(obj.x)
# print(b.x)
