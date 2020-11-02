from time import sleep
stored_pass = "password"
password = ""
guesses = 0
pass_mismatch = stored_pass != password

while pass_mismatch:
  guesses = guesses + 1
  if guesses > 3:
    print("Maximum guesses reached. Locked out for 10 minutes")
    sleep(600)
  print("Enter your password:")
  password = input()
  pass_mismatch = stored_pass != password

print("Access granted")