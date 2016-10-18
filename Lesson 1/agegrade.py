# If age is 5 go to kindergarden
# If 6-17 1 to 12

# Ask age
age = eval(input("Enter your age "))

# Handle if age < 5
if age < 5:
    print("Too young for school")

elif age == 5:
    print("Go to Kindergarden")

elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to grade {}".format(grade))
else:
    print("Go to College")
