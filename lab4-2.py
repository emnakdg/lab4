x = float(input("Enter the base (X): "))
y = int(input("Enter the exponent (Y): "))

result = 1
for _ in range(y):
    result *= x

print("Result:", result)
