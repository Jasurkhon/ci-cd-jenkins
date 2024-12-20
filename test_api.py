import requests

api_endpoint = "http://0.0.0.0:8080/predict/"

payload = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 3.4,
    "petal_width": 1.2
    }

headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
    }

response = requests.post(api_endpoint, headers=headers, json=payload)

print(response.json())

