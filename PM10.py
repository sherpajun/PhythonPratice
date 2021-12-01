from pandas.io.json import json_normalize
import requests
url='http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=zRFvHX1aXXCIImm6VM1r41s7qtk%2BZvLgs6in9M1REA4KFCxy9almfJetM4CgsUwUOATf7XkgGquTvNULLJtJ%2FA%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0'
response = requests.get(url)
response


import json, requests 

url = requests.get("https://jsonplaceholder.typicode.com/users")
text = url.text

data = json.loads(text)

user = data[0]
print(user['name'])

address = user['address']
print(address)