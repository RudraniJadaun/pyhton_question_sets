# # class user:
# #         print("upper side")
# #         x=5
# #         print("lower side")

# # print(user().x)

# # class person:
# #     def __init__(self,name,email) -> None:
# #         self.name=name
# #         self.email=email

# # p=person("max","max23@gmail.com")
# # print(p.name)
# # print(p.email)


# class company:
#     name="meta"
#     product="facebook"

#     def func(it):
#         print(it.name)
#         print(it.product)

# a=company()
# a.func()

# class school:
#     def __init__(self,name,stander):
#         self.name=name
#         self.stander=stander
#         print(self.name)
#         print(self.stander)

# x=school("max",9)

# class user1:
#     print("hey everyone!")

# o=user1()

# class unknown_class():
#     def __init__(self,n):
#         self.n=n
#         str1=n.capitalize()
#         print(str1)
#     x="hello"


# obj=unknown_class("hello")
# print(obj.x)
# b=unknown_class("why")
# print(b.x)

# # # del obj.x
# # print(obj.x)
# # print(b.x)

# class vehical():
#     def __init__(its,brand,mileage):
#         its.brand=brand
#         its.mileage=mileage
#         print("the brand is :"+brand+"\nthe mileage is:"+mileage)

# y=vehical("honda","12")
# sec_obj=vehical("kn","22")
# del y.mileage
# print(vehical("hi","45"))

# class parent():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print("the name is :",name)
#         print("the age is :",age)

# class child(parent):
#     def __init__(self,name,age,email):
#         print("name is :",name)
#         print("age is :",age)
#         self.email=email
#         print("the email is:",email)
    
# ch1=child("steve","34","steve23@gmail.com")

# class student():
#     def __init__(self,name,stander):
#         self.name=name
#         self.stander=stander

#     def show_student(self):
#         print("the name of the student is :",self.name)
#         print("the class of",self.name,"is:",self.stander)

# collection=student("luke","9")
# collection.show_student()


# lst=["blue","black"]
# class adding_item():
#     def __init__(self,item):
#         self.item=item
    
#     def add_it(a):
#         lst.append(a.item)
#         print("it is:",lst)

# y=adding_item("brown")
# y.add_it()

lst=["blue","black"]
class adding_item():
    def __init__(self,item):
        self.item=item
    
        def add_it(self):
            lst.append(item)
            print("it is:",lst)
        add_it(item)
y=adding_item("white")
# print(y.add_it)
print(y)