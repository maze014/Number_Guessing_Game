from random import randint

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 5 chances to guess the correct number.\n")
print("Please select the difficulty level:")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)\n")

random_number = randint(1, 100)
level = ["Easy", "Medium", "Hard"]
chances = [10, 5, 3]
attemp = 0

choice = input("Enter your choice: ")
print()
choice = int(choice)
print("Great! You have selected the " + level[choice - 1] + " difficulty level.")
print("Let's start the game!\n")

if choice < 1 or choice > 3:
    print("Invalid choice")
else:
    while True:
        if attemp < chances[choice - 1]:
            number = input("Enter your guess: ")
            number = int(number)

            attemp += 1

            if number > random_number:
                print("Incorrect! The number is less than", number)
                print()
            elif number < random_number:
                print("Incorrect! The number is greater than", number)
                print()
            else:
                print("Congratulations! You guessed the correct number in", attemp ,"attempts\n")
                break
        else:
            break