# File operations in Python
# Opening a file
file_path: str = "example.txt"
file = open(file_path, "r")
content = file.read()
file.close()
print(content)

# Writing to a file
file = open(file_path, "w")
file.write("Hello, World!\n")
file.write("This is a test file.\n")
file.close()

# Appending to a file
file = open(file_path, "a")
file.write("This is a new line.\n")
file.close()

# Reading a file line by line
file = open(file_path, "r")
for line in file:
    print(line.strip())
file.close()
