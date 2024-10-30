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

# #Get data from Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

#Create DataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [70, 56, 89]
}

# data2 = pandas.DataFrame(data_dict)
# print(data2)
#data2.to_csv() ->Create a new csv file.

#Use .iterrow() for dictionary comprehension in a dataframe
#{key_expression: value_expression for item in iterable if condition}

student_data_frame = pandas.DataFrame(data_dict)
print(student_data_frame)

#Loop through a data frame
#for (key, value) in student_data_frame.items():
    #print(value)

#Loop through rows of DataFrame
# for (index, row) in student_data_frame.iterrows():
#     if row.students == "Amy":
#         print(row.student)

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
    #Access key and value
    # pass


# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}