# pip install requests
import requests

url = "http://api.open-notify.org/iss-now.json"


response = requests.get(url)  # asking for the data from the URL/API

print(response.status_code)  # 200 - SUCCESS

print(response)

data = response.json()

print(data)
