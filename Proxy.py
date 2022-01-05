import requests

proxy = {'https': 'https://198.12.65.175:35036'}

response = requests.get("https://ipinfo.io/json", proxies= proxy)
print(response.text)