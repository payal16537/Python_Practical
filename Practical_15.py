
# Write a program to accept a name from a user. 
# Raise and handle appropriate exception(s) if the text entered by the user contains digits and/or special characters. 

class InvalidNameError(Exception):
  pass


try:
  name = input("Enter a name: ")
  if not all(c.isalpha() or c.isspace() for c in name):
    raise InvalidNameError(
        "Name cannot contain digits or special characters![cite: 1]"
    )
  print(f"Valid name entered: {name}[cite: 1]")
except InvalidNameError as e:
  print(f"Custom Exception Caught: {e}")