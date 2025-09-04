import pandas as pd
excel_file = pd.read_excel("Customer_Call_List.xlsx")

# print("Excel data")
# print(excel_file)

# Excel to CSV
excel_file.to_csv("Customer Call List (CSV).csv", index = False)
print("Excel converted to CSV successfully")