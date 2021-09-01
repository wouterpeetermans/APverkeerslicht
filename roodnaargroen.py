import paho.mqtt.client as mqtt
import time
import logging
logging.basicConfig(level=logging.DEBUG)
broker_address="mqtt.wouterpeetermans.com"
client = mqtt.Client("verkeerlicht-client") #create new instance
logger = logging.getLogger(__name__)
client.enable_logger(logger)
client.connect(broker_address, port=1884) #connect to broker
client.publish("cmnd/tasmota_BE639C/POWER3","ON")
client.publish("cmnd/tasmota_BE639C/POWER2","OFF")
client.publish("cmnd/tasmota_BE639C/POWER1","OFF")
time.sleep(3)
client.publish("cmnd/tasmota_BE639C/POWER2","ON")
time.sleep(1)
client.publish("cmnd/tasmota_BE639C/POWER1","ON")
client.publish("cmnd/tasmota_BE639C/POWER2","OFF")
client.publish("cmnd/tasmota_BE639C/POWER3","OFF")
