from microbit import *
import random
#Generate a random time between 2 and 10 seconds
wait_time = random.randint(2000, 10000)
#Sleep for the randomly generated time
display.show(Image.ASLEEP)
sleep(wait_time)
#This if statement checks if the user pressed the button early
if button_a.get_presses():
    display.show(Image.NO)
else:
    #notify the user that they can press the button
    display.show(Image.TARGET)
    waiting = True
    reaction_time = 0
    #Keep counting up until the user presses the button
    while waiting:
        if button_a.is_pressed():
            waiting = False
        sleep(10)
        reaction_time = reaction_time + 10
    display.show(Image.YES)
    sleep(1000)
    while True:
        #Show the reaction time. This is not terribly accurate
        display.scroll(str(reaction_time))