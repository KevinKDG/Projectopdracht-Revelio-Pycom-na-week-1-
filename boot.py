import pycom
from network import WLAN
import machine
import time

# ---- Config ----

wlan = WLAN(mode=WLAN.STA)
pycom.heartbeat(False)
wlan.connect(ssid='ssid', auth=(WLAN.WPA2, 'password!'))

# ---- Loop ----

while not wlan.isconnected():
    time.sleep(2)
    pycom.rgbled(0xFF0000)
    print("no connection")
    machine.idle()

while wlan.isconnected():
    print("WiFi connected succesfully")
    time.sleep(1)
    print(wlan.ifconfig())
    pycom.rgbled(0x00FF00)
