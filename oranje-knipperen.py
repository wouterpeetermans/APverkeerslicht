import paho.mqtt.client as mqtt
import time
broker_address="mqtt.wouterpeetermans.com"
client = mqtt.Client("verkeerlicht-client") #create new instance
client.connect(broker_address, port=1884) #connect to broker
client.publish("cmnd/tasmota_BE639C/POWER1","OFF")
client.publish("cmnd/tasmota_BE639C/POWER3","OFF")
while 1:
    client.publish("cmnd/tasmota_BE639C/POWER2","TOGGLE")
    time.sleep(0.75)
