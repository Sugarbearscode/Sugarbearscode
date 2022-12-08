# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# the script is intended for UK sources, there are a lot of debug prints in here, so they
# can be removed if you are confident that the script is working.
# Next jobs. Have an LED light and a button to clear the alert.. 
#
#

import requests
import xml.etree.ElementTree as ET
import time
intervaltimer = 65

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    looper = 0
    last_check=''
    requesturl='https://rpilocator.com/feed/?country=UK'
    print('Starting')
    while looper >= 0:
        print('timer' + str(intervaltimer))
        print('Checking Website')
        getaurl = get_rpi_rss(requesturl)
        if getaurl == 'FAIL':
            print('Something has gone horribly wrong')
        else:
            if looper == 0:
                print('First Time - Load the initial Data Time +' + getaurl)
                last_check = getaurl
            if last_check != getaurl:
                print('Alert - it has changed')
                print('Last Check = '+ last_check)
                print('Current check =' + getaurl)
                print('store the current date and time' + getaurl)
                last_check = getaurl
            else:
                print('Value has not changed')
                print('current value' + getaurl)
                print('previous value' + last_check)
            if looper==0:
                looper = 1
        time.sleep(intervaltimer)

def get_rpi_rss(requesturl):
    x = requests.get(requesturl)
    if x.status_code == 200:
        root = ET.fromstring(x.text)
        print(root[0][3].text)
        return(root[0][3].text)
    else:
        print('Non 200 return code')
        print(x.status_code)
        print(x.text)
        return('FAIL')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

