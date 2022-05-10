import pandas

data = pandas.read_csv("squirrel_data.csv")

color = 'Primary Fur Color'
color_data = data[color]
print(color_data)

gray = 0
cinnamon = 0
black = 0

for row in color_data:
    if row == "Gray":
        gray = gray + 1
    elif row == "Black":
        black = black + 1
    elif row == "Cinnamon":
        cinnamon = cinnamon + 1


new_data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray, cinnamon, black]
}

new_data = pandas.DataFrame(new_data_dict)
print(new_data)

new_data.to_csv("new_squirrel.csv")