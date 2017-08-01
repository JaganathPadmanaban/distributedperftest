import paho.mqtt.client as mqtt
import requests
import Mosquitopublisher as pub
import threading
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("QUBE-GREETINGS-STATUS-ENGINE")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    if("OUT" not in msg.payload):
        while(True):
            hit = requests.get("https://jt-admin-staging.herokuapp.com/greetings/{0}".format(msg.payload),
                              headers={
                                  "Cookie": "_jtapp_session=bStJRVpaSkgyK21HQU1TY09jaW1QaDdwZmJDaFYyM1g3YTM4US8yWTJFOU1wWkdrZS9SUHc0RWhOWGpSdVNlc1BzcmJUYXBkNnFVTE1VVXF1K1NSdWFQSHBsMlNLRHRRS1JPMWlOWjczL1BMNHJKQmZyZjQxbUNXdDRveUw3L202STdVKzk1dmswY09LSC9hMVVtZ0V4eUhMREkxYUloa01sc0xhbkU4bXZPVjZLZlBvdWloYnNzeGF0QVdpbytjOVNjWGk1WVFac25Zd1dlYmlPeVJLY1dkR3ZVQjRFYWtmTTJFT2RCMHhpbz0tLUdwNURuVHJic2ZNTDJTNXlQWmE2eFE9PQ%3D%3D--6890f198adc8a4c602702ba78a77a4bcc4df4479"})
            if(hit.status_code <> "404"):
                pub.Publish(topic="QUBE-GREETINGS-STATUS-ENGINE", message="OUT:  "+ hit.content)
                break
            else:
                threading._sleep(5)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()