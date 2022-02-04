from email import header
import requests
import json
from pprint import pprint
import csv
import datetime

api_key = "7MlnYp82iwiT4bG4xO42"
domain = "newaccount1641238466306"
password = "x"

headers = {'Content-Type': 'application/json'}

"""
ticket = {
    'subject' : 'this is test subject' ,
    'description' : 'Ticket detail',
    'email' : 'example@example.com',
    'priority' : 1,
    'status' : 5,
    'source' : 100,
}

ticket = {
    'subject': '電源',
    'description': 'this is description',
    'email': 'example@example.com',
    'priority': 1,
    'status': 5,
    'source': 100,
}

enc = json.dumps(ticket)
print(enc)


r = requests.post("https://" + domain + ".freshdesk.com/api/v2/tickets", auth=(api_key, password), headers=headers, data=json.dumps(ticket))
print(r.status_code)

if r.status_code == 201:
    print("success")
    return_data = r.json()
    # 作成されたチケットのIDを表示
    print("Ticket ID=", return_data["id"])

"""

dt_now = datetime.datetime.now()
print("start time=",dt_now)

with open("export_ticket_utf8-2.csv") as f:
    header = next(csv.reader(f))
    reader = csv.reader(f)
    ticket_list = (row for row in reader)
    for row in ticket_list:
       ticket = {
            'subject': row[8],
            'description': row[22],
            'email': 'example@example.com',
            'priority': 1,
            'status': 5,
            'source': 100,
            }
       print("hit!")
       r = requests.post("https://newaccount1641238466306.freshdesk.com/api/v2/tickets",auth=(api_key,password),headers=headers,data=json.dumps(ticket))
       print(r.status_code)
       return_data = r.json()
       print("Ticket ID=", return_data["id"])
       notes = {
           'body': row[28] , 
           'private': True , 
       }
       r = requests.post("https://newaccount1641238466306.freshdesk.com/api/v2/tickets/" + str(return_data["id"]) + "/notes",auth=(api_key,password),headers=headers,data=json.dumps(notes))
       print(r.status_code)

dt_now = datetime.datetime.now()
print("End time=",dt_now)