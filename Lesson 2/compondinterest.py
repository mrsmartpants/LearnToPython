# Have a user enter their investment amount and expected interest
amt = float(input("Enter the investment amount "))

rate = float(input("Enter the interest rate "))
# Each year their investment will increase by their investment + their investment
for i in range (1 , 10):
    amt = amt + (amt*rate/100)
    print("Amount at end of year {} is {:.2f}".format(i,amt))

# print out the earning after a 10 year period

# Ask for the money invested + the interest rate

# Convert the value to a float

# Convert value to a float and round the percentage rate by 2 digits
