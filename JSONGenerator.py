from bs4 import BeautifulSoup
import requests
import pprint
import re
import json
import urllib
import urllib2
import time

now = 1439769600
thyme = int(time.time())
since = int((thyme - 0.7 * 60 * 1000))

user = '2158538297492446'
access_token = 'EAAILXL42YO4BAJs8tDbbeEwYPqHTFdkJ4qAZBc4fr9Q8KNQACMQlajg6Kb2ZBKP7jQdPCBEDgdbZAmfjCOEIEVZCl1MN2zCITZBVbZAzbZAOuXU0zukrj12fuf64SHIuVQuRxqOWZBdMNfWZC6KVmRL7YBt0d3Toapl9CZCH6DUChNehFRqTzijU1Lm6Hw3CBZAGAuzyRh1JaXlZAAZDZD'
url = 'https://graph.facebook.com/' + user + '?fields=feed{message}&access_token=' + access_token
htmlContent = requests.get(url, verify=False)
data = htmlContent.text
print("data",data)

json_file = open('outputfile.json','w')
json_file.write(data)
json_file.close()