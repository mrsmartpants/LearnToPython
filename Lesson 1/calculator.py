# Calculator

# Store the user input of 2 numbers and operators
num1, operator, num2 = input('Enter Calculation ').split()
# Convert string to integer
num1 = int(num1)
num2 = int(num2)

if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1+num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "-":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "-":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
else:
    print("Use either +, -, * or /")
# print result

