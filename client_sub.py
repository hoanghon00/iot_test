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
mqttc.subscribe("novatus/smarthotel/hoteltest", 1) 
mqttc.loop_forever()
