# 11. A Word on Troubleshooting

We have already come across a scenario that would require you to do some troubleshooting, in the ‘Installing The Mosquitto MQTT Broker Pro Edition’ section. You need to install docker-compose, and its dependencies as well.

We also talked about giving non-root users access to docker to ensure the smooth running of your applications.

The errors you are likely to encounter when using Eclipse Paho Python could be quite specific too, ranging from syntax errors in your code, to software conflicts. 

The best thing to do is to always check the information availed by the error and try to find its solution on Google (or your preferred browser). You can also ask questions about the error on different forums, for example [Stack Overflow](https://stackoverflow.com/) or [IoT Stack Exchange](https://iot.stackexchange.com/)

A quick example we can look at here is this question from [Stack Overflow](https://stackoverflow.com/questions/66784744/mosquito-server-send-last-will-message-even-the-clients-are-still-connected-and)

![Question on last will message](/Eclipse_Paho/Question.png)

As you can see, the problem is that the last will message is being sent even when the server and client are still connected (you can refer to the Eclipse Paho features section to further understand last will messages)

![Response on last will message](/Eclipse_Paho/Answer.png)

The response lets him know that the issue probably results from setting the last will message as a retained message, which causes it to be delivered every time a new client subscribes to the topic in question.

# 12. [Conclusion](/Eclipse_Paho/12_conclusion.md)



