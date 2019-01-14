import urllib
import requests
from collections import OrderedDict

#url, appKeys, type, and query for calling REST API
url="https://api-sms.cloud.toast.com/sms/v2.1"
appKeys="/appKeys/{appkey}"    
type="/statistics/view"
query="?searchType=DATE"

#set time for getting results
fromDate="2018-12-20"
toDate="2018-12-20"
fromTime="00:00"
toTime="10:40"

#encode time data for URL query
encoded_from=urllib.parse.quote_plus(fromDate+' '+fromTime)
encoded_to=urllib.parse.quote_plus(toDate+' '+toTime)

#define header
header=OrderedDict()

#making a header
header["Content-Type"]="application/json;charset=UTF-8"

#call REST API, and get response
responseBody=requests.get(url+appKeys+type+query+"&from="+encoded_from+"&to="+encoded_to, headers=header)

#print result
print(responseBody.text)