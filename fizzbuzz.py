
def fizzbuzz(): # If else condition 
    for i in range(1, 50):
        if i % 3 == 0 and i % 5 ==0:
            print(f"FizzBuzz")
        elif i % 3 == 0:
            print(f"Fizz")
        elif i % 5 == 0:
            print(f"Buzz")
        else:
            print(f"{i}")
        


def fizzbuzz(): # For loop with if conditions
    for i in range(1, 50):
        result = ""
        if i % 3 == 0:
            result += "Fizz"
        if i % 5 == 0:
            result += "Buzz"
        print(result or i)




def fizzbuzz(): # List comprehension
    results = [
        "Fizz" * (i % 3 == 0) + "Buzz" * ( i % 5 == 0) or i 
        for i in range(1, 50)
    ]

    for results in results:
        print(results)

fizzbuzz()