number = int(input("Enter an integer: "))
if number < 2:
    is_prime = False
else:
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")