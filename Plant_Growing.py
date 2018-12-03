"""
Each day a plant is growing by upSpeedmeters. Each night that plant's height decreases by downSpeed meters due to the lack of sun heat. Initially, plant is 0 meters tall. We plant the seed at the beginning of a day. We want to know when the height of the plant will reach a certain level.
Example
For upSpeed = 100, downSpeed = 10, and desiredHeight = 910, the output should be
growingPlant(upSpeed, downSpeed, desiredHeight) = 10.
"""

def growingPlant(upSpeed, downSpeed, desiredHeight):
    plantHeight = 0
    count = 0
    while plantHeight < desiredHeight:
        plantHeight += upSpeed
        count += 1
        if upSpeed >= desiredHeight:
            return 1
        if(plantHeight >= desiredHeight):
            return count
        else:
            plantHeight -= downSpeed
        if plantHeight > desiredHeight:
            count -= 1
    return count
