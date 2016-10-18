# We'll provide output based on age

# Receive age and store age

age = input('Enter your age: ')

age = int(age)

if (age >= 1) and (age <= 18):
    print("Important Birthday")

elif(age >= 21) and (age <= 50):
    print("Cool Birthday")

elif not(age < 65):
    print("ok Birthday")

else:
    print("Sorry, not important")