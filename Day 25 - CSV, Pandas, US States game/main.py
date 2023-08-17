# import csv

# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temperatures=[]
#     for row in data:
#         if(row[1].isnumeric()):
#             temperatures.append(int(row[1]))
#     for t in temperatures:
#         print(t)

import subprocess
## Install pandas if its not already installed
module_name = "pandas"
subprocess.run(["pip", "install", module_name])
import pandas

#data=pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()

# temp_list=data["temp"].to_list()
# avg_temp=round(sum(temp_list)/len(temp_list),2)
# print(avg_temp)
# print(data["temp"].mean())
# print(data["temp"].max())

# print(data["condition"])
# print(data.condition)

# print(data[data.day=="Monday"])
# print(data[data.temp==data.temp.max()])

# monday=data[data.day=="Monday"]
# print(monday.condition)
# monday_temp=int(monday.temp)
# monday_temp_F=(monday_temp*(9/5))+32
# print(monday_temp_F)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65],
# }
# data=pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data=pandas.read_csv("2018centalparksquirrels.csv")
gray_squirrels_count=len(data[data["Primary Fur Color"]=="Gray"])
brown_squirrels_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrels_count=len(data[data["Primary Fur Color"]=="Black"])

data_dict={
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, brown_squirrels_count, black_squirrels_count],
}
print(data_dict)
df=pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")