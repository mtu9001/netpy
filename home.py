import requests


r = requests.get("https://api.github.com")
print(r.status_code)
