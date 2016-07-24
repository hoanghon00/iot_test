import paho.mqtt.publish as publish
import paho.mqtt.subscribe as sub

room_switches = [{"room":"p101", "status":0}]

input = raw_input("nhap OFF de tat LED hoac nhap ON de bat LED, nhap EXIT de thoat:\n")
print("Ban chon " + input + "!")

run = True
while(run):
 if(input == 'OFF'):
   publish.single("novatus/smarthotel/hoteltest", '{"cmd":"control","data":[{"room":"p101","status":0}]}', qos=1, hostname="192.168.1.100")
 elif(input == 'ON'):
   publish.single("novatus/smarthotel/hoteltest", '{"cmd":"control","data":[{"room":"p101","status":1}]}', qos=1, hostname="192.168.1.100")
 elif(input == 'INFO'):
   publish.single("novatus/smarthotel/hoteltest", '{"cmd":"query"}', qos=1, hostname="192.168.1.100")
 elif(input == 'EXIT'):
   break
 input = raw_input("")
 print("Ban chon " + input + "!")
 
print ("Chuong trinh vua thoat")
