import requests
from collections import OrderedDict

#url, appKeys, type for calling REST API
url="https://api-sms.cloud.toast.com/sms/v2.1"
appKeys="/appKeys/{appkey}"    
type="/reservations"

#define header, requestBody
header=OrderedDict()

#making a header
header["Content-Type"]="application/json;charset=UTF-8"

#call REST API, and get response
responseBody=requests.get(url+appKeys+type, headers=header)

#print result
print(responseBody.text)