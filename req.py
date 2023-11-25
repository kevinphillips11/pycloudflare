import requests

url = "https://handy-labrador-humane.ngrok-free.app/"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
