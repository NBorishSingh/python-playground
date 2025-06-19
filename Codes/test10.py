a=[]
x=int(input("enter the number of elements in the list: "))
for i in range(x):
    d=int(input("enter the elements in the list: "))
    a.append(int(d))
b=int(input("enter the number you wanna find frequency of: "))
print(a)
count=0
for i in range(len(a)):
    if b==a[i]:
        count += 1
print(f"the frequency of {b} int the list is {count}")