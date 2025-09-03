# kilometers to miles
def km_to_miles(km):
    return km * 0.621371

# miles to kilometers
def miles_to_km(miles):
    return miles / 0.621371

# celsius to fahrenheit
def c_to_f(celsius):
    return (celsius * 9/5) + 32

# fahrenheit to celsius
def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

# inches to centimeters
def i_to_cm(inches):
    return inches * 2.54

# centimeters to inches
def cm_to_i(cm):
    return cm/2.54

# ---------------------------------------------------------------------------- #
#                                 Main program                                 #
# ---------------------------------------------------------------------------- #
print("--- Unit Converter ---")
print("1 for Kilometers to Miles")
print("2 for Miles to Kilometers")
print("3 for Celsius to Fahrenheit")
print("4 for Fahrenheit to Celsius")
print("5 for Inches to Centimeters")
print("6 for Centimeters to Inches")

# ---------------------------------------------------------------------------- #
#                               user interaction                               #
# ---------------------------------------------------------------------------- #
choice = input("Choose conversion (1-6): ")
try:
    if choice == '1':
        km = float(input("Enter kilometers: "))
        print(f"{km} km is {round(km_to_miles(km), 2)} miles")
    elif choice == '2':
        miles = float(input("Enter miles: "))
        print(f"{miles} miles is {round(miles_to_km(miles), 2)} km")
    elif choice == '3':
        celsius = float(input("Enter Celsius: "))
        print(f"{celsius}°C is {round(c_to_f(celsius), 2)}°F")
    elif choice == '4':
        fahrenheit = float(input("Enter Fahrenheit: "))
        print(f"{fahrenheit}°F is {round(f_to_c(fahrenheit), 2)}°C")
    elif choice == '5':
        inches = float(input("Enter inches: "))
        print(f"{inches} inches is {round(i_to_cm(inches), 2)} cm")
    elif choice == '6':
        cm = float(input("Enter centimeters: "))
        print(f"{cm} cm is {round(cm_to_i(cm), 2)} inches")
    else:
        print("Invalid choice.")
except ValueError:
    print("Please enter a valid number.")