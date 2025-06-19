a=[1,2,3,2,1]
b=[1,"abc","abc",1]
c=a.copy()
c.reverse()
d=b.copy()
d.reverse() 
print(a ,'\n',b ,'\n',c,'\n',d)
if a==c:
    print("a is a palindrome")
if b==d:
    print("b is a palindrome")
else:
    print("they are not palindrome")