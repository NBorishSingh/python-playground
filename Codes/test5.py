def largestnumber():
    if ((a>b)and (a>c)):
        print("the largest number is",a)
    elif((b>a)and(b>c)):
        print("the largest number is",b)
    elif((c>a)and(c>b)):
        print("the largest number is",c)
    else:
        print("the numbers are equal")

if __name__ =="__main__":
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=int(input("Enter third number: "))
    largestnumber()