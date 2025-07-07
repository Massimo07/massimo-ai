import requests

url = "http://127.0.0.1:8080/ask"
data = {"question": "Che crema consigli per pelle secca?"}
response = requests.post(url, json=data)
print(response.json())

