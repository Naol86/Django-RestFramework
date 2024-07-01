import requests

end_point = "http://127.0.0.1:8000/api/product/1"

response = requests.get(end_point)

print(response.status_code)
print(response.json())