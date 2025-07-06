rent = int(input("Enter your hostel/flat rent: "))
food = int(input("Enter the amount of food ordered: "))
electricity_bill = int(input("Enter the amount of electricity bill: "))
persons = int(input("Enter the number of persons living in flat: "))

total_bill = rent + food + electricity_bill
output = (total_bill) // persons

print(f"Total bill is: {total_bill}, amount to be paid by each person is: {output}")