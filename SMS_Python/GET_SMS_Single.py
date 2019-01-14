import json
import requests
from collections import OrderedDict

header=OrderedDict()
requestBody=OrderedDict()

header["Content-Type"]="application/json;charset=UTF-8"
requestBody["mtPr"]=1

url="https://api-sms.cloud.toast.com/sms/v2.1"
appKeys="/appKeys/{appkey}"    
type="/sender/sms"
requestId="/{requestId}"

responseBody=requests.get(url+appKeys+type+requestId, headers=header, params=requestBody)

print(responseBody.text)
