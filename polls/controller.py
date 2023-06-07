import pyfirmata2

PORT = pyfirmata2.Arduino.AUTODETECT
board = pyfirmata2.Arduino(PORT)


def blueOn():
  board.digital[2].write(1)
  board.digital[3].write(0)
  board.digital[4].write(0)
  board.digital[5].write(0)
  print("Green ON")

def redOn():
  board.digital[2].write(0)
  board.digital[3].write(1)
  board.digital[4].write(0)
  board.digital[5].write(0)
  print("Red ON")

def greenOn():
  board.digital[2].write(0)
  board.digital[3].write(0)
  board.digital[4].write(1)
  board.digital[5].write(0)
  print("Blue ON")

def yellowOn():
  board.digital[2].write(0)
  board.digital[3].write(0)
  board.digital[4].write(0)
  board.digital[5].write(1)
  print("Yellow ON")

def allOff():
  board.digital[2].write(0)
  board.digital[3].write(0)
  board.digital[4].write(0)
  board.digital[5].write(0)
  print("Turn OFF all")