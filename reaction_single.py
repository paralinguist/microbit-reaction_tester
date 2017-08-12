from microbit import *
import random
wait_time = random.randint(2000, 10000)
display.show(Image.ASLEEP)
sleep(wait_time)
if button_a.get_presses():
    display.show(Image.NO)
else:
    display.show(Image.TARGET)
    waiting = True
    reaction_time = 0
    while waiting:
        if button_a.is_pressed():
            waiting = False
        sleep(10)
        reaction_time = reaction_time + 10
    display.show(Image.YES)
    sleep(1000)
    while True:
        display.scroll(str(reaction_time))