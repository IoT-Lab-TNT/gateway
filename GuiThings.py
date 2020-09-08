import time
import sys
import paho.mqtt.client as mqtt
import json
import random
 
THINGSBOARD_HOST = 'tntholdings.ddns.net'
 
ACCESS_TOKEN = 'zGIUoZ1SM5NbZ4nbn0mK'
 
sensor_data = {'temperature': 0}
 
minA = 10 
maxA = 70
 
client = mqtt.Client()
 
 
client.username_pw_set(ACCESS_TOKEN)
 
client.connect(THINGSBOARD_HOST, 1883)
 
client.loop_start()
 
try:
	while True:
		temperature = random.randrange(minA,maxA)
		print("temperature:{:g}".format(temperature))
		sensor_data['temperature'] = temperature
		client.publish('v1/devices/me/telemetry',json.dumps(sensor_data))
		time.sleep(10)
except KeyboardInterrupt:
    pass
client.loop_stop()
client.disconnect()