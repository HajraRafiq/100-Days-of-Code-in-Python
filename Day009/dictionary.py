programming_words = {
    "Bug" : "An error in a program that prevents from running as expected",
    "Function" : "A piece of code that can easily be called over and over again",
    "Loop" : "The action of doing something over and over again"
}

print(programming_words["Bug"])

#adding new item to dictionary

programming_words["List"]= "A data structure to store multiple items in a single variable"
print(programming_words["List"])

#wipe an existing dictionary

# programming_words = {}

#Loop through a dictionary

for key in programming_words:
    print(key)
    print(programming_words[key])