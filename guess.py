import random

# user_name = input("What is your name? ")

# print(f"Hi there {user_name} welcome to python!")


def guessing_game():
    active = True
    guess_name = ["Rhys", "Ryan", "Phill", "Jade", "Thelma", "Victoria"]
    msg = "Hi I will try to guess your name!"
    while active:
        try:
            print(msg)
            guess = random.choice(guess_name)
            answer = input(f"Is your name {guess}. [y/n]: ").lower()
            if answer == "y":
                print(f"Hello there {guess}, it's nice to virtually meet you!")
                active = False
            elif answer == 'n':
                active = True
                print("You are an enigma I will guess again")
                msg = "Lets go again, I will try to guess your name!"
            else:
                print("Please enter keys [y/n]: ")
        except Exception as e:
            print(f"An error occured: {e}")


guessing_game()
