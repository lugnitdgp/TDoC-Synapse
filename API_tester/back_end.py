import requests
import json
from authorization import MyAuth  

def headerfxn(head):
    header = json.loads(head)
    return (header)

def request(t, url, auth_token, head, param, jsons):
    while len(head)>1:
        jshead = headerfxn(head)
        break
    else:
        jshead = head

    if t == "GET":
        r = requests.get(url, auth = MyAuth(auth_token), headers=jshead, params=param, json=jsons)
        statcode = r.status_code
        txt = r.text
        head = r.headers
    if t == "POST":
        r = requests.post(url, auth = MyAuth(auth_token), headers=jshead, params=param, json=jsons)
        statcode = r.status_code
        txt = r.text
        head = r.headers
    if t == "PATCH":
        r = requests.patch(url, auth = MyAuth(auth_token), headers=jshead, params=param, json=jsons)
        statcode = r.status_code
        txt = r.text
        head = r.headers
    if t == "PUT":
        r = requests.put(url, auth = MyAuth(auth_token), headers=jshead, params=param, json=jsons)
        statcode = r.status_code
        txt = r.text
        head = r.headers
    if t == "DELETE":
        r = requests.delete(url, auth = MyAuth(auth_token), headers=jshead, params=param, json=jsons)
        statcode = r.status_code
        txt = r.text
        head = r.headers
    return (statcode, txt, head)
