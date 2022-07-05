import paho.mqtt.client as paho
import sys

#create an object from the paho.client class

client = paho.Client()

#connect to our mqtt program
#arguments in the connect method
##name of the pc
##port number - the default mqtt broker port, 1883
##timeout variable in seconds

#check whether the connection to the broker was successful, should return zero
#if successful, publish message
#the publish method takes in the arguments: topic, message, and QoS (Quality of Service)
#disconnect the publisher from the broker


if client.connect("localhost", 1883, 60) != 0:
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)

client.publish("sensors/sensor01/altitude", "Hello World from paho-mqtt!", 0)

client.disconnect()