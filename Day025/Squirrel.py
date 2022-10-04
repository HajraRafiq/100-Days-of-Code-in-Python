import pandas as pd

# DATA ANALYSIS

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
print(gray_squirrels)
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(black_squirrels)
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(red_squirrels)

data_dict = {
    "Fur Color" : ["Gray" , "Black" , "Cinnamon"] ,
    "No_of_Squirrels": [gray_squirrels , black_squirrels ,red_squirrels]
}

df = pd.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")