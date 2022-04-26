#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from robot import Robot


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
claw = Motor(Port.C)
leftWheel = Motor(Port.D)
rightWheel = Motor(Port.A)
armLift = Motor(Port.B)
objectDetector = ColorSensor(Port.S2)

bob = Robot(leftWheel, rightWheel, armLift, claw, objectDetector)

timeTillCenter = 1

# Write your program here.
ev3.speaker.beep()


def task2():
    bob.armDown()

    bob.lineFollowing(100, lookForColor=True,
                      lookingSensor=objectDetector, color=Color.GREEN)

    bob.armUp()
    bob.adjustToLaundry()

    bob.pickUp()

    bob.turnForward(180)

    bob.lineFollowing(4)

    bob.putDown()


def task3():
    bob.armDown()

    bob.lineFollowing(100, lookForColor=True,
                      lookingSensor=objectDetector, color=Color.GREEN)

    bob.armUp()
    bob.adjustToLaundry()

    bob.pickUp()

    bob.turnForward(180)

    bob.lineFollowing(2)
    bob.turnForward(90)
    bob.lineFollowing(100, terminalTime=timeTillCenter)

    bob.turnForward(-90)

    bob.lineFollowing(1)

    bob.turnForward(90)

    bob.lineFollowing(1)

    bob.putDown()


def task4():
    bob.lineFollowing(1)
    # TODO: water Bottle adjust
    bob.adjustToWater()

    bob.pickUp()
    bob.turnForward(-90)

    # Water path with the nurse

    bob.lineFollowing(1)
    bob.turnForward(-90)

    bob.lineFollowing(1)
    bob.turnForward(90)

    bob.lineFollowing(2)
    bob.turnForward(-90)

    bob.lineFollowing(1000, lookForColor=True, color=Color.BLUE)

    bob.adjustToTable(1)  # turning right

    bob.clawOpen()

    # ------------ 4.1 -------------""
    bob.backFromTable()  # 1

    bob.turnForward(90)  # 3
    bob.armDown()  # 3.1
    bob.clawClose()     # 2

    # TODO: GEt on the white first
    bob.outtaRoom()

    task5()


def task5():
    bob.lineFollowing(1)  # 4
    bob.turnForward(90)   # 5
    bob.lineFollowing(1)  # 6
    bob.turnForward(-90)  # 7
    print("time to pick up")
    bob.lineFollowing(100, lookForColor=True,
                      lookingSensor=objectDetector, color=Color.GREEN)

    # print("arrived!")
    bob.armUp()
    bob.adjustToLaundry()
    bob.pickUp()

    bob.lineFollowing(1, isForward=False)
    bob.turnBackward(90)

    # --------- from task 3 ------
    bob.lineFollowing(1)
    bob.turnForward(90)
    bob.lineFollowing(100, terminalTime=timeTillCenter)

    bob.turnForward(-100)

    bob.lineFollowing(1)

    bob.turnForward(90)

    bob.lineFollowing(1)

    bob.putDown()


def task6():  # for the ball

    bob.lineFollowing(100, lookForColor=True,
                      lookingSensor=objectDetector, color=Color.RED)

    bob.pickUp()


def task7():
     bob.lineFollowing(1)
    # TODO: water Bottle adjust
    bob.adjustToWater()

    bob.pickUp()
    bob.turnForward(90)

    bob.lineFollowing(1)
    bob.turnForward(90)

    bob.lineFollowing(1)
    bob.turnForward(-90)

    bob.lineFollowing(1)
    # between the two indicating blocks

    bob.turnForward(90)
    bob.