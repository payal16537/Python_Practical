# Write a program to perform the following operations on a string 
# a. Find the frequency of a character in a string. 
# b. Replace a character by another character in a string. 
# c. Remove the first occurrence of a character from a string. 
# d. Remove all occurrences of a character from a string. 


s = input("Enter a string: ")

# a. Find the frequency of a character
ch = input("Enter character to find frequency: ")
print(f"Frequency of '{ch}': {s.count(ch)}")

# b. Replace a character by another
old_ch = input("Enter character to replace: ")
new_ch = input("Enter replacement character: ")
s_replaced = s.replace(old_ch, new_ch)
print(f"After replacement: {s_replaced}")

# c. Remove the first occurrence of a character
rem_ch = input("Enter character to remove first occurrence: ")
idx = s.find(rem_ch)
if idx != -1:
  s_rem_first = s[:idx] + s[idx + 1 :]
  print(f"After removing first occurrence: {s_rem_first}")
else:
  print("Character not found.")

# d. Remove all occurrences of a character
rem_all_ch = input("Enter character to remove all occurrences: ")
s_rem_all = s.replace(rem_all_ch, "")
print(f"After removing all occurrences: {s_rem_all}")