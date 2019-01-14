import requests
from collections import OrderedDict

#url, appKeys, type, requestId, and query for calling REST API
url="https://api-sms.cloud.toast.com/sms/v2.1"
appKeys="/appKeys/{appkey}"    
type="/sender/mms"
requestId="/{requestId}"
query="?mtPr=1"

#define header
header=OrderedDict()
requestBody=OrderedDict()

#making a header
header["Content-Type"]="application/json;charset=UTF-8"

#call REST API, and get response
responseBody=requests.get(url+appKeys+type+requestId+query, headers=header)

#print result
print(responseBody.text)