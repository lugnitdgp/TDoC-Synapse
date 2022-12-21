import requests
import json
from auth import MyAuth

def headerfxn(head):
        header = json.loads(head)
        return (header)


def request(t, url, auth_token, head):
        while len(head)>1:
                jsheader = headerfxn(head)
                break
        else :
                jsheader = head
        if t=="GET":
                r = requests.get(url, auth=MyAuth(auth_token), headers=jsheader)
                statcode = r.status_code
                txt = r.text
                head = r.headers
        if t=="POST":
                r = requests.post(url, auth=MyAuth(auth_token), headers=jsheader)
                statcode = r.status_code
                txt = r.text
                head = r.headers
        if t=="PUT":
                r = requests.post(url, auth=MyAuth(auth_token), headers=jsheader)
                statcode = r.status_code
                txt = r.text
                head = r.headers
        if t=="PATCH":
                r = requests.post(url, auth=MyAuth(auth_token), headers=jsheader)
                statcode = r.status_code
                txt = r.text
                head = r.headers
        if t=="DELETE":
                r = requests.post(url, auth=MyAuth(auth_token), headers=jsheader)
                statcode = r.status_code
                txt = r.text
                head = r.headers
        return (statcode, txt, head)