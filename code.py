"""
blinking LED, but the dlayed time between each blink increases

Feb 19
Sophie Nguyen
"""
import time
import board
import digitalio

#variables
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
blink_time = 1000

# loop
while True:
    #turns on LED
    led.value = True
    #wait 1 second
    time.sleep(1)
    #turns LED off
    led.value = False
    time.sleep(1)

    #blink time increases by 1 second
    blink_time += 1000