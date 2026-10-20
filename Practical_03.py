# Write a program to create a pyramid of character '*' and a reverse pyramid 
def print_pyramid(n):
    print("--- Standard Pyramid ---")
    for i in range(n):
        # Print leading spaces for alignment
        spaces = " " * (n - i - 1)
        # Print the asterisks (odd number per row: 1, 3, 5, etc.)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)

def print_reverse_pyramid(n):
    print("\n--- Reverse Pyramid ---")
    for i in range(n - 1, -1, -1 ):
        # Print leading spaces for alignment
        spaces = " " * (n - i - 1)
        # Print the asterisks in decreasing order
        stars = "*" * (2 * i + 1)
        print(spaces + stars)

# Set the number of rows for the pyramids
rows = 5
print_pyramid(rows)
print_reverse_pyramid(rows)
