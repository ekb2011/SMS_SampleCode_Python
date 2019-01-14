import requests
from collections import OrderedDict

#url, appKeys, and type for calling REST API
url="https://api-sms.cloud.toast.com/sms/v2.1"
appKeys="/appKeys/{appkey}"    
type="/sender/sms"

#define header, requestBody, recipientList, and template
header=OrderedDict()
requestBody=OrderedDict()
recipientList=OrderedDict()
template=OrderedDict()

#making a header
header["Content-Type"]="application/json;charset=UTF-8"

#making a requestBody
requestBody["sendNo"]=""
requestBody["senderGroupingKey"]="SenderGroupingKey"
requestBody["templateId"]=""
requestBody["body"]="modifying a template"

#modifying a template
template[""]=""

#making a recipientList, and put this in the requestBody
recipientList["recipientNo"]=""
recipientList["recipientGroupingKey"]="RecipientGroupingKey"
recipientList["templateParameter"]=template

requestBody["recipientList"]=[recipientList]

#call REST API, and get response
responseBody=requests.post(url+appKeys+type, headers=header, json=requestBody)

#print result
print(responseBody.text)