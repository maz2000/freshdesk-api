from email import header
import requests
import json
from pprint import pprint 

api_key = "API_KEY"
domain = "DOMAIN"
password = "x"

ticket_id = "84"

headers = { 'Content-Type' : 'application/json' }

note = {
   'body' : 'Sample reply'
}

r = requests.post("https://"+ domain +".freshdesk.com/api/v2/tickets/"+ticket_id+"/reply", auth = (api_key, password), headers = headers,data=json.dumps(note))

print(r.status_code)

if r.status_code == 201:
    print("success")
    return_data=  r.json()
    #作成されたチケットのIDを表示
    print(return_data["id"])