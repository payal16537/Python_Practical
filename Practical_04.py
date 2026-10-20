# Write a program that accepts a character and performs the following: 
# a.print whether the character is a letter or numeric digit or a special character.
# b. if the character is a letter, print whether the letter is uppercase or lowercase 
# c. if the character is a numeric digit, prints its name in text (e.g., if input is 9, output is NINE)

 
char = input("Enter a single character: ")

if len(char) == 1:
  # a. Check if letter, numeric digit, or special character
  if char.isalpha():
    print(f"'{char}' is a letter.")
    # b. Check uppercase or lowercase
    if char.isupper():
      print("It is uppercase.")
    else:
      print("It is lowercase.")
  elif char.isdigit():
    print(f"'{char}' is a numeric digit.")
    # c. Print name in text
    digits_text = {
        "0": "ZERO",
        "1": "ONE",
        "2": "TWO",
        "3": "THREE",
        "4": "FOUR",
        "5": "FIVE",
        "6": "SIX",
        "7": "SEVEN",
        "8": "EIGHT",
        "9": "NINE",
    }
    print(f"Output: {digits_text.get(char, '')}")
  else:
    print(f"'{char}' is a special character.")
else:
  print("Please enter exactly one character.")