import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(black_squirrels)
print(gray_squirrels)
print(red_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")