#Write a function that accepts two strings and returns the indices of all the occurrences of the second string in the first string as a list.
# If the second string is not present in the first string then it should return -1. 

def find_indices(s1, s2):
  indices = []
  if s2 not in s1:
    return -1
  start = 0
  while True:
    idx = s1.find(s2, start)
    if idx == -1:
      break
    indices.append(idx)
    start = idx + 1
  return indices


string1 = input("Enter main string: ")
string2 = input("Enter substring to search: ")
result = find_indices(string1, string2)
print(f"Indices: {result}[cite: 1]")