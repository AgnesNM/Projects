# 4. How to Install the Python MQTT Client

There are several ways to install the Eclipse Paho Python MQTT Client.

## Using Pip

Pip is Python’s package manager (Package Installer for Python in full)

Go to your terminal (Ctrl+Alt+T on Ubuntu) and enter the following command:
*pip install paho-mqtt*

![pip install paho-mqtt](/Eclipse_Paho/pip%20install.png)

You should see a ‘successfully installed’ message.

If you have any permission errors, you can use *sudo*

*sudo pip install paho mqtt*

You need to check the version to which Paho MQTT is attached if you have several Python versions. 

*pip –version*

![pip version](/Eclipse_Paho/pip%20version.png)

In my case, it was installed under Python 3.9. I will make a mental note of this when running Python paho-mqtt. I may have to specify the Python version for it to run as intended.

## Using Pip

A virtual environment allows you to confine your project to a folder with all the necessary dependencies for it to run effectively. This way, you avoid conflicts that would result from using different versions of a package, for example.

The official Python documentation recommends the creation of virtual environments using the venv module.

### Creating, activating, and working with a virtual environment

- Choose the directory in which to create your virtual environment.
- Create your virtual environment using the following command (make sure that your current working directory is the     top-level directory containing the directory in which you wish to create your virtual environment)

*python3 -m venv /path/to/directory/where/you/want/to/create/your/virtual/environment*

Activate your virtual environment (the following command works on a bash or zsh shell)

*source /path/to/directory/where/you/want/to/create/your/virtual/environment/bin/activate*

Note that you don’t need to activate your virtual environment. Activation only allows you to run the installed scripts without using full paths.

Install Python paho-mqtt via pip

*pip install paho-mqtt*


# 5. [How to Connect to a Python MQTT Broker](/Eclipse_Paho/05_how_to_connect_to_a_python_mqtt_broker.md)




