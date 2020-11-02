for number in range(1,16):

  if number <= 15 and number % 3 != 0 and number % 5 != 0:
    print(number)
  if number % 3 == 0 and number % 5 != 0:
    print("Fizz")
  if number % 3 != 0 and number % 5 == 0:
    print("Buzz")
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")