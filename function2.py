#program to find the power of a number by recursion

def num_power(num,power):
    if(power==2):
        x=num*num
        print("the number is",num,"\nand the power is '2' \nso thevalue is:",x)
    elif(power==3):
        y=num*num*num
        print("the number is",num,"\nand the power is '3' \nso the value is:",y)
    else:
        print("something is wrong please try again")

num_power(2,"3")