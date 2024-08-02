# import csv

# with open(file="weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# the above code used to import the file and separate the data in the list, but it gets too long and complicated to code
# so, pandas was used to work with the data frame tables like google sheets and Excel sheets

import pandas
data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])

# same output, but it occurs within 3 lines by using the pandas














import pandas
data = pandas.read_csv("weather_data.csv")
print(type(data))
# checking the type of the data

# used to create the tabular form to a dictionary
data_dict = data.to_dict()
print(data_dict)

# # without pandas finding the mean value
# data_list = data['temp'].tolist()
# print(int(sum(data_list) / len(data_list)))

# print(data["temp"].mean())
#
# print(data["temp"].max())
#
# print(data["condition"])
# print(data.condition)

# we can use
# data["temp"]
# data.temp
# because the pandas saves the values as attribute, so we can use these two methods

# getting the data in row
# print(data[data.day == "Monday"])

# getting the highest temperature row in the temperature list
# print(data[data.temp == data.temp.max()])


# # getting the values in rows
# monday = data[data.day == "Monday"]
# print(monday)
# print(monday.condition)
#
# temperature = data[data.day == "Monday"]
# print(monday.temp[0] * 9/5 + 32) # 0 is optional
#
#

# # create a data frame from scratch
data_dict = {
    "students": ["sugan", "harshini", "james"],
    "scores": [46, 65, 51]
}

datas = pandas.DataFrame(data_dict)
print(datas)
datas.to_csv("rough_file.csv")



