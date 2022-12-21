import requests
import json

def headerfun(head):
    header=json.loads(head)
    return(header)
    
def request(t,url,auth_token,head):
    while len(head)>1:
        jsheader=headerfun(head)
        break
    else:
        jsheader=head
    if t=="GET":
        r=requests.get(url,auth=auth_token,headers=jsheader)
        statcode=r.status_code
        txt=r.text
        head=r.headers
    if t=="POST":
        r=requests.post(url,auth=auth_token,headers=jsheader)
        statcode=r.status_code
        txt=r.text
        head=r.headers
    return(statcode,txt,head)
        