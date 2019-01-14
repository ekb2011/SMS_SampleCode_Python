import urllib
import requests
from collections import OrderedDict

#url, appKeys, type, and query for calling REST API
url="https://api-sms.cloud.toast.com/sms/v2.1"
appKeys="/appKeys/{appkey}"    
type="/tag-sender"
query="/{requestId}?recipientNum={recipientNum}"

#set time for getting results
startUpdateDate="2018-12-20"
endUpdateDate="2018-12-20"
encoded_startRequestDate=urllib.parse.quote_plus(startUpdateDate)
encoded_endRequestDate=urllib.parse.quote_plus(endUpdateDate)

#define header, requestBody
header=OrderedDict()
requestBody=OrderedDict()

#making a header
header["Content-Type"]="application/json;charset=UTF-8"

#call REST API, and get response
responseBody=requests.get(url+appKeys+type+query+"&startRequestDate="+encoded_startRequestDate+"&endRequestDate="+encoded_endRequestDate, headers=header)

#print result
print(responseBody.text)