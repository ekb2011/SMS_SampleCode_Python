import requests
from collections import OrderedDict

#url, appKeys, and type for calling REST API
url="https://api-sms.cloud.toast.com/sms/v2.1"
appKeys="/appKeys/{appkey}"    
type="/sender/sms"

#define header, requestBody, and recipientList
header=OrderedDict()
requestBody=OrderedDict()
recipientList=OrderedDict()

#making a header
header["Content-Type"]="application/json;charset=UTF-8"

#making a requestBody
requestBody["body"]="Python Test by REST API"
requestBody["sendNo"]="01041002071"
requestBody["senderGroupingKey"]="SenderGroupingKey"

#making a recipientList, and put this in the requestBody
recipientList["recipientNo"]="01041002071"
recipientList["recipientGroupingKey"]="RecipientGroupingKey"

requestBody["recipientList"]=[recipientList]

#call REST API, and get response
responseBody=requests.post(url+appKeys+type, headers=header, json=requestBody)

#print result
print(responseBody.text)