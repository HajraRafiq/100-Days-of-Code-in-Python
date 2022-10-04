numbers = [1,2,3,4,5]
new_list = [item+1 for item in numbers]  # It will take item from numbers and same it in item variable for new list. After adding 1 in item it will be appended to new list
print(new_list)

name = "Hajra"

name_char = [letter for letter in name]
print(name_char)

num =range(1,5)
double = [numbers*2 for numbers in num]
print(double)


#Conditional List Comprehension4

names = ["Alex" , "Beth" , "Caroline" , "Alisa" , "Taylor" , "Hannah" , "Justin" , "Jessica"]
short_names = [n for n in names if len(n)<5]
print(short_names)

middle_range = [n.upper() for n in names if len(n) >=5]
print(middle_range)


# Filtering Even Numbers
number_list = [ 1,2,3,4,5,6,7,8,9]
even_numbers = [even for even in number_list if even%2 == 0]
print(even_numbers)


# Data Overlap Exercise
file1 = [1,2,3]
file2= [2,3,4]
result =[int(item) for item in file1 if item in file2 ]
print(result)