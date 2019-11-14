'''
The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2017  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''
from grovepi import *
import grovepi
import time
from time import gmtime, strftime
import dweepy
import json
import database as d

dht_sensor_port = 7
dht_sensor_type = 0
buzzer = 8
button = 3
ultrasonic_ranger = 2
sound_sensor = 1
r_led = 4
b_led = 6
alarm = ""
door = ""
reset = 0
roomNoise = ""
threshold_value = 400

pinMode(buzzer,"OUTPUT")
pinMode(button,"INPUT")
pinMode(r_led,"OUTPUT")
pinMode(b_led,"OUTPUT")
pinMode(sound_sensor,"INPUT")



while True:
    try:
        fireAlarm ={}
        # get the temperature and Humidity from the DHT sensor
        [ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)
        button_sensor = grovepi.digitalRead(button)
        fireDoor = grovepi.ultrasonicRead(ultrasonic_ranger)
        timeStamp = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
        sensor_value = grovepi.analogRead(sound_sensor)
        
        
        if fireDoor > 5:
           door = "Firedoor is open"
           print ("Firedoor is open")
           
        else:
           door = "Firedoor closed"
           print ("Firedoor closed")
           print ("Door",fireDoor)
           
        if sensor_value > threshold_value:
            grovepi.digitalWrite(b_led,1)
            roomNoise = "Room Occupied"
            print("Noise = %d" %sensor_value)
        else:
           grovepi.digitalWrite(b_led,0)
           roomNoise = "Room UnOccupied"
           print("Noise = %d" %sensor_value)
           
        if temp > 23 and reset !=1:
            alarm = "Alarm is active"
            print("alarm",alarm)
            print("temp",temp)
            digitalWrite(r_led,1)
            grovepi.digitalWrite(buzzer,1)
            time.sleep(1)
            digitalWrite(r_led,0)
            grovepi.digitalWrite(buzzer,0)
            time.sleep(1)
                     
            
        else:
         alarm = "Alarm is not active"
         print(alarm)

        if button_sensor ==1:
         reset = 1
         digitalWrite(r_led,0)
         grovepi.digitalWrite(buzzer,0)

        fireAlarm["Alarm"] = alarm
        fireAlarm["Firedoor"] = door
        fireAlarm["Temperature"] = temp
        fireAlarm["Time"] = timeStamp
        fireAlarm["Noise"] = roomNoise
        fireAlarm["Reset"] = reset
        

        with open('room_data.json') as file:
            json_data = json.loads(file.read())
            fire_ID = json_data['fire_ID']
            fireAlarm['location'] = json_data['location']
            
        dweepy.dweet_for(fire_ID,fireAlarm)
        
        mongo_insert = d.insert_into(fireAlarm)
       
        
    except KeyboardInterrupt:
        grovepi.digitalWrite(buzzer,0)
        break
    except IOError:
        print ("Error")        