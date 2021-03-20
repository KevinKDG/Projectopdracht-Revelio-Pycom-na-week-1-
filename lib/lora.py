from network import LoRa
import socket
import time
import ubinascii
import ustruct
from ultrasoon import *

Europe = LoRa.EU868
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# Fill in your correct keys
app_eui = ubinascii.unhexlify('70B3D57ED003E9D9') # App EUI
app_key = ubinascii.unhexlify('EB40EE167D05F35EF01D866802C758C3') # App key
dev_eui = ubinascii.unhexlify('70B3D57ED003E9D9') # Dev EUI

def getlora():
    lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)
    packet = ustruct.pack('f',3.33)

    while not lora.has_joined():
        time.sleep(2.5)
        print('Not yet joined...')

    print('Joined')

def senddata():
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    s.setblocking(True)
    meting = readsensor()
    s.send(bytes(distance))
    s.send(packet)

    s.setblocking(False)

    data = s.recv(64)
    return(data)
