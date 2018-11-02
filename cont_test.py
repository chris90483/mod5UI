# !/usr/bin/python3
import communication as comm
import RPi.GPIO as io

io.setmode(io.BCM)
io.setup(5,io.OUT)
io.setup(6,io.OUT)
io.setup(12,io.OUT)
io.setup(13,io.OUT)
io.setup(9,io.OUT)
io.setup(10,io.OUT)
buttons = [5,6,12,13,9,10]

while True:
    for i in range(0,6):
        x = comm.queryController(i)
        if x:
            io.output(buttons[i], 1)
        else: 
            io.output(buttons[i], 0)

