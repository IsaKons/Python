from urllib import request, parse
import sys

#Download page as object in var GET
myUrl = "http://www.google.com"

otvet = request.urlopen(myUrl)
mytext1 = otvet.readlines()

#mytext2 = otvet.read()
#print(mytext2)  #Выдать именно хтмл код

for line in mytext1:
    print(str(line).lstrip("b'").rstrip("\\r\\n'"))
    
    
#########################
#POST or how to send data
myUrl = "http://www.google.com/search?"
value = {'q': 'ANDESA Soft'}

myheader = {}
myheader['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

try:
    mydata = parse.urlencode(value)
    print(mydata)
    myUrl = myUrl + mydata
    req = request.Request(myUrl, headers=myheader)
    otvet = request.urlopen(req)
    otvet = otvet.readlines()
    for line in otvet:
        print(line)
except Exception:
    print("Error occuried during web request!!")
    print(sys.exc_info()[1])
    
######################
#Download file\files or as

myUrl = "http://adv400.tripod.com/kartinka.jpg"
myFile = "G:\\MyPython\\MyDownloads\\mykartinka.jpg"

try:
        print("Start Downloading file from: " + myUrl)
        request.urlretrieve(myUrl, myFile)
except Exception:
    print("AHTUNG!!!")
    print(sys.exc_info())
    exit

print("File Downloaded and saved at:" + myFile)