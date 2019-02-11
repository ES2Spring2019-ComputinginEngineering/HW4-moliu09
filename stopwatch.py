
# HOMEWORK 4 --- ES2
# Stopwatch

# FILL THESE COMMENTS IN
#*****************************************
# YOUR NAME: Mo Liu
# NUMBER OF HOURS TO COMPLETE:
# YOUR COLLABORATION STATEMENT(s): I worked on this assignment with Nicolas Ragusa and Alyssa Attonito.
#
#
#*****************************************

# Create a micro:bit stopwatch which displays the number
# of seconds that you hold down one of the micro:bit buttons.

# You may wish to accomplish this using a while loop that
# checks whether the button is being pressed. When it is,
# you can update the time elapsed and when it is not, you
# can display that time.

# You will want to make use of the microbit function called
# microbit.running_time() which has a return value of the
# number of milliseconds since the microbit started running.

# You will need to add some while loops and other code in
# order to turn this into a stopwatch that times how long
# the button is held down for.

import microbit
time0 = microbit.running_time()
time1 = microbit.running_time()
elapsed_time = time1 - time0 #calculates difference in milliseconds

while True:
    elapsed_time = time1 - time0
    while microbit.button_a.is_pressed() == True:
        microbit.display.show(microbit.Image.CLOCK2)
        time0 = microbit.running_time()
        microbit.sleep(50)
        time1 = microbit.running_time()
        elapsed_time = elapsed_time + (time1 - time0)
    timeinseconds = elapsed_time/1000
    microbit.display.scroll(round(timeinseconds, 2))
    print(elapsed_time, " milliseconds")
    microbit.display.show(microbit.Image.HEART)
    elapsed_time = 0
