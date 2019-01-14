import urllib
import requests
from collections import OrderedDict
from json.encoder import JSONEncoder

#url, appKeys, and type for calling REST API
url="https://api-sms.cloud.toast.com/sms/v2.1"
appKeys="/appKeys/EGAHwbWtW692uzLs"    
type="/requests/attachFiles/authDocuments"

#define header, requestBody, and file
header=OrderedDict()
requestBody=OrderedDict()

#making a header
header["Content-Type"]="multipart/form-data;"

#making a requestBody
requestBody["attachFile"]="@\\"+"C:\\Users\\NHNEnt\\Desktop\\authTest.JPG\";type=image/jpeg;filename=\"authTest.JPG\""

#call REST API, and get response
responseBody=requests.post(url+appKeys+type, headers=header, json=requestBody)

#print result
print(responseBody.text)
