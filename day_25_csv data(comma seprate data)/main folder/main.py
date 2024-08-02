import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240614.csv")


# we use length because when we take a rows then all they are treated as list so we can use len()
black_squirrels_color = len(data[data["Primary Fur Color"] == "Black"])
Cinnamon_squirrels_color = len(data[data["Primary Fur Color"] == "Cinnamon"])
Gray_squirrels_color = len(data[data["Primary Fur Color"] == "Gray"])


data_dict = {
    "fur_color": ["Black", "Cinnamon", "Gray"],
    "Count": [black_squirrels_color, Cinnamon_squirrels_color, Gray_squirrels_color]
}


data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrels count.csv")
