#display actions code concept v1 
#By: Nathan Aruna 
#Code Explination( When code begins it goes into the main function then runs relay on. The relay does its patern then checks for time if the time is not right then it sends it back to the main loop)


#Importing Modules
import datetime
import time 
#import RPi.GPIO as GPIO
import configparser


#GPIO.setmode(GPIO.BCM)


#list of relay GPIO pins to output to (DO NOT TOUCH)
relayPinOut = [5, 6, 13, 16, 19, 20, 21, 26]

#time between next relay turn on
relayDelay = 2

#system running variable(False = not going to run)
sysRunning = True


#function to send singals to relays(Off)
def relayOff():
    print("relays off")
    #GPIO.cleanup() 


#function to send singals to relays(ON)
def relayOn():
  
  WEEKDAY = datetime.datetime.today().weekday()
  HOUR = datetime.datetime.now().hour
  
  while (HOUR >= 8) and (HOUR <= 15) and (WEEKDAY != 5) and (WEEKDAY != 6):
          
       print("Display Cycle Started")
       #GPIO.setmode(GPIO.BCM)

       #GPIO.setup(5, GPIO.OUT)
       #GPIO.output(5, GPIO.LOW)
       print('relay5 is on')
       time.sleep(relayDelay)

       #GPIO.setup(6, GPIO.OUT)
       #GPIO.output(6, GPIO.LOW)
       print('relay6 is on')
       time.sleep(relayDelay)

       #GPIO.setup(13, GPIO.OUT)
       #GPIO.output(13, GPIO.LOW)
       print('relay13 is on')
       time.sleep(relayDelay)
       
       #GPIO.setup(16, GPIO.OUT)
       #GPIO.output(16, GPIO.LOW)
       print('relay16 is on')
       time.sleep(relayDelay)
       
       #GPIO.setup(19, GPIO.OUT)
       #GPIO.output(19, GPIO.LOW)
       print('relay19 is on')
       time.sleep(relayDelay)

       #GPIO.setup(20, GPIO.OUT)
       #GPIO.output(20, GPIO.LOW)
       print('relay20 is on')
       time.sleep(relayDelay)

       #GPIO.setup(21, GPIO.OUT)
       #GPIO.output(21, GPIO.LOW)
       print('relay21 is on')
       time.sleep(relayDelay)

       #GPIO.setup(26, GPIO.OUT)
       #GPIO.output(26, GPIO.LOW)
       print('relay26 is on')
       time.sleep(relayDelay)
       
       relayOff()
       
       continue
       
       
#Main Loop
def main():
 while sysRunning == True:
   
  HOUR = datetime.datetime.now().hour   
  WEEKDAY = datetime.datetime.today().weekday()
 
  if (HOUR >= 8) and (HOUR <= 15) and (WEEKDAY != 5) and (WEEKDAY != 6):
        if sysRunning == True:
          print("System Running")
          relayOn()
         
        else:
          relayOff()
          print("System Not Running")
  else:
        print("Not In Operation Hours")
        

#Relay Config

def relayConfig():
 while True:
    
  
  
  relaySelection = str(input("Relay To Edit:"))
  relayTimeBegin = str(input("Time To Begin:"))
  relayTimeEnd = str(input("Time To End:"))
  
  config = configparser.ConfigParser()


  if relaySelection == "1":
    config.add_section('Relay1')
    config.set('Relay1', 'on_time', relayTimeBegin)
    config.set('Relay1', 'off_time', relayTimeEnd)
    continue
    
  else:
    print("No Valid Relay Selected")
    
    with open('relay_config.ini', 'w') as configfile:
     config.write(configfile)


    
    
  
  if relaySelection == "2":
    config.add_section('Relay2')
    config.set('Relay2', 'on_time', relayTimeBegin)
    config.set('Relay2', 'off_time', relayTimeEnd)
    continue
    
  else:
    print("No Valid Relay Selected")
    
    with open('relay_config.ini', 'w') as configfile:
     config.write(configfile)


  
  
  
  if relaySelection == "3":
    config.add_section('Relay3')
    config.set('Relay3', 'on_time', relayTimeBegin)
    config.set('Relay3', 'off_time', relayTimeEnd)
    continue
    
  else:
    print("No Valid Relay Selected")
    
    with open('relay_config.ini', 'w') as configfile:
     config.write(configfile)


    
    
  
  if relaySelection == "4":
    config.add_section('Relay4')
    config.set('Relay4', 'on_time', relayTimeBegin)
    config.set('Relay4', 'off_time', relayTimeEnd)
    continue
    
  else:
    print("No Valid Relay Selected")
    
    with open('relay_config.ini', 'w') as configfile:
     config.write(configfile)


    
    
  
  if relaySelection == "4":
    config.add_section('Relay4')
    config.set('Relay5', 'on_time', relayTimeBegin)
    config.set('Relay5', 'off_time', relayTimeEnd)
    continue
    
  else:
   print("No Valid Relay Selected")
   
   with open('relay_config.ini', 'w') as configfile:
    config.write(configfile)


   


  




relayConfig()
#Run main function
main()