import paho.mqtt.client as paho
from paho import mqtt
from time import sleep
from tkinter import Variable
import Adafruit_DHT
import time
from itertools import count
import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BOARD)
pin_to_circuit = 11
hitung = 0
GPIO.setup(pin_to_circuit, GPIO.OUT)
GPIO.output(pin_to_circuit, GPIO.LOW)
time.sleep(5)
GPIO.setup(pin_to_circuit, GPIO.IN)
while (GPIO.input(pin_to_circuit) == GPIO.LOW):
    hitung += 1

# define static variable
# broker = "localhost" # for local connection
broker = "broker.hivemq.com"  # for online version
port = 1883
timeout = 60

username = ''
password = ''
topic = "sensor/manpasi"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
def on_publish(client,userdata,result):
	print("data published \n")
	


client1 = paho.Client("devices0",userdata=None,protocol=paho.MQTTv5)
client1.username_pw_set(username=username,password=password)
client1.on_connect = on_connect
client1.on_publish = on_publish
client1.connect(broker,port,timeout)

Count = 0
while Count == 0:
    status = float(hitung)
    message = status
    ret = client1.publish(topic,payload=message,qos=1)
    sleep(1)