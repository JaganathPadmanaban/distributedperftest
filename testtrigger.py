import paho.mqtt.client as mqtt
import subprocess
import Mosquitopublisher as pub
import socket


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("QUBE-PERFTEST-TRIGGER")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if("OUT" in msg.payload):
        pass
    elif("start test" in msg.payload):
        project= msg.payload.split('>')[1]
        pub.Publish(topic='QUBE-PERFTEST-TRIGGER', message="OUT: starting test run from node: {0}".format(socket.gethostname()))
        print("starting process node!")
        print(subprocess.call(["multimech-run",project]))
        pub.Publish(topic='QUBE-PERFTEST-TRIGGER',
                    message="OUT: Test run comepleted by node: {0}".format(socket.gethostname()))
        print('Test Over!!')
    elif("who?" in msg.payload):

        pub.Publish('QUBE-PERFTEST-TRIGGER',
                    message="OUT: Node {0} is up and awaiting command".format(socket.gethostname()))





pub.Publish('QUBE-PERFTEST-TRIGGER',message="OUT: Node {0} is online and awaiting command".format(socket.gethostname()))
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

