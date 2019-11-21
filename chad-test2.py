import requests
import json
import base64
import spotipy

client_id = '5ec1efbe2ff3440c9d1f419dcaefcdfc'
client_secret = '47496dec8ce641d4bd1f982835266e0e'
username = '225rpxn4vfmxoqug5o3s57qia'

creds = (client_id + ':' + client_secret)
encoded = base64.b64encode(creds.encode("utf-8"))
encodedStr = str(encoded, "utf-8")
# print(encodedStr)

headers = {
    'Authorization': 'Basic ' + encodedStr
}

url = 'https://accounts.spotify.com/api/token'
mydata = {
    'grant_type': 'client_credentials'
}

response = requests.post(url, data=mydata, headers=headers)

check = response.json()

# print(json.dumps(check, indent=4, sort_keys=True))

# url2 = 'https://api.spotify.com/v1/me'
# url2 = 'https://api.spotify.com/v1/users/225rpxn4vfmxoqug5o3s57qia'
url2 = 'https://api.spotify.com/v1/users/225rpxn4vfmxoqug5o3s57qia/playlists'
headers2 = {
    'Authorization': 'Bearer ' + check['access_token']
}
response2 = requests.get(url2, headers=headers2)

check2 = response2.json()

# print(json.dumps(check2, indent=4, sort_keys=True))

# file = open("response.json", "w")
# file.write(json.dumps(check2, indent=4, sort_keys=True))
# file.close()

spotify = spotipy.Spotify()
results = spotify.user_playlist(username, '38CXaK1QtGbnPVuXz75Upu')

print('results = ' + results)

file = open("results.txt", "w")
file.write(results)
file.close()
