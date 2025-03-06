# import csv

# with open("Intermediate_Working_with_CSV_Data_and_the_Pandas_Library/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for data in data:
#         if data[1] != "temp":
#             temperatures.append(int(data[1]))
#     print(temperatures)


# import pandas
# data = pandas.read_csv("Intermediate_Working_with_CSV_Data_and_the_Pandas_Library/weather_data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)



# print(data["temp"].mean())

# print(data["temp"].max())

# print(data["day"])
# print(data.day)


# print(data[data.day == 'Monday'])

# print(data[data.temp == data.temp.max()]) 


# monday = data[data.day == "Monday"]
# print(monday.temp)


# data_dict = {

#     "students":["Hirak","Supriya"],
#     "scores":[90,99]
# }

# data = pandas.DataFrame(data_dict)
# print(data.to_csv("Intermediate_Working_with_CSV_Data_and_the_Pandas_Library/data.csv"))





import pandas
data = pandas.read_csv("Intermediate_Working_with_CSV_Data_and_the_Pandas_Library/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_color = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_color = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_color = len(data[data["Primary Fur Color"] == "Black"])


data_dict = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count":[gray_color,cinnamon_color,black_color]
}

data = pandas.DataFrame(data_dict)
data.to_csv("Intermediate_Working_with_CSV_Data_and_the_Pandas_Library/2018_Central_Park.csv")
