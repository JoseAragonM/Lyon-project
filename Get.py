#!/usr/bin/python

#Copyright 2019 Google LLC WIRID-LAB and contributors

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#version 2 as published by the Free Software Foundation.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.

# WIRID LAB
# Author: Kevin Herney  https://github.com/kherney
# Contributors : Jose Rugeles, Edward Guillen, Juan C. Martinez
# Universidad Militar Nueva Granada
# Bogota D.C

# julio 2019 Editado para prueba en citi-lab por Jose Daniel Aragon

import time
import json
import paho.mqtt.client as mqtt
import base64

def on_connect(client, userdata, rc):
    print('Cliente conectado con {}'.format(rc))

def on_message(client, userdata, msg):
    print("Mensaje en ---> \n")
    print('Topic: {} \n\nContent :{}\n'.format(msg.topic, msg.payload))
    x = msg.payload.decode("utf-8")
    y = json.loads(x)
    z = y["payload_raw"]
    z = base64.b64decode(z).decode("utf-8")
    print ('datos: {}'.format(z)) 

while True:
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set("1401134001","ttn-account-v2.Y6-w7Z_UFAYbR5jhd3HmTsYwAbSHSV1KS3sO8DLhk5M")
    client.connect("eu.thethings.network",1883)
    client.subscribe("+/devices/+/up")
    client.loop_forever()
    time.sleep(1)