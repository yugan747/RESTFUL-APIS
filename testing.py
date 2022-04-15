import requests
import json

URL="http://127.0.0.1:8000/create_data/"
data={
    'Name':'Yugan',
    'city':123

}

data_json = json.dumps(data)
r=requests.post(url =URL,data=data_json)
data=r.json()
print(data)