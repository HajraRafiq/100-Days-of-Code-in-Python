def format_name(first_name,last_name):
    formated_fname=first_name.title()
    formated_lname=last_name.title()

    return f"{formated_fname} {formated_lname}"




fname = input("Enter your first name :")
lname = input("Enter your last name :")
print(format_name(fname,lname))

