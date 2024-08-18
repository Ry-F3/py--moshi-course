from decimal import Decimal


def conversion():
    user_pounds = Decimal(input("What is your weight in pounds?: "))
    kg = Decimal(0.453592)
    pound_to_kg = user_pounds * kg

    print(f"{pound_to_kg:.2f}")


conversion()
