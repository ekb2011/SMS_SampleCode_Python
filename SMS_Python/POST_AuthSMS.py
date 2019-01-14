import random
import math
import time
import requests
from collections import OrderedDict

#generate 6-digit number using time
def get6DigitNumber():
    t=int((time.time())%1000000)
    t=int(t%1000000)
    certNumLength=6
    range=math.pow(10, certNumLength)
    trim=math.pow(10, certNumLength-1)
    result=random.randint(0, t)+trim
    if (result>range):
        result=result-trim
    return int(result)
    
#url, appKeys, and type for calling REST API
url="https://api-sms.cloud.toast.com/sms/v2.1"
appKeys="/appKeys/{appkey}"    
type="/sender/auth/sms"

#define header, requestBody, and recipientList
header=OrderedDict()
requestBody=OrderedDict()
recipientList=OrderedDict()

#making a header
header["Content-Type"]="application/json;charset=UTF-8"

#making a requestBody
requestBody["body"]="Authorization Code is: ["+str(get6DigitNumber())+"]"
requestBody["sendNo"]=""
requestBody["senderGroupingKey"]="SenderGroupingKey"

#making a recipientList, and put this in the requestBody
recipientList["recipientNo"]=""
recipientList["recipientGroupingKey"]="RecipientGroupingKey"

requestBody["recipientList"]=[recipientList]

#call REST API, and get response
responseBody=requests.post(url+appKeys+type, headers=header, json=requestBody)

#print result
print(responseBody.text)