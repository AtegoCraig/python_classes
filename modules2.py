import requests

# Make a GET request to the joke API
response = requests.get("https://official-joke-api.appspot.com/random_joke")

# Check if the request was successful
if response.status_code == 200:
    joke = response.json()
    print("Here's a joke for you:")
    print(f"{joke['setup']}")
    print(f"{joke['punchline']}")
else:
    print("Couldn't fetch a joke at the moment.")