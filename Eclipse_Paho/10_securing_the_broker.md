# 10. Securing the Broker Using SSL/TLS

When using the pub-sub model to send data between IoT devices, we need to ensure data integrity and confidentiality. The Python mqtt server is not secured by default. We need to integrate SSL/TLS to ensure that unauthorized clients and publishers do not connect to the broker.

To do so, we could use digital certificates, but we would need to consider overheads and bandwidth for all the possible number of subscribers and publishers we would be dealing with. 

Let’s look at a simple paho mqtt Python example to secure our Mosquitto broker.

## Changing Configuration Settings to Secure the Mosquitto Broker

You can access Mosquitto’s configuration information (Linux Ubuntu) by 

        cd /etc/mosquitto/conf.d

Create a default configuration file:

        sudo nano /etc/mosquitto/conf.d/default.conf


![config file](/Eclipse_Paho/config%20file.png)

The above command opens a nano text editor

Enter the following command

                allow_anonymous false
                
                password_file /etc/mosquitto/passwd

![nano editor](/Eclipse_Paho/nano.png)

The command disallows anonymous connections to the python mqtt server.

# 11. [A Word on Troubleshooting](/Eclipse_Paho/11_a_word_on_troubleshooting.md)
