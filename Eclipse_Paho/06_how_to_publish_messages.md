# 6. How to Publish Messages

Remember our Richard hot air balloon example? We are going to use it here to help us understand how message subscription and publishing would work.

Imagine that on the day that Richard and Per went on their adventure, two other groups were taking two other different routes. We would now have three Raspberry Pi 3 boards in the 3 altitude sensors in each hot air balloon.

Each sensor will need to publish its altitude for every topic to the topic: sensors/sensornumber/altitude

The sensor number will be replaced by the specific sensor number, for example, sensor01, so sensor one’s topic would be *sensors/sensor01/altitude*

The following python mqtt example shows a sample script to send out messages via the sensor:

![publisher screenshot](/Eclipse_Paho/Publisher%20Screenshot.png)

You can also find the script here: [publisher script](/publisher.py) 


- We would need to import the mqtt paho client.

- And the sys module.

- Then create an object from the mqtt paho.client class.

- Connect to our mqtt program using the connect method. The arguments in the connect method are:
_
    - name of the pc (this would be replaced by the name of the Raspberry Pi)
    - port number - the default mqtt broker port, 1883 (this would be replaced by the Raspberry Pi port)
    - timeout variable in seconds

- Check whether the connection to the broker was successful. It should return zero.

    - if successful, publish message
    - exit

- The publish method takes in the arguments: topic, message, and QoS (Quality of Service)
- Disconnect the publisher from the broker

- Once we have the script, we need to ensure that our Mosquitto Broker is running. 

        *sudo service mosquitto status*

![mosquitto broker status](/Eclipse_Paho/broker%203.png)

- Mosquitto starts automatically after installation. We can stop it by 
        *sudo service  mosquitto stop*

- We can then restart it in the folder containing our mqtt client script.
        *mosquitto -v*

- Once we are sure that our broker is running, enter the following subscriber client command
        *mosquitto_sub -t sensors/sensor01/altitude*

- On our terminal, run the script:
        *python3 publisher.py*


![mosquitto broker restart](/Eclipse_Paho/publisher1.png)

The broker starts and runs on port 1883. The broker sends a CONNACK control packet showing that it is successfully connected to the client (we can assume that this is our Raspberry Pi in this case)

We can also see that our topic *sensors/sensor01/altitude* is published with our QoS as zero.
The PINGREQ and PINGRES control packet show us that the server/connection is still alive.

![run publisher script](/Eclipse_Paho/Hello%20World%20Publisher.png)

*Hello World from paho-mqtt* should be printed on the console. 

The last line in our script, client.disconnect() will disconnect the publisher from the broker.

# 7. [How to Subscribe to Topics](/Eclipse_Paho/07_how_to_subscribe_to_topics.md)








