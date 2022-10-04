#Opening a file
file = open("my_file.txt")

# Reading the file
contents = file.read()
print(contents)

# Closing the file
file.close()


#Another way to open a file and saving it in variable. 
with open("my_file.txt") as file:
    contents = file.read()
    print(contents) # It will be closed by itself

#Writing in the file and make it writable with changing the mode

# with open("my_file.txt" , mode="w") as file:
#     file.write("I live in Karachi")

# The "a" mode will append the new text in existing text

# with open("my_file.txt" , mode="a") as file:
#     file.write("\nI live in Karachi")

with open ("file2.txt" , mode="w") as file2: #It will create new file if the file doesn't exist
    contents = file2.write("Hello")