# Sample list
numbers = [2, 3, 2, 5, 3, 2, 4, 5, 5, 3]

# Create an empty dictionary to store frequency
frequency = {}

# Count frequency
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Print the result
for key, value in frequency.items():
    print(f"{key} appears {value} times")
