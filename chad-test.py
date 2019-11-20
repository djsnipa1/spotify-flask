import requests
import json
import base64

# var request = require('request')

client_id = '5ec1efbe2ff3440c9d1f419dcaefcdfc'
client_secret = '47496dec8ce641d4bd1f982835266e0e'
creds = (client_id + ':' + client_secret)
encoded = base64.b64encode(creds.encode("utf-8"))
encodedStr = str(encoded, "utf-8")
print(encodedStr)

headers = {
    # 'Accept': 'application/json',
    # 'Content-Type': 'application/json',
    #    'Authorization': 'Basic ' + client_id + ':' + client_secret
    'Authorization': 'Basic ' + encodedStr
}
# authOptions = {
#     url: 'https://accounts.spotify.com/api/token',
#     headers: {
#         'Authorization': 'Basic ' + (new Buffer(client_id + ':' + client_secret).toString('base64'))
#     },
#     form: {
#         grant_type: 'client_credentials'
#     },
#     json: true
# }
# headers = {
#     'Accept': 'application/json',
#     'Content-Type': 'application/json',
#     'Authorization': 'Bearer AQAmLsRD0cImcFksN3WokZCn606wbXUFyL0pGhqcB-0YkU7gxpOH6U-f2edEtU8KPDzhoeb_MALIk0KO3xlOFL2hnI-gYtC6AJbiTsd3lIKQWmABddxyMLfeTj7sjBWu3m09OI7kCFMdebrqT_CL5FoHVcaLDpZXvQlf_iJj52_zREwPz6pXKpTICkUlFYDaWjcQ_YRQ3YUzetKOWb9k0AUCmxmlIlpBVxPDlXV1iWSO8HD638pl9dAVY9MidlghBCsLYxFN3Q'
# }

# print(headers2)

url = 'https://accounts.spotify.com/api/token'
mydata = {
    'grant_type': 'client_credentials'
}

response = requests.post(url, data=mydata, headers=headers)

check = response.json()

print(json.dumps(check, indent=4, sort_keys=True))
# response = requests.post(
# 'https://accounts.spotify.com/api/token', data=mydata, headers=headers2)

# url2 = 'https://api.spotify.com/v1/me'
# url2 = 'https://api.spotify.com/v1/users/225rpxn4vfmxoqug5o3s57qia'
url2 = 'https://api.spotify.com/v1/users/225rpxn4vfmxoqug5o3s57qia/playlists'
headers2 = {
    'Authorization': 'Bearer ' + check['access_token']
}
response2 = requests.get(url2, headers=headers2)

check2 = response2.json()

print(json.dumps(check2, indent=4, sort_keys=True))
# id = json.dumps(check['id'])

# print("nice! my id is " + id)
file = open("response.json", "w")
file.write(json.dumps(check2, indent=4, sort_keys=True))
file.close()
