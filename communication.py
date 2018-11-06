# !/usr/bin/python3
import RPi.GPIO as io
from time import sleep

'''
To use this module, 
+ setup()
+ matrixcomm(matrix)
+ cleanup()

changeProgram() must now be used to sync with cube base

This will output the matrix to the pins listed. 
E.g. Matrix x = [[1, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 1]]
     matrixcomm(x) -> (handshake 0) to all 8 bits
     '' -> 1, 0, 1, 1, ... to all 8 bits
     '' -> 0, 1, 1, 0, ... ''
     '' -> (handshake 1) to all 8 bits. 
'''

snake_start = [0,0,0,0,0,0,0,1]
raindrop_start = [0,0,0,0,0,0,1,0]
tetris_start = [0,0,0,0,0,0,1,1]
menu_start = [0,0,0,0,0,0,0,0]
program_check = [0,0,0,0,0,0,0,1]

current_game = 0
frame_count = 0
delay = .001

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

controller = []
controller1 = 0
controller2 = 0
controller3 = 0
controller4 = 0 
controller5 = 0 
controller6 = 0 
controller7 = 0
controller8 = 0

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
    global controller7
    global controller8
    global controller
    
    controller1 = 6
    controller2 = 12
    controller3 = 11
    controller4 = 9 
    controller5 = 13
    controller6 = 10 
    controller = [controller1,controller2,controller3,controller4,controller5,controller6]

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

    io.setmode(io.BCM)
    for i in pins:
        io.setup(i, io.OUT)
    
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


def queryController(buttonNumber):
    print(buttonNumber)
    return io.input(controller[buttonNumber])


def changeProgram(numberofProgram):
    global current_game
    current_game = numberofProgram
    startupSignal(current_game)


def startupSignal(numberofProgram):
    bytecomm(program_check)
    if numberofProgram == 0:
        bytecomm(menu_start)
    elif numberofProgram == 1:
        bytecomm(snake_start)
    elif numberofProgram == 2:
        bytecomm(raindrop_start)
    elif numberofProgram == 3:
        bytecomm(tetris_start)


def matrixcomm(matrix):    
    print(matrix)
    #global frame_count
    #frame_count += 1
    #if frame_count % 32 == 0:
    #    frame_count = 0
    #    bytecomm(program_check)
    #    bytecomm(current_game)

    handshake = [[[1] * 8], [[0] * 8]]
    bytecomm(handshake[1][0])
    for x in matrix:
        for y in x:
            for z in y:
                bytecomm(z)
    bytecomm(handshake[0][0])
    return


def bytecomm(array):
    count = 0
    pins = [clock, pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8]
    io.output(clock, 1)
    flipped = array[::-1]
    for pin in pins[1:]:
        io.output(pin, int(flipped[count]))
        count += 1

    sleep(delay)
    io.output(clock, 0)
    sleep(delay)
    io.output(clock, 1)
    return

