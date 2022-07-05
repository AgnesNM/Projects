# 7. How to Subscribe to Topics

Back to our Richard hot air balloon example.

Each subscriber would need to subscribe to the *sensors/sensornumber/altitude* topic to receive information on the hot air balloon’s altitude.

The following python mqtt example shows a sample script to to subscribe to topics:

![subscriber script](/Eclipse_Paho/Subscriber%20Script.png)

You can also find the script here: [publisher script](/subscriber.py) 

- We would need to import the mqtt paho client.

- And the sys module.

- Create a function that will be called every time the client receives a message from the broker.

- The function takes 3 arguments: a client instance, user data (authentication and authorization information), and the message.

- The function’s output is the topic and the message's payload received from the broker. The payload needs to be decoded.

- Create an object from the mqtt paho.client class.

- Set the callback function.

- Connect to our mqtt program using the connect method. The arguments in the connect method are:
_
    - name of the pc (this would be replaced by the name of the Raspberry Pi)
    - port number - the default mqtt broker port, 1883 (this would be replaced by the Raspberry Pi port)
    - timeout variable in seconds

- Check whether the connection to the broker was successful. It should return zero.

    - if successful, publish message
    - exit

- The subscribe method takes one argument: the topic it wants to
- Disconnect the publisher from the broker

- Once we have the script, we need to ensure that our Mosquitto Broker is running. 

         sudo service mosquitto status

![mosquitto broker status](/Eclipse_Paho/broker%203.png)

- Mosquitto starts automatically after installation. We can stop it by 

         sudo service  mosquitto stop

- We can then restart it in the folder containing our mqtt client script.

         mosquitto -v

- On our terminal, run the script:

         python3 subscriber.py

![mosquitto broker restart](/Eclipse_Paho/subscriber.png)

- The broker starts and runs on port 1883. The broker sends a CONNACK control packet showing that it is successfully connected to the client (we can assume that this is our Raspberry Pi in this case)

- We can also see that we are now subscribed to the topic *sensors/sensor01/altitude* with our QoS as zero.

- The PINGREQ and PINGRES control packet show us that the server/connection is still alive.

- ‘Press Ctrl+C to exit’ should be printed on the console. 

- The last line in our script, **client.disconnect()** will disconnect the publisher from the broker.


# 8. [How to Disconnect from the Broker](/Eclipse_Paho/08_how_to_disconnect_from_the_broker.md)