import requests
import os

token = os.environ.get("FRIENDLI_TOKEN") or "YOUR_FRIENDLI_TOKEN"

url = "https://api.friendli.ai/dedicated/v1/completions"

headers = {
  "Authorization": "Bearer " + token,
  "Content-Type": "application/json"
}

payload = {
  "model": "845nxzat3y3y",
  "prompt": "",
  "max_tokens": 512,
  "temperature": 0.8,
  "top_p": 0.95
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)