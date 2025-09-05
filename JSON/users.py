import requests
import json

url = "https://randomuser.me/api/?results=7" #results=7 to get 7 random users
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Data fetched successfully!\n")

    # Print the JSON response in a pretty format
    print(json.dumps(data, indent=4))
    # json.dumps() is used to convert a Python object into a JSON string.
    # The indent parameter is used to define the number of spaces for ach nested level.

    # Extracting user names and emails
    users = []
    for user in data["results"]:
        users.append({
            "name": f"{user['name']['first']} {user['name']['last']}",
            "email": user["email"]
        })

    # Save the extracted data to a JSON file
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)

    print("\nUser data saved to users.json")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")