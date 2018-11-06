# !/usr/bin/python3
import RPi.GPIO as io
import numpy as np
from time import sleep

'''
To use this module, 
+ setup()
+ matrixcomm(matrix)
+ cleanup()

This will output the matrix to the pins listed. 
E.g. Matrix x = [[1, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 1]]
     matrixcomm(x) -> (handshake 0) to all 8 bits
     '' -> 1, 0, 1, 1, ... to all 8 bits
     '' -> 0, 1, 1, 0, ... ''
     '' -> (handshake 1) to all 8 bits. 
'''

# signal set for initialization of different pi programs.
standard_size = (4,4,4,8)
snake_start = [0,0,0,0,0,0,0,1]
raindrop_start = [0,0,0,0,0,0,1,0]
menu_start = [0,0,0,0,0,0,0,0]
program_check = [0,0,0,0,0,0,0,1]

# allowed setup and hold time 
delay = 0.0001
frame_count = 0

# pins used for data transmission to FPGA. Uses BCM numbers
pins = []
clock = 0
pin1 = 0
pin2 = 0
pin3 = 0
pin4 = 0
pin5 = 0
pin6 = 0
pin7 = 0
pin8 = 0

# pins used for gpio controller. 
controller = []
controller1 = 0
controller2 = 0
controller3 = 0
controller4 = 0
controller5 = 0
controller6 = 0

def setup():
    global clock
    global pin1
    global pin2
    global pin3
    global pin4
    global pin5
    global pin6
    global pin7
    global pin8
    global pins
    global controller1
    global controller2
    global controller3
    global controller4
    global controller5
    global controller6
    global controller
    
    clock = 16
    pin1 = 17
    pin2 = 27
    pin3 = 22
    pin4 = 26
    pin5 = 18
    pin6 = 23
    pin7 = 24
    pin8 = 25
    pins = [clock, pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8]
    
    controller1 = 0
    controller2 = 0
    controller3 = 0
    controller4 = 0
    controller5 = 0
    controller6 = 0
    controller = [controller1, controller2, controller3, controller4, controller5, controller6]

    io.setmode(io.BCM)

    for pin in pins:
        io.setup(pin, io.OUT)
    
    for button in controller:
        io.setup(button, io.IN)

    io.output(clock, 1)
    return 0


def setDelay(delay_arg):
    global delay
    delay = delay_arg


def getPins():
    global pins
    return pins


def cleanup():
    io.cleanup()


def startupSignal(numberOfProgram):
    bytecomm(program_check)
    if numberOfProgram == 0:
        bytecomm(menu_start)
    if numberOfProgram == 1:
        bytecomm(snake_start)
    elif numberOfProgram == 2:
        bytecomm(raindrop_start)


def matrixcomm(matrix):
    global frame_count
    frame_count += 1
    if frame_count % 32 == 0:
        frame_count = 0
        bytecomm(program_check)
        bytecomm(current_game)
    handshake = [[[1] * 8], [[0] * 8]]
    bytecomm(handshake[0][0])
    for x in matrix:
        for y in x:
            for z in y: 
                bytecomm(z)
    bytecomm(handshake[1][0])
    return


def bytecomm(array):
    count = 0
    pins = [clock, pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8]
    io.output(clock, 1)

    for pin in pins[1:]:
        print(str(pin) + " " + str(array[count]))
        io.output(pin, array[count])
        count += 1

    sleep(delay)
    io.output(clock, 0)
    sleep(delay)
    io.output(clock, 1)
    return

def queryController(buttonNumber):
    print(buttonNumber)
    return io.input(controller[buttonNumber])


test1 = [[[[[1]*8, [0]*8]*2]*4]*4]
test1 = test1[::-1]
test2 = [[[[1,0,1,0,1,0,1,0]]*4]*4]*4
test2 = test2[::-1]
test3 = [[[[0,1,0,1,0,1,0,1]]*4]*4]*4
test4 = [test2[0:2], test3[0:2]]
# still need to reverse array. 

# setup()
# matrixcomm([[[0,1,0,1,0,1,0,1], [1,0,1,0,1,0,1,0]], [[0,1,0,1,1,1,1,1],[0,0,0,0,1,1,1,1]]])
# cleanup()
