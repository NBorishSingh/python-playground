start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):  # check from 2 up to num-1
            if num % i == 1:
                is_prime = False
                break
            else:
                is_prime = True
            if is_prime:
                print(f"{num}", end=" ")