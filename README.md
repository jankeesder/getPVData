# getPVData
Retreve data from Omnik inverter and send to Domoticz

This script retreves values from the Omnik inverter website and send them to Domoticz. 

It is tested on Omnik3000tl with firmware V4.08Build215 (main) / V4.12Build246 (slave)



Usage:

1 - In Domoticz, create virtual sensor of type "Usage (Electric)"

2 - Copy the getPVData.py file to the scripts directory of Domoticz

3 - Correct the following values in getPVData.py:
    
    username                <-- username of the inverter device. Default is admin
    password                <-- password of the inverter device. Default is admin
    inverterIP              <-- ip address of the inverter
    domoticz_host           <-- ip address of the Domoticz device
    domoticz_port           <-- port of the Domoticz website
    domoticz_ActualPower    <-- virtual device id of the sensor in Domoticz

4 - Create crontab entry:
    */5 * * * * /usr/bin/python /home/<##USERNAME##>/domoticz/scripts/getPVData.py
