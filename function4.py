# program to get the list of parameters of a function
def func(x, y):
    print(list(locals().keys()))
func(1, 2)