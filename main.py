#imports
import wifi
from ultrasoon import *
import time
import urequests as requests
import lora

#Adafruit.io information
aio_key = "aio_rVhK25ikrhyPryBR4XIjFwYBaVch"
username = "kevinkdg"
feed_name = "ultrasoon"

#Uncomment for WiFi connection
wifi.wificonnect('WiFi-2.4-133B', '24652CC8A4') # ssid , password

#Uncomment for lora connection
#lora.getlora()

#Connect with adafruit.io
while True:
    # uncomment for lora
    #lora.senddata

    # uncomment for wifi
    afstand = readsensor()

    url = 'https://io.adafruit.com/api/v2/' + username + '/feeds/' + feed_name + '/data'
    body = {'value': afstand}
    headers = {'X-AIO-Key': aio_key, 'Content-Type': 'application/json'}
    try:
        r = requests.post(url, json=body, headers=headers)
        print(r.text)
        r.close()

    except Exception as e:
        print(e)
    time.sleep(10)
