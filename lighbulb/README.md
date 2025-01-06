# Task
Some light bulbs are placed in a circle (clockwise direction). Each one is either on (1) or off (0).

Every turn, the light bulbs change their states. If a light bulb was on at the previous turn, the light bulb to the right of it changes its state, i.e. if lights[0] is on. then, if lights[1] was on, it turns off and vice versa.

Find the state of the light bulbs after n turns.

# Input/Output
[input] integer array lights
A non-empty array, the initial states of the light bulbs.

0 ≤ lights.length ≤ 100

[input] integer n
The number of turns.

0 ≤ n ≤ 300

[output] an integer array
The final light bulbs' states.

# Example
For lights = [0,1,1,0,1,1], n = 2, the output should be [1, 0, 1, 1, 0, 1]