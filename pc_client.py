import paho.mqtt.publish as publish
 
input = raw_input("nhap OFF de tat LED hoac nhap ON de bat LED, nhap EXIT de thoat:\n")
print("Ban chon " + input + "!")
 
run = True
while(run):
 if(input == 'OFF'):
   publish.single("novatus/smarthotel/hoteltest", "[{ \"room\" : \"p101\", \"status\" : 0 }]", qos=1, hostname="192.168.1.100")
 elif(input == 'ON'):
   publish.single("novatus/smarthotel/hoteltest", "[{ \"room\" : \"p101\", \"status\" : 1 }]", qos=1, hostname="192.168.1.100") 
 elif(input == 'EXIT'):
   break
 input = raw_input("")
 print("Ban chon " + input + "!")
 
print ("Chuong trinh vua thoat")
