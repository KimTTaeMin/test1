Python 2.7.10 (default, May 23 2015, 09:44:00) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
 import serial
 import time 

 arduino = serial.Serial("/dev/ttyACM4", 9600) 
 
 def onOffFunction(): 
   command = raw_input("Type R/r/G/g: "); 
 	if command =="R":  
 		time.sleep(1)  
 		arduino.write('R')  
 		onOffFunction() 
 	elif command =="r": 
 		time.sleep(1)  
 		arduino.write('r') 
 		onOffFunction() 
 	elif command =="G":
		time.sleep(1)
		arduino.write('G')  
 		onOffFunction()
 	elif command =="g":
		time.sleep(1)
		arduino.write('g')  
 		onOffFunction()
 	else:  
 		time.sleep(1)  
 		arduino.close() 
 
 time.sleep(1) 
 
 onOffFunction() 
