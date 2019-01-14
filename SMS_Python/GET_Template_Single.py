import requests
from collections import OrderedDict

#url, appKeys, type, and templateId for calling REST API
url="https://api-sms.cloud.toast.com/sms/v2.1"
appKeys="/appKeys/{appkey}"    
type="/templates"
templateId="/{templateId}"

#define header
header=OrderedDict()

#making a header
header["Content-Type"]="application/json;charset=UTF-8"

#call REST API, and get response
responseBody=requests.get(url+appKeys+type+templateId, headers=header)

#print result
print(responseBody.text)