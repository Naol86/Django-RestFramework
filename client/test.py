import requests

end_point = "http://127.0.0.1:8000/api/"

response = requests.get(end_point, params={"abc": 123}, json={"query": "hello world"})

print(response.status_code)
print(response.json())