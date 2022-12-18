import requests

song_id = input("Which song id to use?\n")

try:
    song_id = int(song_id)
except:
    song_id = None
    print(f"{song_id} is not valid id")

if song_id:
    endpoint = f"http://127.0.0.1:8000/api/songs/{song_id}/delete"
    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code==204)
