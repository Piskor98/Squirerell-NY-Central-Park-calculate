import csv
import pandas
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     weather=[]
#     temp_values = []
#     for row in data:
#         weather.append(row)
#         print(row)
#         if row[1] != 'temp':
#          temp_values.append(int(row[1]))
#
#     print(temp_values)

data=pandas.read_csv("weather_data.csv")    #We can explain the table by pandas library
# print(type(data))
# print(data["temp"])                         #Also we can print only columns
# print(type(data["temp"]))
#
#
# data_dict=data.to_dict()                    #we can change data.csv to dictionary
# print(data_dict)
#
# temp_list=data["temp"].to_list()            #and any of coulmn, that is inside data.csv to table
# print(temp_list)
#
# sum=0                                       #Basic method to calculate avr
# for temp in temp_list:
#     sum=sum+temp
# avr=sum/(len(temp_list))
# print(avr)
#
# print(data["temp"].mean())                  #Pandas method to calculate avr
#
# print(data["temp"].max())
#
# #Get data in columns
# print(data["condition"])                    #pandas put avery column as attribute of csv data
# print(data.condition)                       #Same result as line before

#Get Data in Row
print(data[data.day=="Monday"])
print(data[data.temp == data.temp.max()])
#
monday=(data[data.day=="Monday"])
monday_temp=float((monday["temp"])*(9/5)+32)
print(monday_temp)

#Create a dataframe from scratch

data_dict={
    "students": ["Amy", "James", "Angela"],
    "scores": [76,56,65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("./data_dict.csv")              #creating a csv file