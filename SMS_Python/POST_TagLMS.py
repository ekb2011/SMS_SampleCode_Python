import requests
from collections import OrderedDict

#url, appKeys, and type for calling REST API
url="https://api-sms.cloud.toast.com/sms/v2.1"
appKeys="/appKeys/{appkey}"    
type="/tag-sender/mms"

#define header, requestBody, and recipientList
header=OrderedDict()
requestBody=OrderedDict()
recipientList=OrderedDict()

#making a header
header["Content-Type"]="application/json;charset=UTF-8"

#making a requestBody
requestBody["title"]="tag Title"
requestBody["body"]=""
requestBody["sendNo"]=""
requestBody["senderGroupingKey"]="SenderGroupingKey"

#making a recipientList, and put this in the requestBody
recipientList["recipientNo"]=""
recipientList["recipientGroupingKey"]="RecipientGroupingKey"

requestBody["recipientList"]=[recipientList]
requestBody["tagExpression"]=["aKYyaCa0","AND","vfQCw9ib"]

#call REST API, and get response
responseBody=requests.post(url+appKeys+type, headers=header, json=requestBody)

#print result
print(responseBody.text)