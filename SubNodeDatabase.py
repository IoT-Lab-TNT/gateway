import paho.mqtt.client as mqtt
import json
import mysql.connector

THINGSBOARD_HOST = 'tntholdings.ddns.net'
ACCESS_TOKEN = 'GatewayF20_Token'



def on_connect(client, userdata, rc, *extra_params):
    client.subscribe('v1/devices/me/rpc/request/+')


def on_message(client, userdata, msg):
    print ('Topic: ' + msg.topic + '\nMessage: ' + str(msg.payload))
    data = json.loads(msg.payload)
    data2 = json.loads(data['params'])

    if data['method'] == 'InsertDevice':
        con =  ConnectToMysql ('localhost', 'trung', 'raspberry', 'TNTHOLDINGS')
        print ("Connected!")
        for x in data2:
            print (CheckExistsDevice (con, x['deviceId']))
           # InsertDeviceToMysql (con, x['deviceId'], x['deviceName'], x['deviceLocation'], x['chanelId'])
        print ("Inserted!")

def ConnectToMysql (host, userName, password, dataBase):
    myconn = mysql.connector.connect(host = host, user = userName, password = password, database = dataBase)
    print ("Database connected!")
    return myconn

def InsertDeviceToMysql (sqlConnector, deviceId, deviceName, deviceLocation, chanelId):
    cursor = sqlConnector.cursor()
    insertDeviceSQL = "INSERT INTO device (deviceId, deviceName, deviceLocation, chanelId) VALUES (%s, %s, %s, %s)"
    cursor.execute(insertDeviceSQL, (deviceId, deviceName, deviceLocation, chanelId))
    sqlConnector.commit()
    #sqlConnector.close()

def CheckExistsDevice (sqlConnector, deviceId):
    check = False
    cursor = sqlConnector.cursor(buffered=True)
    print (deviceId, type(deviceId))
    SQL = "SELECT COUNT(1) FROM device WHERE deviceId = %s"
    id = (deviceId,)
    cursor.execute(SQL, id)
    sqlConnector.commit()
    if cursor.fetchone()[0]:
        check = True
    return check
    
#############################################################################################################################################################################
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883, 60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    client.disconnect()
