import requests
import base64
from collections import OrderedDict

def encodeFileByBase64(filePath):
    fp=open(filePath, "rb")
    data=fp.read()
    fp.close()
    return base64.standard_b64encode(data)

#url, appKeys, and type for calling REST API
url="https://api-sms.cloud.toast.com/sms/v2.1"
appKeys="/appKeys/{appkey}"    
type="/attachfile/binaryUpload"

#define header, requestBody, and recipientList
header=OrderedDict()
requestBody=OrderedDict()
recipientList=OrderedDict()

#making a header
header["Content-Type"]="application/json;charset=UTF-8"

#making a requestBody
filePath="C:\\.."
requestBody["fileName"]="testFile.jpg"
requestBody["createUser"]=""
requestBody["fileBody"]=encodeFileByBase64(filePath).decode('UTF-8')

#call REST API, and get response
responseBody=requests.post(url+appKeys+type, headers=header, json=requestBody)

#print result
print(responseBody.text)
