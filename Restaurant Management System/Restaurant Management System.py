from termcolor import colored

menu = {
    "Tea": 50,
    "Cookies": 50,
    "Biryani": 150,
    "Pasta" : 80,
    "Burger" : 120,
}

def display_menu():
    print(colored("Welcome to Python Food Corner", "yellow"))
    for item, price in menu.items():
        print(f"{item.title()}: {price} PKR")
display_menu()

total_bill = 0

while True:
    order = input(colored("Please enter your order: ", "green")).title() # We can use .capitalize() too but that only capitalize the forst character of a string while .title() capitalize the first character of each word
    if order in menu:
        total_bill += menu[order]
        print(f"Your bill is {total_bill} PKR")
    else:
        print("Please select an item from the menu")

    more = input("Do you want to order more? (yes/no): ").strip().lower()
    if more == "yes":
        continue # If the user wants to order more, continue the loop
    elif more == "no":
        print(colored(f"Your total is: {total_bill} PKR", "magenta"))
        break