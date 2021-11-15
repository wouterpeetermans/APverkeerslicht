import paho.mqtt.client as mqtt
import time
broker_address="mqtt.wouterpeetermans.com"
client = mqtt.Client("verkeerlicht-client") #create new instance
client.connect(broker_address, port=1884) #connect to broker
client.publish("cmnd/tasmota_BE639C/POWER3","OFF")
client.publish("cmnd/tasmota_BE639C/POWER2","OFF")
client.publish("cmnd/tasmota_BE639C/POWER1","ON")
time.sleep(3)
client.publish("cmnd/tasmota_BE639C/POWER2","ON")
client.publish("cmnd/tasmota_BE639C/POWER1","OFF")
time.sleep(1)
client2 = mqtt.Client("verkeerlicht-client2", transport="tcp")
client2.connect(broker_address, port=1884)
client2.publish("cmnd/tasmota_BE639C/POWER3","ON")
client2.publish("cmnd/tasmota_BE639C/POWER2","OFF")
