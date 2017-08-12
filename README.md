# microbit-reaction_tester
Micropython MicroBit demo program - simple reaction tester
The tester generates a random wait time and displays a sleeping graphic.
The tester switches to a target graphic when it is ready for the user to press a button and counts in blocks of 10 ms
until the button is pressed.
When pressed, the display changes to a tick and then displays the reaction time in ms.
It should be noted that while it technically counts up in 10ms blocks, the reality is that it is not really this precise.
Some tweaking might be advisable to determine the kind of precision the M:B can support.
