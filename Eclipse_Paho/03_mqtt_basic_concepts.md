# 3. MQTT Basic Concepts

It’s important to understand some MQTT basic concepts before you begin working with the paho mqtt examples. Let’s delve into them below:

**The Publish-Subscribe Pattern/Model**

It is also known as the pub-sub pattern. There are several devices that exchange data in this model which we will look at shortly.

In the pub-sub model, a publisher sends out messages to subscribers that have ‘subscribed’ to a particular topic.

The pub-sub model is decoupled (the publisher is not aware of the presence of the recipient subscribers).

**The Broker**

The broker or server is at the heart of the pub-sub model. It is the server equivalent in the HTTP/HTTPS protocol. All clients must connect to the server.

The broker filters all incoming messages and sends them out to the subscribers who have subscribed to specific topics. 

**The Publisher**

The publisher is an MQTT client who sends messages to the broker for distribution to the subscribers. 

**The Subscriber**

The subscriber is an MQTT client who receives messages from the broker for topics they are subscribed to.

Note:
- Both publishers and subscribers need to establish a connection with the broker.
- Sometimes an MQTT client can be both a publisher and a subscriber. For example, when a subscriber receives a message, it could send out a message to confirm the message’s receipt.This way, it becomes both a publisher and subscriber.

**Topic**

It is also known as a channel or subject. This is the area of interest that the subscriber subscribed to.

**A Pub-Sub Pattern Demonstration**

I will use a story from Richard Branson’s book, “Screw It, Let's Do It: Lessons in Life” to illustrate the pub-sub model.

In the book, Richard and his friend Per went on several hot air balloon adventures. They needed to know their altitude so as not to fly too high as to lack oxygen or too low so as to crash. 

They used an altitude sensor (let’s call it sensor 1). For the sake of our demonstration, let’s assume that the altitude sensor had a Raspberry Pi 3 board.

The Raspberry Pi 3 board in the sensor will send out altitude information to various people:

- Richard and Per 
- Air Traffic Control (in case of a crash)
- Maritime Patrol (in case of a crash)
- News station (in case of a crash)

The following diagram might make things even clearer:

![The publish-subscribe model](/Eclipse%20_Paho/pub-sub.png "Image source: “MQTT Essentials - A Lightweight IoT Protocol” by Gaston C. Hillar")

The altitude sensor with the Raspberry Pi 3 board is the publisher (sensor1). It sends out messages to subscribers which could be anything from an Android tablet or iOS smartphone to a walkie-talkie in Richard’s or Per’s hand.

For the subscriber to receive information about the altitude, however, they need to have subscribed to the topic. In our example, the topic is ‘sensor1/altitude’.

The broker will receive the message and topic from the publisher and only send it to the subscribers subscribed to the ‘sensor1/altitude’ topic.

The news station will not receive the message because it is not subscribed to the ‘sensor1/altitude’ topic. The flying is a private event. The news station could be subscribed to another topic though, ‘sensor1/emergency’, and would only receive a message if there was an accident and Richard and Per’s flying had been made known to the public.

With that out of the way, then it will be easier for us to work with the MQTT protocol and the Paho Python MQTT Client.

# 4. [How to Install the Python MQTT Client](/Eclipse%20_Paho/04_how_to_install_the_python_%20mqtt_client.md)
