def is_palindrome(a):
    a=a.lower()
    a=a.replace(" ","")
    return a == a[::-1]
if __name__=="__main__":
    a = input("Enter a string: ")
    if is_palindrome(a):
        print("it's a palindrome")
    else:
        print("it's not a palindrome")