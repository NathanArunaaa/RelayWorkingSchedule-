#display actions code concept v1 
#By: Nathan Aruna 

import datetime
import time 

#replace print with raspberry pi GPIO pin trigger
def relay1(relayID):
  print("relay1")

def relay2(relayID):
  print("relay1")

def relay3(relayID):
  print("relay1")

    
#loop is needed to update dat/time vars 
while True:
  YEAR        = datetime.date.today().year     
  MONTH       = int(datetime.date.today().month)
  DATE        = datetime.date.today().day      
  HOUR        = datetime.datetime.now().hour   
  MINUTE      = datetime.datetime.now().minute 
  SECONDS     = datetime.datetime.now().second 
  WEEKDAY     = datetime.datetime.today().isoweekday()

  #used to if we want to end the operations
  sysrun = True

  #time/ date checks
  while (sysrun == True) and (WEEKDAY != 6 or 7): 
   while (HOUR >= 8) and (HOUR <=16): 
     
     relay1(1)
     relay2(2)
     relay3(3)
     

   print("Not In Operation Hour")



     



    







