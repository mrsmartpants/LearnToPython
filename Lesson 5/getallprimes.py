
# Return list

# A prime can only divide 1 and itself

# Receive a request for max prime

# Use for loop to check of mod == 0
def isprime(num):
    for i in range(2,num):
        if (num % i) == 0:
            return False
    return True

def getPrimes(max_num):
    list_of_primes = []

    for num1 in range(2, max_num):
        if isprime(num1):
            list_of_primes.append(num1)
    return list_of_primes

max_num_to_check = int(input("Search for prime up to: "))

list_of_primes = getPrimes(max_num_to_check)

for prime in list_of_primes:
    print(prime)