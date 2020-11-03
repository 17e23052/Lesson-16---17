#UNFINISHED BROKEN FIZZBUZZ GAME
number = 1
if number % 3 != 0 and number % 5 != 0:
  ans = number
elif number % 3 == 0 and number % 5 != 0:
  ans = "Fizz"
elif number % 3 != 0 and number % 5 == 0:
  ans = "Buzz"
elif number % 3 == 0 and number % 5 == 0:
  ans = "FizzBuzz"

print("Welcome to FizzBuzz! Enter a number, Fizz, Buzz or FizzBuzz.")
guess = input()
number = number + 1
if guess == ans:
  print("Next:")
elif guess != ans:
  print("Incorrect! Game over.")
elif number == 15:
  print("You completed Fizzbuzz! Thanks for playing.")