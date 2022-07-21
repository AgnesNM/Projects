# Django

Started learning Django as part of the Powerlearn Project. I am still trying to get the hang of the MVT architecture.

Here are some gotchas, or notes to self that you are likely to miss as a Django beginner:

1. When changing the ALLOWED_HOSTS in your settings.py (project directory) don't add the port number. If your IP is localhost, 127.0.0.1 and ypour port number is 8000, then add only '127.0.0.1' as a string, with no treailing slash or port number.

2. When defining your url path in your urls.py (project directory), don't add a slash to represent the home page, an empty string will do. Also, don't add an extra space.

![urls.py](/Views.png)



