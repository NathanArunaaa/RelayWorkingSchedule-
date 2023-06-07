#display actions code concept v1 
#By: Nathan Aruna 
import datetime
import time 
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#system state 
sysRunning = True

#list of relay GPIO pins to output to (DO NOT TOUCH)
relayPinOut = [5, 6, 13, 16, 19, 20, 21, 26]

relayDelay = 60
   
#loop is needed to update dat/time vars and for time checks
while sysRunning == True:
  YEAR        = datetime.date.today().year     
  MONTH       = int(datetime.date.today().month)
  DATE        = datetime.date.today().day      
  HOUR        = datetime.datetime.now().hour   
  MINUTE      = datetime.datetime.now().minute 
  WEEKDAY     = datetime.datetime.today().weekday()
 
  
  #if relay state is false circuit is open, true circuit is closed
  relay5_state = False
  relay6_state = False
  relay13_state = False
  relay16_state = False
  relay19_state = False 
  relay20_state = False 
  relay21_state = False 
  relay26_state = False 
  
  #functions to send singals to relays
  def relayOn():
    while True:
       print("Working Times Started")
       GPIO.setmode(GPIO.BCM)

       GPIO.setup(5, GPIO.OUT)
       GPIO.output(5, GPIO.LOW)
       relay5_state = True
       print('relay5 is on')
       time.sleep(relayDelay)

       GPIO.setup(6, GPIO.OUT)
       GPIO.output(6, GPIO.LOW)
       relay6_state = True
       print('relay6 is on')
       time.sleep(relayDelay)

       GPIO.setup(13, GPIO.OUT)
       GPIO.output(13, GPIO.LOW)
       relay13_state = True
       print('relay13 is on')
       time.sleep(relayDelay)
       
       GPIO.setup(16, GPIO.OUT)
       GPIO.output(16, GPIO.LOW)
       relay16_state = True
       print('relay16 is on')
       time.sleep(relayDelay)

       GPIO.setup(19, GPIO.OUT)
       GPIO.output(19, GPIO.LOW)
       relay19_state = True
       print('relay19 is on')
       time.sleep(relayDelay)

       GPIO.setup(20, GPIO.OUT)
       GPIO.output(20, GPIO.LOW)
       relay20_state = True
       print('relay20 is on')
       time.sleep(relayDelay)

       GPIO.setup(21, GPIO.OUT)
       GPIO.output(21, GPIO.LOW)
       relay21_state = True
       print('relay21 is on')
       time.sleep(relayDelay)

       GPIO.setup(26, GPIO.OUT)
       GPIO.output(26, GPIO.LOW)
       relay26_state = True
       print('relay26 is on')
       time.sleep(relayDelay)
    
  def relayOff():
    print("relays off")
    GPIO.output(relayPinOut, GPIO.HIGH)
    GPIO.cleanup() 

  
  #relay 1
  if (HOUR >= 8) and (HOUR <= 16) and (WEEKDAY != 5) and (WEEKDAY != 6):
        if sysRunning == True:
          relayOn()
          print("System Running")
        else:
          relayOff()
          print("System Not Running")
  else:
        print("Not In Operation Hours")
        
  
  