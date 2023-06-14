import pyfirmata2
import time
import random

# Define the constant and variables
PORT = pyfirmata2.Arduino.AUTODETECT
board = pyfirmata2.Arduino(PORT)
buzzer_pin = 1 # Buzzer pin

# Function that holds the delay in seconds
def delay(seconds):
  time.sleep(seconds)

# Define a main functions that hosts 2-13 outputs
def allPins(a, b, c, d, e, f, g, h, i, j, k, l):
  board.digital[2].write(a)
  board.digital[3].write(b)
  board.digital[4].write(c)
  board.digital[5].write(d)
  board.digital[6].write(e)
  board.digital[7].write(f)
  board.digital[8].write(g)
  board.digital[9].write(h)
  board.digital[10].write(i)
  board.digital[11].write(j)
  board.digital[12].write(k)
  board.digital[13].write(l)

def redOn():
  allPins(1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
  print("Red ON")

def blueOn():
  allPins(0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0)
  print("Green ON")

def greenOn():
  allPins(0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0)
  print("Blue ON")

def yellowOn():
  allPins(0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1)
  print("Yellow ON")

def allOff():
  allPins(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
  print("Turn OFF all")

def allON():
  allPins(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
  print('Turn ON all')

# Lightshow1 wiht delay test
def lightshow1():
  allPins(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
  delay(.3)
  allPins(0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
  delay(.3)
  allPins(0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
  delay(.3)
  allPins(0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)
  delay(.3)
  allPins(0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0)
  delay(.3)
  allPins(0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
  delay(.3)
  allPins(0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)
  delay(.3)
  allPins(0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0)
  delay(.3)
  allPins(0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0)
  delay(.3)
  allPins(0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0)
  delay(.3)
  allPins(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0)
  delay(.3)
  allPins(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
  delay(.3)
  allOff
  delay(.3)
  allON()
  delay(.3)
  allOff()
  delay(.3)
  allON()
  delay(.3)
  allOff()

def lightshow2():
  allPins(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
  delay(.3)
  allPins(1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
  delay(.3)
  allPins(1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0)
  delay(.3)
  allPins(1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0)
  delay(.3)
  allPins(1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1)
  delay(.3)
  allPins(1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1)
  delay(.3)
  allPins(1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1)
  delay(.3)
  allPins(1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1)
  delay(.3)
  allPins(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
  delay(.3)
  allOff()
  delay(.3)
  allON()
  delay(.3)
  allOff()

notes = {
  'C4': 261.63,
  'D4': 293.66,
  'E4': 329.63,
  'F4': 349.23,
  'G4': 392.00,
  'A4': 440.00,
  'B4': 493.88,
  'C5': 523.25,
}

mario_bross_song = [
  'E4', 'E4', 'E4', 'C4', 'E4', 'G4', 'G3',
  'C4', 'G3', 'E3', 'A3', 'B3', 'A#3', 'A3',
  'G3', 'E4', 'G4', 'A4', 'F4', 'G4', 'E4',
  'C4', 'D4', 'B3', 'C4', 'G3', 'E3', 'A3',
  'B3', 'A#3', 'A3', 'G3', 'E4', 'G4', 'A4',
  'F4', 'G4', 'E4', 'C4', 'D4', 'B3', 'C4',
  'G3', 'E3', 'A3', 'B3', 'A#3', 'A3', 'G3'
]

def MarioBrossSound():
  random_number = random.randint(1, 4)
  
  # Iterate each note of the mario bross song
  for note in mario_bross_song:
    frequency = notes[note]
    board.digital[buzzer_pin].write(1)
    board.send_sysex(0x0B, board.get_pin('d:{}:o'.format(buzzer_pin)).mode)
    board.send_sysex(0x0B, int(frequency))
    
    # Validate if the random number is 1-4. Then turn on "color" LEDs 
    if random_number == 1:
      redOn()
    elif random_number == 2:
      blueOn()
    elif random_number == 3:
      greenOn()
    elif random_number == 4:
      yellowOn()
    delay(.3)
    board.digital[buzzer_pin].write(0)
    allOff()
    delay(.05)