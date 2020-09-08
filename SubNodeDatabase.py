import paho.mqtt.client as mqtt
import json
import random
from time import sleep
from Insert import Sensors

# MQTT setting
MQTT_Broker = "192.168.1.244"
MQTT_Port = 1883
Keep_Alive_Interval = 7200
MQTT_Topic = 'thean'

sw_data = {}
# Callback server

def on_connect(client, userdata, flags, rc):
    if rc != 0:
        pass
    else:
        print("Connected! ")
    print("Connection returned result: " + str(MQTT_Broker))
    mqttc.subscribe(MQTT_Topic, qos = 1)
    print("da subscribe")

# Callback on_message server
def on_message(client, userdata, msg):
    Sensors(msg.payload) 
    print("Message Recieved from tang 20: "+msg.payload.decode())

    

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
#mqttc.username_pw_set(username = "thean", password = "qdLpQewK")
mqttc.connect(MQTT_Broker, MQTT_Port, Keep_Alive_Interval)
mqttc.loop_forever()
