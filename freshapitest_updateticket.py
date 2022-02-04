from email import header
import requests
import json
from pprint import pprint 

api_key = "7MlnYp82iwiT4bG4xO42"
domain = "newaccount1641238466306"
password = "x"

ticket_id = "84"

headers = { 'Content-Type' : 'application/json' }

ticket = {
    'subject' : 'Update title',
    'description' : 'Update Ticket detail',
}



r = requests.put("https://"+ domain +".freshdesk.com/api/v2/tickets/"+ticket_id, auth = (api_key, password), headers = headers,data=json.dumps(ticket))

print(r.status_code)

if r.status_code == 201:
    print("success")
    return_data=  r.json()
    #作成されたチケットのIDを表示
    print(return_data["id"])