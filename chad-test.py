import requests
import json

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQCFv2wPI4CI-YQwc-uMUm6nF4CjXdp30myz8Pb_CuL_vR167_YvJe0c1WKPAw_cq6UFv-PrUnnjm61Motj6UY7O2X-Wv2I8uyytk69r3lzPkXJmIChOnVSzkdb5NVtELOfWR0fIeOtHUAsqgX5gMTiNEs8405rcyP3xsYKK9DssA9O9VA',
}

response = requests.get('https://api.spotify.com/v1/me', headers=headers)

check = response.json()
# print(check)


print(json.dumps(check, indent=4, sort_keys=True))

id = json.dumps(check['id'])

print("nice! my id is " + id)
