# with open("./weather_data.csv","r") as data_file:
#     data_list = data_file.readlines()
#     for every_day in data_list:
#         every_day = every_day.strip()
#         print(every_day)
from calendar import MONDAY

# import csv
# with open("./weather_data.csv","r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas
# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
#
# # total_temp = 0
# # for each_temp in temp_list:
# #     total_temp += float(each_temp)
# # avg_temp = total_temp/len(temp_list)
# # print(avg_temp)
#
# avg_temp = data["temp"].mean()
# print(avg_temp)
#
# max_temp = data["temp"].max()
# print(max_temp)
#
# #We can also use pandas as:
# print(data.temp.max())
#
# #How to get control of a row in data
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max() ])
#
# #Create a dataframe
# data_dict = {
#     "students": ["ayan","vaibhav","rahul"],
#     "scores": [90, 90, 90]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# # Create a csv file from the dataframe
# data.to_csv("new_data.csv")

import pandas
data = pandas.read_csv("./squirrel_data.csv")
fur_color_list = data["Primary Fur Color"]
primary_colors = fur_color_list.dropna().to_list()
# colors = set(primary_colors) '''Tells unique values from the list'''
# print(colors)
grey = 0
cinnamon = 0
black = 0
for color in primary_colors:
    color = color.lower()
    if color == "gray":
        grey += 1
    elif color == "cinnamon":
        cinnamon += 1
    else:
        black += 1
print(grey, cinnamon, black)
data = {
    "Fur Color": ["black","gray","cinnamon"],
    "Count": [black, grey, cinnamon]
}
data = pandas.DataFrame(data)
data.to_csv("squirrel_count.csv")

