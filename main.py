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
withWaterBottleDegree = 80
SLOWMODE = 3
DEFAULTMODE = 4

# Write your program here.
ev3.speaker.beep()


def task2():
    bob.armDown()

    bob.lineFollowing(100, lookForColor=True,
                      lookingSensor=objectDetector, colors=[Color.GREEN])

    bob.armUp()
    bob.adjustToLaundry()

    bob.pickUp()

    bob.turnForward(180)

    bob.lineFollowing(4)

    bob.putDown()


def task3():
    bob.armDown()

    bob.lineFollowing(100, lookForColor=True,
                      lookingSensor=objectDetector, colors=[Color.GREEN])

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


def task4():  # put the water bottle on the table
    """
    remove the comments when only doing task 4
    bob.lineFollowing(1)
    # TODO: water Bottle adjust
    bob.adjustToWater()

    bob.pickUp()
    bob.turnForward(-90)

    """

    # Water path with the nurse

    bob.lineFollowing(1)
    bob.turnForward(-90)

    bob.lineFollowing(1)
    bob.turnForward(90)

    bob.lineFollowing(2)
    bob.turnForward(-90)

    bob.lineFollowing(1000, lookForColor=True, colors=[Color.BLUE])

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
                      lookingSensor=objectDetector, colors=[Color.GREEN])

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
                      lookingSensor=objectDetector, colors=[Color.RED])

    bob.pickUp()


def task7():

    bob.lineFollowing(1, speed=SLOWMODE)
    # TODO: water Bottle adjust
    # bob.adjustToWater()

    bob.pickUp()
    bob.turnForward(90)

    bob.lineFollowing(1)
    bob.turnForward(90)

    bob.lineFollowing(1)
    bob.turnForward(-90)

    bob.lineFollowing(2)  # go past between the indicating blocks
    bob.putDown()  # put down water bottle
    bob.adjustToWater()

    bob.turnForward(180)

    bob.armDown()

    bob.lineFollowing(1, speed=SLOWMODE)
    bob.turnForward(-90)

    # TODO: the arm has to be lowered at this point

    tableDir = -1  # negative is left
    for _ in range(2):
        indColor = bob.lineFollowing(100, speed=SLOWMODE, lookForColor=True,
                                     lookingSensor=objectDetector, colors=[Color.RED, Color.GREEN])

        print(indColor)
        if indColor == Color.GREEN:  # Water bottle room!
            print("Water bottle")
            bob.turnForward(180)

            break

        if indColor == Color.RED:  # frick
            tableDir = 1  # positive is right

        bob.turnForward(180)

    print("out of function")
    bob.lineFollowing(1, speed=SLOWMODE)
    bob.turnForward(-90 * tableDir)  # opposite of table dir
    # out of decision path

    # pull claw back up
    bob.armUp()

    bob.pickUpWithAdjust()

    bob.lineFollowing(1, isForward=False, speed=SLOWMODE)

    bob.turnBackward(-90 * tableDir)  # room dir is opposite of table dir

    bob.lineFollowing(1000, lookForColor=True, colors=[
                      Color.RED, Color.GREEN], speed=2)

    bob.adjustToTable(tableDir)

    bob.clawOpen()  # placed the water bottle on the table

    bob.backFromTable()  # 1

    bob.turnForward(90 * tableDir)  # 3
    bob.clawClose()
    bob.outtaRoom()
    bob.lineFollowing(1)
    bob.turnForward(90 * tableDir)

    print("out of task 7")


def task8():  # task 7 + task 4
    task7()

    bob.lineFollowing(2)
    bob.turnForward(90)
    # have to do a zigzag cause it isn't two black lines
    bob.lineFollowing(100, terminalTime=timeTillCenter)

    bob.turnForward(-90)

    bob.lineFollowing(1)  # in front of the waterbottles

    bob.adjustPickWater()
    bob.turnForward(85)

    bob.lineFollowing(1, speed=bob.SLOWMODE)

    bob.adjustForPickingUp()
    bob.pickUp()

    bob.lineFollowing(1, isForward=False)
    bob.turnForward(-90)

    task4()


task8()
