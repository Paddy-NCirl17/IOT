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

dht_sensor_port = 7
dht_sensor_type = 0
buzzer = 8
button = 3
reset = 0

grovepi.pinMode(buzzer,"OUTPUT")
grovepi.pinMode(button,"INPUT")

while True:
    try:
        # get the temperature and Humidity from the DHT sensor
        [ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)
        button_sensor = grovepi.digitalRead(button)
        print(grovepi.digitalRead(button))
        print("temp =", temp,)
        if temp > 23 and reset !=1:
           if button_sensor ==1:
            reset = 1
           else:
            grovepi.digitalWrite(buzzer,1)
            time.sleep(1)
            grovepi.digitalWrite(buzzer,0)
            time.sleep(1)
    except KeyboardInterrupt:
        grovepi.digitalWrite(buzzer,0)
        break
    except IOError:
        print ("Error")        