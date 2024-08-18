
from datetime import datetime


def calc_age():
    current_year = datetime.now().year
    user_birth_year = int(input("What is your birth year: "))

    current_age = current_year - user_birth_year
    print(current_age)


calc_age()
