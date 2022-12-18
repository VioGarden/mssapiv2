import requests
import json

headers = {'Authorization': 'Bearer ef9985f075799a0e059e070a9dc77938848ab527'}

endpoint = "http://127.0.0.1:8000/api/songs/"


with open("scrapeamq.json") as f:
    full = json.load(f)

final4 = []


for i in range(len(full)):
    final_object = {}
    final_object['title'] = full[i][0]
    final_object['titleRom'] = full[i][1]
    final_object['song'] = full[i][2]
    final_object['artist'] = full[i][3]
    final_object['opedin'] = full[i][4]
    final_object['video'] = full[i][5]
    final_object['audio'] = full[i][6]
    final4.append(final_object)

for i in range(len(final4)):
    data = final4[i]
    get_response = requests.post(endpoint, json=data, headers=headers)
    print(get_response.json())