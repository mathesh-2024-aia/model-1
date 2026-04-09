# Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

print()  # space

# Binary addition
a = input("Enter first binary number: ")
b = input("Enter second binary number: ")

# Convert and add
sum_decimal = int(a, 2) + int(b, 2)

# Convert back to binary
result = bin(sum_decimal)[2:]
 
print("Binary sum:", result)
