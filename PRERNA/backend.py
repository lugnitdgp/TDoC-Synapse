import requests
import json
from auth import MyAuth


def headerfunc(head):
    header=json.loads(head)
    return (header)

def request(t,url,param,auth_token,head,json):
    while len(head)>1:
        jsheader=headerfunc(head)
        break
    else:
        jsheader=head

    if t=="GET":
        r=requests.get(url,params=param,auth=MyAuth(auth_token),headers=jsheader,data=json)
        statcode=r.status_code
        txt=r.text
        hed=r.headers
    if t=="POST":
        r=requests.post(url,params=param,auth=MyAuth(auth_token),headers=jsheader,data=json)
        statcode=r.status_code
        txt=r.text
        hed=r.headers
    if t=="PUT":
        r=requests.put(url,params=param,auth=MyAuth(auth_token),headers=jsheader,data=json)
        statcode=r.status_code
        txt=r.text
        hed=r.headers
    if t=="PATCH":
        r=requests.patch(url,params=param,auth=MyAuth(auth_token),headers=jsheader,data=json)
        statcode=r.status_code
        txt=r.text
        hed=r.headers
    if t=="DELETE":
        r=requests.delete(url,params=param,auth=MyAuth(auth_token),headers=jsheader,data=json)
        statcode=r.status_code
        txt=r.text
        hed=r.headers
    return (statcode,txt,hed)
