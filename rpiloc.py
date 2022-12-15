# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# the script is intended for UK sources, there are a lot of debug prints in here, so they
# can be removed if you are confident that the script is working.
# Next jobs. Have an LED light and a button to clear the alert..
#
#
import time
import requests
#import xml.etree.ElementTree as ET
import datetime
#import json

json_rpi = '[]'

intervaltimer = 65

def mid(s, offset, amount):
    return s[offset:offset + amount]

def build_json(array1,array2):
    json_rpi = '{\n"RPI":['
    z0 = array1
    z1 = array2
    loopx = 0
    loopa = len(array1) - 1
    maxloop = loopa
    while loopx <= loopa:
        json_rpi = json_rpi + '\n{"Location":"' + z0[loopx] + '" , '
        json_rpi = json_rpi + '"DateChanged":"' + z1[loopx] + '"}'
        if loopx<loopa:
            json_rpi = json_rpi + ','
        #print(z1[loopx])
        loopx = loopx + 1
    json_rpi = json_rpi + '\n]\n}'
    return json_rpi

def get_xml_elements(xml_text,element):
    #print('Lets find those elements')
    rpi_locations = []
    new_xml_text = xml_text
    new_element = '<' + element + '>'
    #print(new_element)
    new_element_end = '</' + element + '>'
    text = new_xml_text
    index = 0
    index_end = 0
    field_len = 0
    while index < len(text):
        index = text.find(new_element, index)
        index_end = text.find(new_element_end, index)
        if index == -1:
            break
        field_len = index_end - index - len(new_element)
        rpi_locations.append(mid(text,index + len(new_element),field_len))
        index += len(new_element)  # +2 because len('ll') == 2
    return rpi_locations


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    looper = 0
    last_check = ''
    requesturl = 'https://rpilocator.com/feed/?country=UK'
    print('STARTING PROCESS')
    while looper >= 0:
        print('timer value - ' + str(intervaltimer))
        print('Checking Website')
        getaurl = get_rpi_rss(requesturl)
        if getaurl == 'FAIL':
            print('FAIL !!! Something has gone horribly wrong')
        else:
            if looper == 0:
                print('FIRST TIME - Load the initial Data +')
                #print(getaurl)
                last_check = getaurl
            if last_check != getaurl:
                print('ALERT - SOMETHING HAS CHANGED')
                #print('Last Check')
                #print(last_check)
                #print('Current Values')
                #print(getaurl)
                #print('store the current date and time')
                last_check = getaurl
            else:
                print('Value has not changed')
                #print('current value' + getaurl)
                #print('previous value' + last_check)
            if looper == 0:
                looper = 1
        time.sleep(intervaltimer)


def get_rpi_rss(requesturl):
    x = requests.get(requesturl)
    current_details = ''
    if x.status_code == 200:
        #root = ET.fromstring(x.text)
        z0 = get_xml_elements(x.text, 'title')
        z1 = get_xml_elements(x.text, 'pubDate')
        z0.pop(0) # these are here because the XML has two extra titles that are not needed
        z0.pop(0)
        current_details = build_json(z0,z1)
        now = datetime.datetime.now()
        print("Current date and time : ")
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        print(current_details)
        return current_details
    else:
        print('Non 200 return code')
        print(x.status_code)
        print(x.text)
        return ('FAIL')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
