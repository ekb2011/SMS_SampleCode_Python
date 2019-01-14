import requests
from collections import OrderedDict

#url, appKeys, and type for calling REST API
url="https://api-sms.cloud.toast.com/sms/v2.1"
appKeys="/appKeys/{appkey}"    
type="/reservations/cancel"

#define header, and reservationList
header=OrderedDict()
requestBody=OrderedDict()
reservationList=OrderedDict()

#making a reservationList, and requestBody for deleting reserved SMS
reservationList["requestId"]="20181231103000Ms0ClUUh3u0"
reservationList["recipientSeq"]=1

requestBody["reservationList"]=[reservationList]
requestBody["updateUser"]="gibonglim"

#making a header
header["Content-Type"]="application/json;charset=UTF-8"

#call REST API, and get response
responseBody=requests.put(url+appKeys+type, headers=header, json=requestBody)

#print result
print(responseBody.text)