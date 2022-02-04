import requests
import json
from pprint import pprint 

api_key = "API_KEY"
domain = "DOMAIN"
password = "x"

url = requests.get("https://"+ domain +".freshdesk.com/api/v2/solutions/categories/73000240499/folders", auth = (api_key, password))

print(url.status_code)

if url.status_code == 200:
    print("success")

jsondata = url.json()
for dat in jsondata:
    print(dat["name"])

