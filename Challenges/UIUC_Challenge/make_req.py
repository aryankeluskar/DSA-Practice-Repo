import requests

# Specify the URL you want to send the request to
url = "https://artemis.hackillinois.org/challenge"

# Define headers (optional)
headers = {
    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImdpdGh1YjgwMDkzMzkyIiwiZW1haWwiOiJhcnlhbmtlbHVza2FyNkBnbWFpbC5jb20iLCJwcm92aWRlciI6ImdpdGh1YiIsInJvbGVzIjpbIlVTRVIiXSwiZXhwIjoxNzA4OTA2MTc1LjY3NywiaWF0IjoxNzA2MzE0MTc1fQ.CKJd0DZkLU2XrDAWDNn9674SjvCWSViq1Tq-2X_eFso",
    "Content-Type": "application/json",
}

# Define the request body (optional, depends on the type of request)
payload = {
    "max_goodness": int(4083),
}

response = requests.post(url, headers=headers, json=payload)

# Check the response status code
if response.status_code == 200:
    print("Request was successful!")
    print("Response JSON:", response.json())

else:
    print(f"Request failed with status code {response.status_code}")
    print("Response text:", response.text)
