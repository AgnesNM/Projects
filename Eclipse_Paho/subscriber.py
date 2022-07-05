import paho.mqtt.client as paho
import sys

#create a function that will be called every time the client receives a message 
#from the broker.
#the function takes 3 arguments: a client instance, user data (authentication and authorization information), 
#and the message
#the functions output is the topic and the message's payload, received from the broker. The payload needs to be decoded


def onMessage(client, userdata, msg):
    print(f"{msg.topic} : {msg.payload.decode()}") 

client = paho.Client()

#set the callback function

client.on_message = onMessage

#check whether the connection to the broker was successful, should return zero
#if successful, broker message should be received by the subscriber
#the subscribe method takes in one argument: the topic it wants to subscribe to
#disconnect the publisher from the broker

if client.connect("localhost", 1883, 60) != 0:
    print("Could not connect to MQTT Broker!")
    sys.exit(-1)

client.subscribe("board/boardnumber/altitude")

#print an exit message
# create an endless loop to handle all the clients requests and responses

try:
    print("Press Ctrl+C to exit")
    client.loop_forever()

except:
    print("Disconnecting from broker")

client.disconnect()    
