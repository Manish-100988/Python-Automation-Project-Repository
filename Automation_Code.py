import requests
# GET request (fetch data)
response = requests.get("https://api.example.com/data")
# POST request (send data)
requests.post("https://api.example.com/submit", json={"key": "value"})
