####### Local scope ######
### variable inside the function can only be accessed inside the function
num = 1
def sum():
    a = 2
    b = 5
    c = a + b
    print(c)

# sum()
#  print(c) it will give error here


# GLOBAL SCOPE
# Variable outside the functions can also be called inside the function and outside the function
num = 1
def sum():
    a = 2
    b = 5
    c = num + a + b
    print(c)

# sum()

def global_func():
    def local_func():
        print('This is local function and can only be called inside the function above')
    local_func()

global_func()
# local_func() # Error will be raised here



# MODIFYING GLOBAL SCOPE #

enemies = 2
def increase_enemies():
    return enemies + 1

enemies = increase_enemies()
print(f"The enemies are {enemies}")

increase_enemies()