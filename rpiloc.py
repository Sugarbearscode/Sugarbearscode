## this is a really simple script for my raspberry pi which will run to 
## altert of stock changes. Pulls in an XML every minute and then
## checks to see if the timestamp has changed. 

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import xml.etree.ElementTree as ET
import time

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    looper = 0
    last_check=''
    requesturl='https://rpilocator.com/feed/?country=UK'
    print('Starting')
    while looper >= 0:
        time.sleep(61)
        print('Checking Website')
        getaurl = get_rpi_rss(requesturl)
        if getaurl == 'FAIL':
            print('Something has gone horribly wrong')
        else:
            if looper == 0:
                last_check = getaurl
            if last_check != getaurl:
                print('Alert - it has changed')
                print(gerurl)
                last_check = geraurl
            if looper==0:
                looper = 1

def get_rpi_rss(requesturl):
    x = requests.get(requesturl)
    if x.status_code == 200:
        root = ET.fromstring(x.text)
        return(root[0][3].text)
    else:
        return('FAIL')
    
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
