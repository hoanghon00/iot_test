import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO 
import json
 
gpio_pin = 11 
map_pin = { "p101" : 11 }
 
GPIO.setmode(GPIO.BOARD) # chon kieu danh so chan GPIO la BOARD
GPIO.setup(gpio_pin, GPIO.OUT)
GPIO.output(gpio_pin, GPIO.HIGH)

def update_room_switch(room_no, status):
  if (status == 1):
    print("Switch turn on " + room_no)
    GPIO.output(map_pin[room_no], GPIO.LOW)
  else:
    print("Switch turn off " + room_no)
    GPIO.output(map_pin[room_no], GPIO.HIGH)
 
def on_connect(mqttc, obj, flags, rc):
 print("Connected with result code "+str(rc))
 
def on_message(mqttc, obj, msg):
 print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
 if(msg.topic == "novatus/smarthotel/hoteltest"):
    request_info = json.loads(msg.payload)
    for room_info in request_info:
      update_room_switch(room_info['room'], room_info['status'])
   #if(str(msg.payload) == "1"): #bat LED
   #  GPIO.output(gpio_pin, GPIO.HIGH)
   #elif(str(msg.payload) == "0"): #tat LED
   #  GPIO.output(gpio_pin, GPIO.LOW)
 
def on_publish(mqttc, obj, mid):
 print("mid: "+str(mid))
 
def on_subscribe(mqttc, obj, mid, granted_qos):
 pass
 
def on_log(mqttc, obj, level, string):
 pass
 
mqttc = mqtt.Client("hoteltest")
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
 
mqttc.connect("192.168.43.227", 1883, 60) #dien IP cua Pi, vd: 192.168.1.77
mqttc.subscribe("novatus/smarthotel/hoteltest", 1) 
mqttc.loop_forever()
