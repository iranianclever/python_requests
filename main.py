import requests

url = 'https://localhost:5000/api/process'
data = {'license': 'ok'}

request = requests.post(url, json=data)

print(request.status_code)
print(request.text)
