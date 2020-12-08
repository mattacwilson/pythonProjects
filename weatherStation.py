#Program name: senseHatWeatherStation
#Description: Reads temperature, pressure and humidity. Asks how many measurements needed.
#Author: Matthew Wilson EC1841586
#Date: 31/03/2020
#Company: Edinburgh College



from sense_hat import SenseHat
import time
from time import sleep
sense = SenseHat()

temp = 1
press = 2
humid = 3
exit = 4



readinput = 0
while (readinput != exit):

#Display menu system. Can comment out below to speed up process.
  sense.show_message("1. Temp. 2. Pressure. 3. Humidity")
  print("1. Temp \n2. Pressure \n3. Humidity\n4. Exit")


  readinput = int(input("choose"))



  b = (0,0,255)
  y = (255,255,0)
  w = (255,255,255)
  r = (255,0,0)
  x = (255,255,255)




  if (readinput == temp):
  
  
    sense.show_message("Measurements?")
    amount = int(input("Measurements?"))
    totaltemp = 0
    for i in range (amount):
      temperature=sense.get_temperature() 
      totaltemp = totaltemp+temperature

      sense.show_message(str (temperature))
      print (temperature)
    averagetemp=totaltemp / amount
    
    
    print ("Average temp:" + str(averagetemp))
    sense.show_message("Average temp: " + str(averagetemp ))
    
    if (averagetemp > 20):
      
      sense.show_message(str(averagetemp))
      print(averagetemp)
      print ("Damn, it's hot")
    
      hot=[
      r, r, r, r, r, r, r, r,
      r, r, x, r, r, x, r, r,
      r, r, x, r, r, x, r, r,
      r, r, r, r, r, r, r, r,
      r, r, r, r, r, r, r, r,
      r, r, x, x, x, x, r, r,
      r, x, r, r, r, r, x, r,
      r, r, r, r, r, r, r, r,
      ]

      sense.set_pixels(hot)
    
      sleep(2)
      sense.clear()
      
    
    elif (averagetemp < 15):
      print(averagetemp)
      print ("Damn, it's cold!")

      cold=[
      b, b, b, b, b, b, b, b,
      b, b, x, b, b, x, b, b,
      b, b, x, b, b, x, b, b,
      b, b, b, b, b, b, b, b,
      b, b, b, b, b, b, b, b,
      b, b, x, x, x, x, b, b,
      b, x, b, b, b, b, x, b,
      b, b, b, b, b, b, b, b,
      ]

      sense.set_pixels(cold)

      sleep(2)
      sense.clear()
      
    
    elif (averagetemp >= 15 or averagetemp <= 20):
      print(averagetemp)
      print ("It's just right")
    
      perfect=[
      y, y, y, y, y, y, y, y,
      y, y, x, y, y, x, y, y,
      y, y, x, y, y, x, y, y,
      y, y, b, y, y, b, y, y,
      y, x, b, y, y, b, x, y,
      y, y, x, x, x, x, y, y,
      y, y, y, y, y, y, y, y,
      y, y, y, y, y, y, y, y,
      ]

      sense.set_pixels(perfect)
    
      sleep(2)
      sense.clear()
      
  
  #Display pressure. Ask for measurements  
  elif (readinput == press):
    
    sense.show_message("Measurements?")
    amount = int(input("Measurements?"))
    totalpress = 0
    for i in range (amount):
      press=sense.get_pressure()
      totalpress = totalpress + press
      
      sense.show_message(str (press))
      print (press)
    averagepress = totalpress / amount
    print ("Average Pressure: " + str(averagepress))
    sense.show_message("Average pressure: " + str(averagepress))
      
  
  
  #Display humidity. Ask for measurements
  elif (readinput == humid):
    sense.show_message("Measurements?")
    amount = int(input("Measurements?"))
    totalhumid = 0
    for i in range (amount):
      humidity=sense.get_humidity()
      totalhumid = totalhumid + humidity
      
      sense.show_message (str (humidity))
      print(humidity)
    averagehumid = totalhumid / amount
    print("Average Humidity: " + str(averagehumid))
    sense.show_message("Average Humidity: " + str(averagehumid))
        

  #When pressing 4 exit program.  
  elif (readinput == exit):
    sense.show_message("Goodbye")
    print("Goodbye!")
    
