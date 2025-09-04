import pandas as pd

csv_file = pd.read_csv("Ice Cream Ratings.csv")
# print("CSV data")
# print(csv_file)

# CSV to excel
csv_file.to_excel("Ice Cream (Excel).xlsx", index = False)
print("CSV converted to excel successfully")