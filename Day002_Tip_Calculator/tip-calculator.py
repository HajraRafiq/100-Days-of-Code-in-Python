number_of_persons= int(input("Enter number of person\n"))
total_amount_to_pay = int(input("Enter the amount of bill\n"))
tip_percent = 12
individual_amount_to_pay = round((total_amount_to_pay / number_of_persons) + ((total_amount_to_pay / number_of_persons)*(12/100)),2)


print (f"Each person needs to pay ${individual_amount_to_pay} ")