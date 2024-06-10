import json
import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)

print(json.dumps(response.json(), indent=2))