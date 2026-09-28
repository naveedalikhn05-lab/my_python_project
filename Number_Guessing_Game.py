# import random

# Random Numbers From 1 to 100

# secret_number = random.randint(1,100)
# print(secret_number)


# Enter Your Guess secret_number

# guess = int(input("Enter Your Guess (1 - 100): "))
# print(guess)


# # Compare the Guess Number

# if guess > secret_number:
#     print("Too High!")
# elif guess < secret_number:
#     print("Too Low!")
# else:
#     print("Correct! ")



# Attempt Counter

# attempts = 0
# attempts += 1
# OR 
# attempts = attempts + 1


# Valiidation The Guess 

# if guess < 1 or guess > 100:
#        print("Please Enter Number From 1 To 100")
#        continue



# Play Again Option

#  if play_again != "y":
#         print("Thanks for playing! 👋")
#         break


# Add The into function
# def play_game()


# Last Set Difficulty

#  print("\nChoose difficulty:")
#     print("1. Easy   (1-50)")
#     print("2. Medium (1-100)")
#     print("3. Hard   (1-200)")

#     difficulty = input("Enter your choice (1/2/3): ")

#     if difficulty == "1":
#         max_number = 50
#     elif difficulty == "2":
#         max_number = 100
#     elif difficulty == "3":
#         max_number = 200
#     else:
#         print("Invalid choice. Medium selected.")
#         max_number = 100




# Final Code 
import random


def play_game():

    print("\nChoose difficulty:")
    print("1. Easy   (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard   (1-200)")

    difficulty = input("Enter your choice (1/2/3): ")

    if difficulty == "1":
        max_number = 50
    elif difficulty == "2":
        max_number = 100
    elif difficulty == "3":
        max_number = 200
    else:
        print("Invalid choice. Medium selected.")
        max_number = 100

    secret_number = random.randint(1, max_number)
    attempts = 0

    print(f"\nI'm thinking of a number between 1 and {max_number}.")
    print("Try to guess it!")

    while True:

        guess = int(input(f"Enter your guess (1-{max_number}): "))

        if guess < 1 or guess > max_number:
            print(f"Please enter a number between 1 and {max_number}.")
            continue

        attempts += 1

        if guess > secret_number:
            print("Too high!")
        elif guess < secret_number:
            print("Too low!")
        else:
            print("\nCorrect! 🎉")
            print(f"You found the number in {attempts} attempts!")
            break


print("================================")
print("     NUMBER GUESSING GAME")
print("================================")

while True:

    play_game()

    play_again = input("\nDo you want to play again? (y/n): ").lower()

    if play_again != "y":
        print("\nThanks for playing! 👋")
        break


