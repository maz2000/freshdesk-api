import requests
import json
from pprint import pprint 
import re
import csv

api_key = "API_KEY"
domain = "DOMAIN"
password = "x"
folder_list = []
headers = { 'Content-Type' : 'application/json' }

with open("folder.csv") as f:
    header = next(csv.reader(f))
    reader = csv.reader(f)
    folder_list = (row for row in reader)
    for row in folder_list:
        print (row[1],row[3]) 
        folder_name = {
            "name" : row[1],
            "description" : "" ,
            "visibility" : 1,
        }
        url_path = ("https://"+ domain +".freshdesk.com/api/v2/solutions/categories/"+ row[4] + "/folders")
        print (url_path)
        r = requests.post(url_path, auth = (api_key, password), headers = headers,data=json.dumps(folder_name))
        print(r.status_code)
