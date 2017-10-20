
import subprocess
import Mosquitopublisher as pub
import socket
import paho.mqtt.client as mqtt



# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("QUBE-PERFTEST-TRIGGER")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    if ("OUT" in msg.payload):
        pass
    elif ("start-dynos:" in msg.payload):
        scale=msg.payload.split(':')[1]
        for i in range(0,int(scale)):
            xx=subprocess.check_output(["heroku","scale","--app",str(nodes[i]),"worker=1"])
        pub.Publish(topic='QUBE-PERFTEST-TRIGGER', message='OUT: Dynos started successfully!!')
    elif ("stop-dynos" in msg.payload):

        for i in range(0,len(nodes)):
            yy=subprocess.check_output(["heroku", "scale", "--app", str(nodes[i]), "worker=0"])
        pub.Publish(topic='QUBE-PERFTEST-TRIGGER', message='OUT: Dynos stopped successfully!!')
    elif ("who?" in msg.payload):
        pub.Publish(topic='QUBE-PERFTEST-TRIGGER',message='OUT: I the DynoManger is online!!')



x= subprocess.check_output(["heroku", "apps"])
outarray= x.split('\n')
global nodes
nodes = []
for item in outarray:
    if("node" in item):
        nodes.append(item)

print nodes
print len(nodes)

for i in range(0, len(nodes)):
    print nodes[i]

pub.Publish(topic='QUBE-PERFTEST-TRIGGER',message='OUT: QUBE Perf-test Dyno Manager is up and running')
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()




