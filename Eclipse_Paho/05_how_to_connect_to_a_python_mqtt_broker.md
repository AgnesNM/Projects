# 5. How to Connect to a Python MQTT Broker

After installing the Paho MQTT Client, we need to use a broker to distribute the messages to the correct subscribers. We are going to install the broker first and then connect to it.

## Installing the Mosquitto MQTT Broker

There are several ways to install the Mosquitto MQTT broker. 

### Installing from Source

Here you download the .tar file from the [Mosquito downloads section](https://mosquitto.org/download/) on the official site or use the source code from the [Eclipse Mosquitto git repo](https://github.com/eclipse/mosquitto) 

### Binary Installation

In this case, you can use a package manager like pip (Linux) or brew (MacOS) depending on your Operating System and/or distro.

[Mosquito downloads section](https://mosquitto.org/download/) 

For our illustration, we will use Linux Ubuntu 20.04

- Enter the following command to install the Mosquitto MQTT broker

        sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa

- Enter your password

- Follow the prompts as in the screenshot below:

![install the mosquitto broker from the repository](/Eclipse_Paho/mqtt%20broker.png)

- Enter *sudo apt-get update*

- Install the Ubuntu broker package 

        sudo apt-get install mosquitto

- Follow the prompts as in the screenshot below:

![install the mosquitto broker](/Eclipse_Paho/mosquitto%20broker%202.png)

- Choose 'y'

- Press ‘enter’

- Install the Mosquitto client packages that run the message publication commands and topic subscription via the following command:

        sudo apt-get install mosquitto-clients

- Check the recently installed mosquitto service status

        sudo service mosquitto status

- You should see a message like… ‘starting MQTT Broker…’ as in the below screenshot:

![mosquitto service status](/Eclipse_Paho/broker%203.png)

- Confirm that the Mosquitto server is listening via the default port: 1883

        netstat -an | grep 1883

![mosquitto server port](/Eclipse_Paho/broker.png)

# 6. [How to Publish Messages](/Eclipse_Paho/06_how_to_publish_messages.md)