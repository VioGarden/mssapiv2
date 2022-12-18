import requests


song_id = input("Which song id to update?\n")

try:
    song_id = int(song_id)
except:
    song_id = None
    print(f"{song_id} is not valid id")

endpoint = f"http://127.0.0.1:8000/api/songs/{song_id}/update"
data = {} # fill in

get_response = requests.put(endpoint, json=data)
print(get_response.json())