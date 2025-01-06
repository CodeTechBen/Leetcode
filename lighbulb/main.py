"""Turn the lights off or on depending on the lightbulb to the right"""

def light_bulbs(lights, n):
    for _ in range(n):
        new_lights = lights[:]

        for i in range(len(lights)):
            if lights[i] == 1:
                if i + 1 < len(lights):
                    new_lights[i + 1] = 1 - new_lights[i + 1]
                else: 
                    new_lights[0] = 1 - new_lights[0]
        lights = new_lights

    return lights
