#Write a program to create a list of the cubes of only the even integers appearing in the input list (may have elements of other types also) using the following:
# a. 'for' loop 
# b. list comprehension 

input_list = [1, "hello", 2, 3, 4, 5.5, 6]

# a. Using 'for' loop
cubes_for = []
for item in input_list:
  if isinstance(item, int) and not isinstance(item, bool) and item % 2 == 0:
    cubes_for.append(item**3)
print(f"Cubes using 'for' loop: {cubes_for}[cite: 1]")

# b. Using list comprehension
cubes_comp = [
    item**3
    for item in input_list
    if isinstance(item, int) and not isinstance(item, bool) and item % 2 == 0
]
print(f"Cubes using list comprehension: {cubes_comp}[cite: 1]")