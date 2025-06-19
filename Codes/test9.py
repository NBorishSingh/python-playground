a=int(input("enter the start of the range: "))
b=int(input("enter the end of the range: "))
print(f"Prime numbers between {a} and {b} are:")
for d in range(a,b+1):
    if d>1:
        isprime=True
        for i in range(2,d):
            if(d%i==0):
                isprime=False
                break
        if isprime:
            print(d, end=' ')   