import requests

# url = 'https://aq-server.herokuapp.com/predict'
url = 'https://aq-model-server.herokuapp.com/predict'
# url = 'http://localhost:9696/predict'
r = requests.post(url, json={'data': '1,0,0,0,0,0,0,1,1,0,1,28,3,f,middle eastern,yes,no,family member'})
# print(r)
# res = r.text.strip()
print('RESULT: ' + str(r.json()))
res = r.json()['prediction'][0]
print('RESULT 2: ' + str(res))
