# import csv
#
# with open("weather_data.csv") as raw_data:
#     data = csv.reader(raw_data)
#     temperature = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
# print(temperature)

import pandas
data = pandas.read_csv("weather_data.csv")

#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #Get data from columns
# print(data["condition"]) #More of a Key
# print(data.condition) #More of an Object

#Get data from Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])