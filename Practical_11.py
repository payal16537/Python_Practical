# Consider a tuple t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10). Write a program to perform following operations: 
# a. Print half the values of the tuple in one line and the other half in the next line. 
# b. Print another tuple whose values are even numbers in the given tuple. 
# c. Concatenate a tuple t2=(11,13,15) with t1. 
# d. Return maximum and minimum value from this tuple 


t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# a. Print half the values in one line and the other half in the next line
mid = len(t1) // 2
print(*(t1[:mid]))
print(*(t1[mid:]))

# b. Print another tuple whose values are even numbers in the given tuple
even_tuple = tuple(x for x in t1 if x % 2 == 0)
print(f"Even numbers tuple: {even_tuple}[cite: 1]")

# c. Concatenate tuple t2=(11, 13, 15) with t1
t2 = (11, 13, 15)
t_concat = t1 + t2
print(f"Concatenated tuple: {t_concat}[cite: 1]")

# d. Return maximum and minimum value from this tuple
print(f"Maximum: {max(t1)}, Minimum: {min(t1)}[cite: 1]")
