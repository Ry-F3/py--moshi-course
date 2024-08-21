import random

# user_name = input("What is your name? ")

# print(f"Hi there {user_name} welcome to python!")


# def guessing_game():
#     active = True
#     guess_name = ["Rhys", "Ryan", "Phill", "Jade", "Thelma", "Victoria"]
#     msg = "Hi I will try to guess your name!"
#     while active:
#         try:
#             print(msg)
#             guess = random.choice(guess_name)
#             answer = input(f"Is your name {guess}. [y/n]: ").lower()
#             if answer == "y":
#                 print(f"Hello there {guess}, it's nice to virtually meet you!")
#                 active = False
#             elif answer == 'n':
#                 active = True
#                 print("You are an enigma I will guess again")
#                 msg = "Lets go again, I will try to guess your name!"
#             else:
#                 print("Please enter keys [y/n]: ")
#         except Exception as e:
#             print(f"An error occured: {e}")


def guessing_game():
    number = random.randint(1,9)
    attempts = 0
    guess_limit = 3

    while attempts < guess_limit:
        try:
            guess = int(input("Guess the number I am thinking of between 1-9: "))

            if guess < 1 or guess > 9:
                print("Please enter a valid number between 1-9.")
            elif guess == number:
                print(f"Well done! The number {number} is correct. You Win!")
                return
            else:
                print("Incorect. Guess again.")
                attempts += 1
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Sorry you have used all of your attempts. The correct number is {number}")
            
        
guessing_game()
