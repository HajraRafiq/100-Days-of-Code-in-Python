from statistics import mean
from numpy import average, maximum
import pandas as pd

#Reading CSV file with pandas
data = pd.read_csv("weather_data.csv")

print(type(data))

#Extracting temperature column with pandas
print(data["temp"])
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)


# Finding average 
avg = mean(data["temp"])
print(avg)

# Finding average another way
avg = average(data["temp"])
print(avg)

# Finding average another way

avg = data["temp"].mean()
print(avg)


# Finding maximum value in temperature column

max = data["temp"].max()
print(max)
#Printing condition column
print(data["condition"])
print(data.condition)

# Extracting a row with particular value
print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
mondays_temp = int(monday["temp"])
in_celsius = mondays_temp * 9/5 +32
print(in_celsius)



# Creating a DATA-FRAME 
data_dict = {
    "Students" : ["Hajra" , "Hadia" , "Ammar"],
    "Age" : [23,18,23],
    "Education" : ["Undergraduate", "Intermediate" , "Undergraduate" ]
}

students_data = pd.DataFrame(data_dict)
print(students_data)
students_data.to_csv("students.csv")
