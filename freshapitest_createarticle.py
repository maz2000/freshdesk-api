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

with open("article100.csv") as f:
    header = next(csv.reader(f))
    reader = csv.reader(f)
    folder_list = (row for row in reader)
    for row in folder_list:
        print(row[1])
        print(row[2])
        article_content = {
            "title" : row[2],
            "description" : row[3] ,
            "status" : 1,
        }
        url_path = ("https://"+ domain +".freshdesk.com/api/v2/solutions/folders/73000322971/articles")
        print (url_path)
        r = requests.post(url_path, auth = (api_key, password), headers = headers,data=json.dumps(article_content))
        print(r.status_code)
