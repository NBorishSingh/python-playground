# Input string
text = input("Enter a string: ")

# Initialize counters
alphabets = digits = special = 0

# Check each character
for char in text:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits += 1
    else:
        special += 1

# Display output
print("Alphabets:", alphabets)
print("Digits:", digits)
print("Special Characters:", special)
