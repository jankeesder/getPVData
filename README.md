# getPVData
Retreve data from Omnik inverter and send to Domoticz

This script retreves values from the Omnik inverter website and send them to Domoticz

Usage:
1 - Copy the getPVData.py file to the scripts directory of Domoticz

2 - Correct the following values in getPVData.py:
    
    username
    password
    inverterIP
    domoticz_host
    domoticz_port
    domoticz_url
    domoticz_ActualPower

3 - Create crontab entry:
    */5 * * * * /usr/bin/python /home/<##USERNAME##>/domoticz/scripts/getPVData.py
