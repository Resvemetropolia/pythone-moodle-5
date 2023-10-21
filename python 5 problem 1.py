num_dice = int(input("Enter the number of dice to roll: "))
total = 0
for _ in range(num_dice):
    roll = random.randint(1, 6)
    total += roll
print(f"Sum of the dice rolls: {total}")