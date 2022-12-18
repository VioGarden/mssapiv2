import requests
from getpass import getpass

auth_endpoint = "http://127.0.0.1:8000/api/auth/"
username = input('Username: ')
password = getpass()

auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})
print(auth_response.json())

# endpoint = "http://127.0.0.1:8000/api/songs/"

# get_response = requests.get(endpoint)
# print(get_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://127.0.0.1:8000/api/songs/"
    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())