import binascii
import pycom
import machine
import socket
import json
from network import LoRa
import time
# Colors
off = 0x000000
red = 0xff0000
green = 0x00ff00
blue = 0x0000ff

# Turn off heartbeat LED
pycom.heartbeat(False)

# # Initialize LoRaWAN radio
# lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# # Set network keys
# app_eui = binascii.unhexlify('70B3D57ED002B821')
# app_key = binascii.unhexlify('BF2D68A0F3EB9A52633F93532D6C868E')

# # # Join the network
# lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
# pycom.rgbled(red)

# # Loop until joined
# while not lora.has_joined():
#     print('Not joined yet...')
    
#     pycom.rgbled(off)
#     time.sleep(0.1)
#     pycom.rgbled(red)
#     time.sleep(2)

# print('Joined')
# pycom.rgbled(blue)

# s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
# s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
# s.setblocking(True)


adc = machine.ADC()             # create an ADC object
audio_pin = adc.channel(pin='P19', attn=adc.ATTN_0DB)   # create an analog pin on P20 - look out for pin confusion
envelope_pin = adc.channel(pin='P18', attn=adc.ATTN_0DB)
gate_pin = adc.channel(pin='P17', attn=adc.ATTN_0DB)



while True:
    #value = '{ \"audio\":\'' + str(audio_pin.value()) + '\'}'
    #get sound detector values
    audio =audio_pin.value() 
    envelope = envelope_pin.value()
    gate = gate_pin.value()
    #concatenate them
    value = {"audio":audio,"envelope":envelope,"gate":gate}

#   timestamp = '{\"timestamp\":\"' + now + '\"}'
    payload = value
          
    #send them
    json_payload=json.dumps(payload)
    print(json_payload)
    # s.send(json_payload)
    time.sleep(0.5)     





  

