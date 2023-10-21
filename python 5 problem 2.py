numbers = []
while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    if user_input == "":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if numbers:
    numbers.sort(reverse=True)
    print("The five greatest numbers in descending order:")
    for i in range(min(5, len(numbers))):
        print(numbers[i])
else:
    print("No valid numbers were entered.")
