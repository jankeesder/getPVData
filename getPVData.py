#!/usr/bin/python

import urllib, urllib2, hashlib, re, requests
from xml.etree import ElementTree as ET
from requests.auth import HTTPBasicAuth

#config
username          = 'admin' #your inverter webpage username
password          = 'admin' #your inverter webpage password
inverterIP        = 'xxx.xxxx.xxx.xxx' #inverter ip address

#domoticz settings
domoticz_host         = 'xxx.xxxx.xxx.xxx' #domoticz ip address
domoticz_port         = '80'
domoticz_url          = 'json.htm'
domoticz_ActualPower   = 'xxx' # PV Device id domoticz

# Process html response
def processResponse(resp, strToken, strNextToken):
        #parse response and get values
        strTokenLen = len(strToken)
        valueIndexToken = resp.find(strToken)
        valueIndexNextToken = resp.find(strNextToken)
        value = re.sub('[ =";]', '', resp[valueIndexToken+strTokenLen:valueIndexNextToken-5])
        #print retreved values
        return value

#fetch site from url
url     = 'http://' + inverterIP + '/status.html'

try:
        res = requests.get(url,auth=HTTPBasicAuth(username, password))
        res.raise_for_status()
except requests.exceptions.HTTPError as err:
        print err
        sys.exit(1)


#gather values
inverter = processResponse(res.content, 'webdata_pv_type', 'webdata_rate_p')
totalToday = processResponse(res.content, 'webdata_today_e', 'webdata_total_e')
totalOveral = processResponse(res.content, 'webdata_total_e', 'webdata_alarm')
now = processResponse(res.content, 'webdata_now_p', 'webdata_today_e')
multiply='1000.0'
etotal1000 = float(totalOveral) * float(multiply)
strTotalOveral=str(etotal1000)

#print to console
print('Success! Connected...')
print 'Inverter: ' + inverter
print 'Total overal: ' + totalOveral
print 'Total today: ' + totalToday
print 'Current: ' + now

#uploading values to domoticz
url = ("http://" + domoticz_host + ":" + domoticz_port + "/" + domoticz_url+ "?type=command&param=udevice&idx=" + domoticz_ActualPower+ "&nvalue=0&svalue=" + now + ";" + strTotalOveral)
urllib.urlopen(url)
