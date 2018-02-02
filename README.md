# Washing Machine motion detector
Detects when a washing machine is active. Great for college housing!

## Requirements
1. Raspberry Pi (I used version 3B) - https://goo.gl/CX5RdM
2. SW-420 Vibration Sensor - https://goo.gl/LiHqU4

## Installation
1. Instructions for setting up raspberry pi - https://www.raspberrypi.org/help/noobs-setup/2/
2. Instructions for setting up Flask - http://flask.pocoo.org/docs/0.12/quickstart/#quickstart
3. Download and move to folder of choice. Then run the following:

```
export FLASK_APP=washing_machine.py
flask run
```

## Setting up listening port
"If you run the server you will notice that the server is only accessible from your own computer, not from any other in the network. This is the default because in debugging mode a user of the application can execute arbitrary Python code on your computer.

If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply by adding --host=0.0.0.0 to the command line:

```
flask run --host=0.0.0.0
```

This tells your operating system to listen on all public IPs." - Flask Quickstart Guide

## Acknowledgements
PiddlerInTheRoot - https://www.youtube.com/watch?v=twBpU_pfFbI