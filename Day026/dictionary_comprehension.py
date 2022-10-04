import random
names = ["Alex" , "Beth" , "Caroline" , "Alisa" , "Taylor" , "Hannah" , "Justin" , "Jessica"]
students_score = {student:random.randint(60,100) for student in names}
print(students_score)

passed_students = {student:score for (student,score) in students_score.items() if score>70}
print(passed_students)


# Exercise 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {item:len(item) for item in sentence.split() }

print(result)

# Exercise 2
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:temp*(9/5)+32 for (day,temp) in weather_c.items() }

print(weather_f)
