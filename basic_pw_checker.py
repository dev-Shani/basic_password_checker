user_password = "PW1243"
incorrect_password_counter = 0
entered_password = input("Please enter your password: ")

while entered_password != user_password:
  if incorrect_password_counter < 4:
    incorrect_password_counter += 1
    entered_password = input(f"Incorrect password. {5 - incorrect_password_counter} tries remaining. Please try again: ")
    if incorrect_password_counter == 3:
      entered_password = input(f"Incorrect password. 1 try remaining. Please try again: ")
      incorrect_password_counter += 1
  else:
    print("Too many incorrect tries. Try again later.")
    break

if entered_password == user_password:
  print("Password accepted.")