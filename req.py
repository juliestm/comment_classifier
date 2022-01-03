import requests
URL = "http://127.0.0.1:5000/predict"
requests.get("http://127.0.0.1:5000/")
response = requests.post(URL, json='{"text":"Все было не очень хорошо, я бы даже сказал не отлично"}')
print(response.json()["answer"][1:-1])
