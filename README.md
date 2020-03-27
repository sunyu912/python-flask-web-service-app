# python-flask-web-service-app

Here is a backend sample:
https://repl.it/@sunyu912/depression-server

Here is a frontend sample:
https://repl.it/@sunyu912/WebFrontend

## Instructions to Run the Web Serivce

Open the backend in repl.it and run it. 
Get the backend URL such as https://depression-server.sunyu912.repl.co/

Open the frontend in repl.it and make sure to update the script.js to use the URL above.

## How to Install Git in Amazon Linux

```sudo yum update -y```
 
```sudo yum install git -y```

## How to Install Python3

```sudo yum install python3```

## How to Install Flask
 
```pip install Flask```

or 

```pip3 install Flask```

# How to Run Python application in background

```nohup python Server.py > log.txt &```

or

```nohup python3 Server.py > log.txt &```


## How to Redirect the Port Number

If you have your app up and running in your own server, most likely it is running on a port such as 5000, 8080, et.

We want to change and use the default port 80, so that it is easy for people to visit. You need to run the following two commands in your server:

Please make sure to change 5000 into the port number your application is uing. 

```sudo iptables -t nat -I PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 5000```

```sudo iptables -I INPUT -p tcp --dport 5000 -j ACCEPT``` 