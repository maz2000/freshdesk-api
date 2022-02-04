from email import header
import requests
import json
from pprint import pprint 

api_key = "7MlnYp82iwiT4bG4xO42"
domain = "newaccount1641238466306"
password = "x"

headers = { 'Content-Type' : 'application/json' }

ticket = {
    'subject' : '至急　壁の不具合',
    'description' : '<div><font face="Arial">?平面図は正しいのに、外観パースを出すと、2階の壁の表示が455ずれて表示されます。</font><div><font face="Arial">最終系は、</font><span style="font-family: Arial;">1階の４５５出ている部分は、フラットルーフにしたいです。</span></div><div><br></div><div><div style="color: rgb(0',
    'email' : 'example@example.com',
    'priority' : 1,
    'status' : 5,
    'source' : 100,
}



r = requests.post("https://"+ domain +".freshdesk.com/api/v2/tickets", auth = (api_key, password), headers = headers,data=json.dumps(ticket))

if r.status_code == 201:
    print("success")
    return_data=  r.json()
    #作成されたチケットのIDを表示
    print(return_data["id"])