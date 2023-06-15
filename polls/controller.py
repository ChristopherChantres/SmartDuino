# Import pyfirmata, time and random
import pyfirmata2
import time
import random

# Define the constant and variables
PORT = pyfirmata2.Arduino.AUTODETECT # PORT constant that stores the autodetected port of the arduino
board = pyfirmata2.Arduino(PORT) # Create the board variable that holds the arudino with its port
buzzer_pin = 9 # Buzzer set in pin 9

# Function that holds the delay in seconds
def delay(seconds):
  time.sleep(seconds) # Delay "n" amount of seconds

# Define a main functions that hosts 2-13 Arduino outputs
# Letters a...l are going to be variables so that can hold different states
def allPins(a, b, c, d, e, f, g, h, i, j, k, l):
  board.digital[2].write(a) # Set the digital pin 2 ==> a
  board.digital[3].write(b) # Set the digital pin 3 ==> b
  board.digital[4].write(c) # Set the digital pin 4 ==> c
  board.digital[5].write(d) # Set the digital pin 5 ==> d
  board.digital[6].write(e) # Set the digital pin 6 ==> e
  board.digital[7].write(f) # Set the digital pin 7 ==> f
  board.digital[8].write(g) # Set the digital pin 8 ==> g
  board.digital[9].write(h) # Set the digital pin 9 ==> h
  board.digital[10].write(i) # Set the digital pin 10 ==> i
  board.digital[11].write(j) # Set the digital pin 11 ==> j
  board.digital[12].write(k) # Set the digital pin 12 ==> k
  board.digital[13].write(l) # Set the digital pin 13 ==> l

# Turn on all red LEDs
def redOn():
  allPins(1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0) # Calling the fnc allPins() with the pins to be lit up
  print("Red ON") # Display in console the action

# Turn on all blue LEDs
def blueOn():
  allPins(0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0) # Calling the fnc allPins() with the pins to be lit up
  print("Green ON") # Display in console the action

# Turn on all green LEDs
def greenOn():
  allPins(0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0) # Calling the fnc allPins() with the pins to be lit up
  print("Blue ON") # Display in console the action

# Turn on all yellow LEDs
def yellowOn():
  allPins(0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1) # Calling the fnc allPins() with the pins to be lit up
  print("Yellow ON") # Display in console the action

def allOff():
  allPins(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) # Calling the fnc allPins() with the pins to be lit up
  print("Turn OFF all") # Display in console the action

def allON():
  allPins(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # Calling the fnc allPins() with the pins to be lit up
  print('Turn ON all') # Display in console the action

# Lightshow1
# Calling the fnc allPins with the pins to be lit up
# Add a delay between each call to the fnc allPins()
# Calling the functin allOff() and allON()
def lightshow1():
  allPins(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) # Calling the allPins() fnc
  delay(.3) # Delay .3s
  allPins(0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) # Calling the allPins() fnc
  delay(.3) # Delay .3s
  allPins(0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0) # Calling the allPins() fnc
  delay(.3) # Delay .3s
  allPins(0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0) # Calling the allPins() fnc
  delay(.3) # Delay .3s
  allPins(0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0) # Calling the allPins() fnc
  delay(.3) # Delay .3s
  allPins(0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0) # Calling the allPins() fnc
  delay(.3) # Delay .3s
  allPins(0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0) # Calling the allPins() fnc
  delay(.3) # Delay .3s
  allPins(0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0) # Calling the allPins() fnc
  delay(.3) # Delay .3s
  allPins(0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) # Calling the allPins() fnc
  delay(.3) # Delay .3s
  allPins(0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0) # Calling the allPins() fnc
  delay(.3) # Delay .3s
  allPins(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0) # Calling the allPins() fnc
  delay(.3) # Delay .3s
  allPins(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1) # Calling the allPins() fnc
  delay(.3) # Delay .3s
  allOff() # Turn off all LEDs
  delay(.3) # Delay .3s
  allON() # Calling the function allON()
  delay(.3) # Delay .3s
  allOff() # Turn off all LEDs
  delay(.3) # Delay .3s
  allON() # Calling the function allON()
  delay(.3) # Delay .3s
  allOff() # Turn off all LEDs


# Lightshow2
# Calling the fnc allPins with the pins to be lit up
# Add a delay between each call to the fnc allPins()
# Calling the functin allOff() and allON()
def lightshow2():
  allPins(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) # Calling the allPins() fnc
  delay(.3) # Delay .3s
  allPins(1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0) # Calling the allPins() fnc
  delay(.3) # Delay .3s
  allPins(1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0) # Calling the allPins() fnc
  delay(.3) # Delay .3s
  allPins(1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0) # Calling the allPins() fnc
  delay(.3) # Delay .3s
  allPins(1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1) # Calling the allPins() fnc
  delay(.3) # Delay .3s
  allPins(1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1) # Calling the allPins() fnc
  delay(.3) # Delay .3s
  allPins(1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1) # Calling the allPins() fnc
  delay(.3) # Delay .3s
  allPins(1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1) # Calling the allPins() fnc
  delay(.3) # Delay .3s
  allPins(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # Calling the allPins() fnc
  delay(.3) # Delay .3s
  allOff() # Turn off all LEDs
  delay(.3) # Delay .3s
  allON() # Calling the function allON()
  delay(.3) # Delay .3s
  allOff() # Turn off all LEDs

def lightshow3():
  allON() # Calling the function allON()
  delay(2) # Delay 2s
  allOff() # Calling the function allOff()
  delay(2) # Delay 2s
  allON() # Calling the function allON()
  delay(1) # Delay 1.5s
  allOff() # Calling the function allOff()
  delay(.5) # Delay .5s
  allON() # Calling the function allON()
  delay(.5) # Delay .5s
  allOff() # Calling the function allOff()
  delay(.25) # Delay .25
  allON() # Calling the function allON()
  delay(.25) # Delay .25
  allOff() # Calling the function allOff()
  delay(.125) # Delay .125s
  allON() # Calling the function allON()
  delay(.125) # Delay .125s
  allOff() # Calling the function allOff()
  delay(.0625) # Delay .0625s
  redOn() # Turn on all red LEDs
  delay(1) # Delay 1s
  yellowOn() # Turn on all yellow LEDs
  delay(1) # Delay 1s
  blueOn() # Turn on all blue LEDs
  delay(1) # Delay 1s
  greenOn() # Turn on all green LEDs
  delay(1) # Delay 1s
  allOff() # Turn off all LEDs

# Fucntion that calls all the lightshows and then in calls itself at the end (recursivity)
def ultimatelightshow():
  lightshow1() # Calling lightshow1()
  lightshow2() # Calling lightshow2()
  lightshow3() # Calling lightshow3()
  ultimatelightshow()  # Calling ultimatelightshow() again