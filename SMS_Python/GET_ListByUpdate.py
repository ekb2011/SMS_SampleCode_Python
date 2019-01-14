import urllib
import requests
from collections import OrderedDict

#url, appKeys, type, requestId, and query for calling REST API
url="https://api-sms.cloud.toast.com/sms/v2.1"
appKeys="/appKeys/{appkey}"    
type="/message-results"

#set time for getting results
startUpdateDate="2018-12-20"
endUpdateDate="2018-12-20"
startTime="00:00:00"
endTime="10:40:00"

#encode time data for URL query
encoded_startUpdateDate=urllib.parse.quote_plus(startUpdateDate+' '+startTime)
encoded_endUpdatedDate=urllib.parse.quote_plus(endUpdateDate+' '+endTime)

#define header
header=OrderedDict()

#making a header
header["Content-Type"]="application/json;charset=UTF-8"

#call REST API, and get response
responseBody=requests.get(url+appKeys+type+"?startUpdateDate="+encoded_startUpdateDate+"&endUpdateDate="+encoded_endUpdatedDate, headers=header)

#print result
print(responseBody.text)