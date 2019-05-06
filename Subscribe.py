import paho.mqtt.client as mqtt
from Get_Data_to_DB import*

MQTT_Broker="localhost"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic ="home/sensors"

def on_connect(client, userdata, rc):
	if rc!=0:
		pass
		print ("Unable to connect to MQTT Broker..")
	else:
		print("Connected with MQTT Broker: " + str(MQTT_Broker))

def on_message(client,userdata,mgs):
	print ("MQTT Data Recevied ....")
	print ("MQTT Topic: "+mgs.topic)
	print ("Data: " + string(mgs.payload))
	Sensor(mgs.payload)

client = mqtt.Client()
client.username_pw_set(username="chung",password="123")
client.on_connect =on_connect
client.on_message = on_message
client.connect(MQTT_Broker,MQTT_Port,Keep_Alive_Interval)
client.loop_furever()
