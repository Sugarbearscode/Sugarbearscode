## this is a really simple script for my raspberry pi which will run to 
## altert of stock changes. Pulls in an XML every minute and then
## checks to see if the timestamp has changed. 

import requests
import xml.etree.ElementTree as ET
import time
looper = 0
last_check=''
requesturl='https://rpilocator.com/feed/?country=UK'

def get_rpi_rss(requesturl):
   x = requests.get(requesturl)
   if x.status_code == 200:
      root = ET.fromstring(x.text)
      return(root[0][3].text)   
   else:
      return("FAIL") 

do while looper>=0
   time.sleep(61)
   getaurl = get_rpi_rss(requesturl)
   if getaurl = 'FAIL':
      print('Something has gone horribly wrong')
   else:
      if looper == 0:
          last_check = getaurl
      if lastcheck!=getaurl:
          print('Alert - it has changed)
