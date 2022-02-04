import requests
import json
from pprint import pprint 
import re
import csv

api_key = "API_KEY"
domain = "DOMAIN"
password = "x"
category_list = []
headers = { 'Content-Type' : 'application/json' }

with open("category.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        category_list.append(row[1])

del category_list[0]
#print(category_list)

for cat in category_list:
    print(cat)
    category = {
    'name' : cat,
    }
r = requests.post("https://"+ domain +".freshdesk.com/api/v2/solutions/categories", auth = (api_key, password), headers = headers,data=json.dumps(category))
print(r.status_code)
q  = requests.get("https://"+ domain +".freshdesk.com/api/v2/solutions/categories", auth = (api_key, password))
print(q.content)
