# for number in range(1,101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

for number in range(1, 101):
    # Create two empty variables for fizz and buzz strings. Each iteration will reset this variables with empty strings
    fizz = ""
    buzz = ""
    # Check if number divisible by 3 or 5. If does then redefine the fizz and buzz variables. Don't use the elif here.
    if number % 3 == 0:
        fizz = "Fizz"
    if number % 5 == 0:
        buzz = "Buzz"

    # Check if variables are not empty or check this way: fizz != "" or buzz != "". If not then use the f string or + sign to concatenate.
    if fizz or buzz:
        number = f"{fizz}{buzz}"

    print(number)