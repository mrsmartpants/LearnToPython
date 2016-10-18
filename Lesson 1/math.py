# Ask the user to input 2 values and store them in a variable num1 and num2
num1, num2 = input('Enter 2 numbers: ').split()

# Convert the strings into regular bumber integer
num1 = int(num1)
num2 = int(num2)

# Add two values and store in sum
sum = num1 + num2

# Subtract values and store the sum
diff = num1 - num2

# Multiply
product = num1 * num2

# Divide
quotient = num1 / num2

# Mod
rem = num1 % num2

# print results
print("{} + {} = {}".format(num1,num2,sum))

print("{} - {} = {}".format(num1,num2,diff))

print("{} * {} = {}".format(num1,num2,product))

print("{} / {} = {}".format(num1,num2,quotient))

print("{} % {} = {}".format(num1,num2,rem))


