# 1. The Eclipse Paho Project

The Eclipse Paho project is one of the implementations of the MQTT protocol by the Eclipse Foundation (the organization behind popular open-source tools like the Eclipse IDE, and Jarkata EE)

The Eclipse Paho project uses different programming languages in its implementations, ranging from Python, Java, Javascript, Golang, C, C++, and Rust.

Our focus will be on MQTT’s Python implementation.

### The Eclipse Paho MQTT Python Client Library

Eclipse Paho Client is a library that works with the MQTT publish-subscribe model to ensure that MQTT clients publish messages smoothly. It does this via helper functions and a client class. Supported MQTT versions include 5.0, 3.1.1, and 3.1

### Paho MQTT Python Client Library Features

What features make the Paho MQTT Python Client a great option?

**Last Will and Testament Messages (LWT)**

For an MQTT client to connect to an MQTT broker, it needs to send a connection request. The connection request contains a CONNECT control packet with information that the broker will use for authorization and authentication, and to initiate a connection.

One of the flags in the CONNECT control packet is the Will. It determines whether the MQTT broker gets to store and publish the last will message associated with the last session. A will message is meant to be published once the MQTT client reestablishes a connection, in the event that the connection was interrupted or lost. 

**SSL/TLS**

Security, even in IoT needs to be a priority. The SSL/TLS feature helps you ensure data confidentiality and integrity. 

**Automatic Reconnect**

This feature ensures that the client can reconnect if the connection to the MQTT broker is severed.

**Offline Buffering**

This feature ‘stores’ messages when the recipient MQTT broker/client is disconnected.

**Websocket Support**

This feature allows for communication with brokers that allow the connection between client and server to persist, depending on the KeepAlive flag value in the CONNECT control packet.

**Standard TCP Support**

This feature allows for communication with brokers with TCP support.

**Blocking API**

This feature means that when the publisher requests the broker to send messages to the clients subscribed to a topic, execution only continues after successful delivery.

**Non-Blocking API**

This feature means that when the publisher requests the broker to send messages to the clients subscribed to a topic, execution can continue, and the clients can receive messages at different times.

Before looking at some paho mqtt examples, let’s understand MQTT’s origins and some basic concepts.

# 2. [MQTT Origins](/Eclipse_Paho/02_mqtt_origins.md)

