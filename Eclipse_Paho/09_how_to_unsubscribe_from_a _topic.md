# 9. How to Unsubscribe from a Topic

If we want a client to stop receiving messages from a publisher, the client needs to send an ‘unsubscribe’ message to the broker. This makes the client a publisher too!

The following python mqtt example shows a sample script to unsubscribe from topics. It is basically the opposite of the python paho mqtt example we looked at the topic subscription section.

![unsubscribe script](/Eclipse_Paho/Unsubscribe%20Script.png)

As you can see, the broker received the unsubscribe request…

![unsubscribe](/Eclipse_Paho/Unsubscribe.png)

And the PINGREQ/PINGRESP control packet is still being sent to show that the connection between the client and server is still alive.

# 10. [Securing the Broker Using SSL/TLS](/Eclipse_Paho/10_securing_the_broker.md)




