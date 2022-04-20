import csv
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")         #Load Excel Data to csv file
print(data)

kolor=(data["Primary Fur Color"]).to_list()                                             #Extract color_column to list

Gray=0                                                                                  #defined the basic variables
Cinnamon=0
Black=0

for color in kolor:                                                                     #main loop to count Squirrels colors
    if color == 'Gray':
        Gray = Gray+1
    elif color=='Black':
        Black=Black+1
    elif color == 'Cinnamon':
        Cinnamon=Cinnamon+1
    else:
        pass

print(Gray, Cinnamon, Black)                                                            #result

final_result_dict={                                                                     #Create a dictionary that achieve results
    "color": ['Grey','Cinnamon','Black'],
    "count": [Gray,Cinnamon,Black]
}
result = pandas.DataFrame(final_result_dict)                                            #Transform dictionary to csv file with results
result.to_csv("./Squirrel_out.csv")




#ANGELA VERSION

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

