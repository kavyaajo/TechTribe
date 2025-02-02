import requests

response = requests.get("https://api.github.com")
print(response.status_code)


url = "http://127.0.0.1:5000"
data = {"message": "I have a severe headache. What should I do?"}
response = requests.post(url, json=data)

print(response)
