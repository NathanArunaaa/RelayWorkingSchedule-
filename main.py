#display actions code concept v1 
#By: Nathan Aruna 
import datetime
import time 
#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)

sysRunning = True

    
#loop is needed to update dat/time vars and for time checks
while sysRunning == True:
  YEAR        = datetime.date.today().year     
  MONTH       = int(datetime.date.today().month)
  DATE        = datetime.date.today().day      
  HOUR        = datetime.datetime.now().hour   
  MINUTE      = datetime.datetime.now().minute 
  WEEKDAY     = datetime.datetime.today().weekday()

  relay1State = False
  relay2State = False
  relay3State = False
  relay4State = False
  
  Relay1GPIO = 17
  Relay2GPIO = 18
  Relay3GPIO = 19
  Relay4GPIO = 20
  
  #functions to send singals to relays
  def relayOn():
    print("relays on")
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(17, GPIO.OUT)
    #GPIO.output(17, GPIO.LOW)

  def relayOff():
    print("relays off")
    #GPIO.output(17, GPIO.HIGH)
    #GPIO.cleanup() 

  
  #relay 1
  if (HOUR >= 8) and (HOUR <= 16) and (WEEKDAY != 5) and (WEEKDAY != 6):
        if (relay1State == False):
          relay1State = True
          relayOn()
          print("relay1 on")
        else:
          relay1State = False
          relayOff(relay1State)
          print("relay1 off")
  else:
        print("Not In Operation Hours")
        
  
  #relay 2
  if (HOUR >= 8) and (HOUR <= 16) and (WEEKDAY != 5) and (WEEKDAY != 6):
        if (relay2State == False):
          relay2State = True
          relayOn()
          print("relay2 on")
        else:
          relay2State = False
          relayOff()
          print("relay2 off")
  else:
        print("Not In Operation Hours")
  
  
  #relay 3
  if (HOUR >= 8) and (HOUR <= 16) and (WEEKDAY != 5) and (WEEKDAY != 6):
        if (relay3State == False):
          relay3State = True
          relayOn()
          print("relay3 on")
        else:
          relay3State = False
          relayOff()
          print("relay3 off")
  else:
        print("Not In Operation Hours")
  
  
  #relay 4
  if (HOUR >= 8) and (HOUR <= 16) and (WEEKDAY != 5) and (WEEKDAY != 6):
        if (relay4State == False):
          relay4State = True
          relayOn()
          print("relay4 on")
        else:
          relay4State = False
          relayOff()
          print("relay4 off")
  else:
         print("Not In Operation Hours")

     








