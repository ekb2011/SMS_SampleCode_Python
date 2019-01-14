import requests
from collections import OrderedDict

#url, appKeys, and type for calling REST API
url="https://api-sms.cloud.toast.com/sms/v2.1"
appKeys="/appKeys/EGAHwbWtW692uzLs"    
type="/tag-sender/sms"

#define header, requestBody, and recipientList
header=OrderedDict()
requestBody=OrderedDict()
recipientList=OrderedDict()
tagExpression=OrderedDict()

#making a header
header["Content-Type"]="application/json;charset=UTF-8"

#making a requestBody
requestBody["body"]="Tag Test"
requestBody["sendNo"]="01041002071"
requestBody["senderGroupingKey"]="SenderGroupingKey"

#making a recipientList, and put this in the requestBody
recipientList["recipientNo"]="01041002071"
recipientList["recipientGroupingKey"]="RecipientGroupingKey"

requestBody["recipientList"]=[recipientList]
requestBody["tagExpression"]=["aKYyaCa0","AND","vfQCw9ib"]

#call REST API, and get response
responseBody=requests.post(url+appKeys+type, headers=header, json=requestBody)

#print result
print(responseBody.text)