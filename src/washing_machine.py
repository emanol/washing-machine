from flask import Flask
import RPi.GPIO as GPIO
import time

# flask
app = Flask(__name__)

# Raspberry Pi Detector
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

# Washer State
is_active = False
time_active = 0

@app.route('/')
def washer():
    if is_active:
        return "Washing Machine has been active for " + str(time_active) + " minutes." 
    else:
        return "The Washing Machine is available."

time.sleep(60)
def callback(channel):
    if GPIO.input(channel):
        if is_active:
            time_active += 1
        is_active = True
    else:
        is_active = False

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)    

if __name__ == '__main__':
    app.run()