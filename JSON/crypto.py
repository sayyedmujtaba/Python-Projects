import requests
import json

url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Data fetched successfully!\n")

    # Print the JSON response in a pretty format
    print(json.dumps(data, indent=4))
    # json.dumps() is used to convert a Python object into a JSON string.
    # The indent parameter is used to define the number of spaces for each nested level.

    # Extracting price information
    price_info = [{
        "symbol": data["symbol"],
        "price": data["price"]
    }]
    
    with open("crypto_prices.json", "w") as f:
        json.dump(price_info, f, indent=4)
    
    print("\nCrypto price data saved to crypto_prices.json")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")