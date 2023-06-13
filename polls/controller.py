import pyfirmata2
import time

PORT = pyfirmata2.Arduino.AUTODETECT
board = pyfirmata2.Arduino(PORT)


def redOn():
  board.digital[2].write(1)
  board.digital[3].write(1)
  board.digital[4].write(1)
  board.digital[5].write(0)
  board.digital[6].write(0)
  board.digital[7].write(0)
  board.digital[8].write(0)
  board.digital[9].write(0)
  board.digital[10].write(0)
  board.digital[11].write(0)
  board.digital[12].write(0)
  board.digital[13].write(0)
  print("Red ON")

def blueOn():
  board.digital[2].write(0)
  board.digital[3].write(0)
  board.digital[4].write(0)
  board.digital[5].write(1)
  board.digital[6].write(1)
  board.digital[7].write(1)
  board.digital[8].write(0)
  board.digital[9].write(0)
  board.digital[10].write(0)
  board.digital[11].write(0)
  board.digital[12].write(0)
  board.digital[13].write(0)
  print("Green ON")

def greenOn():
  board.digital[2].write(0)
  board.digital[3].write(0)
  board.digital[4].write(0)
  board.digital[5].write(0)
  board.digital[6].write(0)
  board.digital[7].write(0)
  board.digital[8].write(1)
  board.digital[9].write(1)
  board.digital[10].write(1)
  board.digital[11].write(0)
  board.digital[12].write(0)
  board.digital[13].write(0)
  print("Blue ON")

def yellowOn():
  board.digital[2].write(0)
  board.digital[3].write(0)
  board.digital[4].write(0)
  board.digital[5].write(0)
  board.digital[6].write(0)
  board.digital[7].write(0)
  board.digital[8].write(0)
  board.digital[9].write(0)
  board.digital[10].write(0)
  board.digital[11].write(1)
  board.digital[12].write(1)
  board.digital[13].write(1)
  print("Yellow ON")

def allOff():
  board.digital[2].write(0)
  board.digital[3].write(0)
  board.digital[4].write(0)
  board.digital[5].write(0)
  board.digital[6].write(0)
  board.digital[7].write(0)
  board.digital[8].write(0)
  board.digital[9].write(0)
  board.digital[10].write(0)
  board.digital[11].write(0)
  board.digital[12].write(0)
  board.digital[13].write(0)
  print("Turn OFF all")

def allON():
  board.digital[2].write(1)
  board.digital[3].write(1)
  board.digital[4].write(1)
  board.digital[5].write(1)
  board.digital[6].write(1)
  board.digital[7].write(1)
  board.digital[8].write(1)
  board.digital[9].write(1)
  board.digital[10].write(1)
  board.digital[11].write(1)
  board.digital[12].write(1)
  board.digital[13].write(1)
  print('Turn ON all')

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

# Lightshow1 wiht delay test
def lightshow1():
  allPins(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
  time.sleep(1)
  allPins(0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0)
  time.sleep(1)
  allOff()