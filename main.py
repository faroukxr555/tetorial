import microbit # import the micro:bit library
import time     # import time library

myButton = micro:bit.button_a   # defline Variable to be our Button
outputpin = microbit.pin0        # defline Variable to be output pin
while True:
    if mybutton.is_pressed()  == 1:           # check if the button is pressed
        if outputpin .read_degital()          # read the current state  of the LedSpriteProperty
            outputpin.write_degital(0)        # if led is on Turn it radio.off()
        else:
        outputpin.write_degital(1)            #  if led is not on, turn it on
        time.sleep(.5)
        microbit.sleep(125)
