# Class is just a blueprint for creating any object
# We will create our own custom classes

class User:
    pass

user_1 = User() #object from class

#Creating attribute for that class
#Attribute are associated with objects
user_1.id = "001"
user_1.username = "Hajra"
print(user_1.username)


user_2 = User()
user_2.id = "002"
user_2.username = "Hadia"
print(user_2.id)