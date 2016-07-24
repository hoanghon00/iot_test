import paho.mqtt.client as mqtt

def on_connect(mqttc, obj, flags, rc):
    print("Connected with result code "+str(rc))
 
def on_message(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
 
def on_publish(mqttc, obj, mid):
    print("mid: "+str(mid) + "\n")
 
def on_subscribe(mqttc, obj, mid, granted_qos):
    pass
 
def on_log(mqttc, obj, level, string):
    pass

mqttc = mqtt.Client("pc_client")
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
 
mqttc.connect("192.168.1.100", 1883, 60)
mqttc.subscribe("smarthotel/hoteltest/info", 1) 
mqttc.loop_start()

print("Help:\nON: turn on switch\nOFF: turn off switch\nSTATUS: get status info\nEXIT: exit program\n")
input = raw_input("")
print("Your selection is: " + input + "!")
user_input = str.upper(input)

run = True
while(run):
    if(user_input == 'OFF'):
        mqttc.publish("novatus/smarthotel/hoteltest", "[{ \"room\" : \"p101\", \"status\" : 0 }]", qos=1)
    elif(user_input == 'ON'):
        mqttc.publish("novatus/smarthotel/hoteltest", "[{ \"room\" : \"p101\", \"status\" : 1 }]", qos=1)
    elif(user_input == "STATUS"):
        mqttc.publish("novatus/smarthotel/hoteltest", "'cmd':'query'", qos=1)
    elif(input == 'EXIT'):
        break
    input = raw_input("")
    print("Ban chon " + input + "!")
    user_input = str.upper(input)
 
print ("Chuong trinh vua thoat")
