import requests
import json
from pprint import pprint 

api_key = "API_KEY"
domain = "DOMAIN"
password = "x"

url = requests.get("https://"+ domain +".freshdesk.com/api/v2/tickets?filter=new_and_my_open", auth = (api_key, password))

if url.status_code == 200:
    print("success")

jsondata = url.json()

for dat in jsondata:
    print(dat["subject"],dat["created_at"],dat["status"])
