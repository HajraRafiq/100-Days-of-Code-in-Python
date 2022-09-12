total = 0
for num in range (1,101):
    total = total + num
print(total)


# adding even numbers

add_even = 0
for even in range(0,101,2):
    add_even = add_even + even
print(add_even)


# fizz buzz exercise
for num in range (1,101,1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)