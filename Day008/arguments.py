def greet_with(name , location): # name and location are parameters
    print(f"Hey {name}")
    print(f"I live in {location}")

greet_with("Hajra" , "Karachi")  #  Hajra and Karachi are positional arguments

greet_with(location="Australia" , name = "Hajra") # Now it becomes keyword arguments``