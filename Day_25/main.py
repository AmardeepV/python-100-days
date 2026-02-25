import pandas

data = pandas.read_csv("Central_Park_Squirrel_Data.csv")
# colors = data["Primary Fur Color"].unique()
counts = data["Primary Fur Color"].value_counts()
pandas.DataFrame(counts).to_csv("unique_colors_count.csv")
