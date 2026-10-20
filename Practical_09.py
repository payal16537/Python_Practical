#Write a program to read a file and 
#a.  Print the total number of characters, words and lines in the file. 
#b.  Calculate the frequency of each character in the file. Use a variable of dictionary type to maintain the count. 
#c.  Print the words in reverse order. 
#d.  Copy even lines of the file to a file named ‘File1’ and odd lines to another file named ‘File2’. 


filename = "sample.txt"

# Step 0: Automatically create a sample file for demonstration
with open(filename, "w") as f:
  f.write("Hello world\nThis is a sample file\nPython programming is fun!\n")

# a. Print the total number of characters, words and lines in the file[cite: 1]
chars = 0
words = 0
lines = 0

with open(filename, "r") as f:
  file_content = f.readlines()
  lines = len(file_content)
  for line in file_content:
    chars += len(line)
    words += len(line.split())

print(f"Total lines: {lines}")
print(f"Total words: {words}")
print(f"Total characters: {chars}")

# b. Calculate the frequency of each character in the file using a dictionary[cite: 1]
char_freq = {}
with open(filename, "r") as f:
  text = f.read()
  for ch in text:
    char_freq[ch] = char_freq.get(ch, 0) + 1
print(f"Character frequencies: {char_freq}")

# c. Print the words in reverse order[cite: 1]
print("Words in reverse order:")
all_words = text.split()
for word in reversed(all_words):
  print(word, end=" ")
print("\n")

# d. Copy even lines to 'File1' and odd lines to 'File2'[cite: 1]
with open(filename, "r") as f:
  all_lines = f.readlines()

with open("File1", "w") as f1, open("File2", "w") as f2:
  for idx, line in enumerate(all_lines, start=1):
    if idx % 2 == 0:
      f1.write(line)
    else:
      f2.write(line)

print("Even lines successfully copied to 'File1' and odd lines to 'File2'.")