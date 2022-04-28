#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait
from time import clock


def lineFollowingReflection(leftWheel, rightWheel, countTarget, isForward=True, lookForColor=False, lookingSensor=None, colors=None, terminalTime=1000):
    lightSensorLeft = ColorSensor(Port.S4)
    lightSensorRight = ColorSensor(Port.S1)

    count = 0
    canCount = True
    speedScale = 4
    lineFollowingMode = True
    initialTime = clock()

    if not isForward:
        # speedScale -= 1 # slightly slower
        speedScale *= -1  # make everything backward

    # 0 < BLACK < 20
    # 20 <= WHITE < 100
    WHITE = 20

    finalColor = None

    while lineFollowingMode:
        leftLight = lightSensorLeft.reflection()
        rightLight = lightSensorRight.reflection()

        # TODO: rewrite but inverse for going backward
        if isForward:
            # go straight
            if leftLight >= WHITE and rightLight >= WHITE:
                leftWheel.run(100 * speedScale)
                rightWheel.run(100 * speedScale)
                canCount = True

            # if black, white it's swaying to the right, hence should turn left
            if leftLight < WHITE and rightLight >= WHITE:
                leftWheel.run(70 * speedScale)
                rightWheel.run(120 * speedScale)
                canCount = True

            # if white, black, it's swaying to the left, hence should turn right
            if leftLight >= WHITE and rightLight < WHITE:
                leftWheel.run(120 * speedScale)
                rightWheel.run(70 * speedScale)
                canCount = True

            # counting the intersections it passes through
            if leftLight < WHITE and rightLight < WHITE and canCount:
                count += 1
                print(count)
                canCount = False
        else:
            # go straight
            if leftLight >= WHITE and rightLight >= WHITE:
                leftWheel.run(100 * speedScale)
                rightWheel.run(100 * speedScale)
                canCount = True

            # if black, white it's swaying to the right, hence should turn left
            if leftLight < WHITE and rightLight >= WHITE:
                leftWheel.run(120 * speedScale)
                rightWheel.run(70 * speedScale)
                canCount = True

            # if white, black, it's swaying to the left, hence should turn right
            if leftLight >= WHITE and rightLight < WHITE:
                leftWheel.run(70 * speedScale)
                rightWheel.run(120 * speedScale)
                canCount = True

            # counting the intersections it passes through
            if leftLight < WHITE and rightLight < WHITE and canCount:
                count += 1
                print(count)
                canCount = False

        # end line following mode
        # if count is equal to designated value.
        if countTarget == count:
            lineFollowingMode = False
        # or reached the wanted color.
        if lookForColor:
            if lookingSensor != None:
                for color in colors:
                    if lookingSensor.color() == color:
                        print("successS!")
                        finalColor = color
                        lineFollowingMode = False
            else:
                for color in colors:
                    if lightSensorLeft.color() == color:
                        print("ayo")
                        finalColor = color
                        lineFollowingMode = False

        # or reached the terminal time
        timePassed = clock() - initialTime
        if timePassed >= terminalTime:
            lineFollowingMode = False

    leftWheel.stop()
    rightWheel.stop()

    return finalColor
