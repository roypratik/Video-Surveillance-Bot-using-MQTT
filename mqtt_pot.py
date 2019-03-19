import RPi.GPIO as GPIO
import time
from numpy import interp
servoPIN =12
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
import paho.mqtt.client as mqtt
p.start(0)
def on_connect(client, userdata, flags, rc):
    print("Connected!"+str(rc))
    client.subscribe("/pot/")

def on_message(client, userdata, msg):
    #print (int(msg.payload))
    value =(int(msg.payload))
    val=int(interp(value,[1,1024],[0,180]))
    val=(val/18)+2.5
    p.ChangeDutyCycle(val)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_forever()




