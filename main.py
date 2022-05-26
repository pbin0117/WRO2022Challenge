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

    bob.lineFollowing(1, speed=bob.SLOWMODE)
    bob.turnForward(90)

    bob.lineFollowing(2)
    bob.adjustAfterLineFollow()
    bob.turnForward(-90)

    bob.lineFollowing(1000, lookForColor=True, colors=[Color.BLUE])

    bob.adjustToTable(1)  # turning right

    bob.clawOpen()

    # ------------ 4.1 -------------""
    bob.backFromTable()  # 1

    bob.turnForward(90)  # 3
    # bob.armDown()  # 3.1
    bob.clawClose()     # 2

    # TODO: GEt on the white first
    bob.outtaRoom()

    # remove when not doing task 9
    # task5()


def task5():
    bob.lineFollowing(1)  # 4
    bob.turnForward(90)   # 5
    bob.lineFollowing(1, speed=bob.SLOWMODE)  # 6

    bob.turnForward(-90)  # 7
    print("time to pick up")
    bob.lineFollowing(100, speed=bob.SLOWMODE, lookForColor=True,
                      lookingSensor=objectDetector, colors=[Color.GREEN])

    # print("arrived!")
    bob.armUp()
    bob.adjustToLaundry()
    bob.pickUp(extra1=True)

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
    bob.putDown(clawClose=False)  # put down water bottle
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
        bob.getOutofBB()

    print("out of function")
    bob.lineFollowing(1, speed=SLOWMODE)
    bob.adjustAfterLineFollow()

    bob.turnForward(-90 * tableDir)  # opposite of table dir
    # out of decision path

    # pull claw back up
    bob.armUp()

    bob.pickUpWithAdjust(clawOpen=False)

    bob.lineFollowing(1, isForward=False, speed=SLOWMODE)

    bob.turnBackward(-90 * tableDir)  # room dir is opposite of table dir
    bob.adjustAfterLineFollow()

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

    bob.lineFollowing(100, speed=bob.SLOWMODE,
                      terminalTime=timeTillCenter + 0.5)

    bob.turnForward(-95)

    bob.lineFollowing(1)  # in front of the waterbottles

    bob.adjustPickWater()
    bob.turnForward(80)

    bob.lineFollowing(1, speed=bob.SLOWMODE)

    bob.adjustForPickingUp()
    bob.pickUp()

    bob.lineFollowing(1, isForward=False)
    bob.turnForward(-90)

    task4()


def task9():
    # TODO: add all of the adjust after lineFollow where appropriate
    # in combination with the previous task
    # ----------------------------
    task8()

    # ----------------------------
    # add in previous task if wanted
    # remove comments if only doing task 9
    """
    bob.lineFollowing(3)
    bob.adjustAfterLineFollow()
    bob.turnForward(90)
    """

    bob.lineFollowing(100, speed=bob.SLOWMODE,
                      lookForColor=True, colors=[Color.YELLOW])
    bob.yaya()  # in the yellow room
    bob.turnForward(90)  # facing the laundry block, hopefully

    # don't need when doing the whole task
    bob.armDown()  # have to put it down to detect the green block

    bob.lineFollowing(100, speed=bob.SLOWMODE, lookForColor=True, colors=[
                      Color.BLACK], lookingSensor=objectDetector)

    # problem

    bob.armUp()
    bob.adjustToLaundry()
    bob.pickUp(extra1=True)

    bob.turnForward(90)
    bob.lineFollowing(1)  # out of the yellow room

    bob.adjustAfterLineFollow()
    bob.turnForward(-90)

    # rest is similar to task 5
    bob.lineFollowing(2)
    bob.turnForward(90)
    bob.lineFollowing(100, terminalTime=timeTillCenter)

    bob.turnForward(-100)

    bob.lineFollowing(1)

    bob.turnForward(90)

    bob.lineFollowing(1)

    bob.clawOpen()
    bob.clawClose()

    bob.leftWheel.run_angle(150, -250, wait=False)
    bob.rightWheel.run_angle(150, -250, wait=True)
    bob.turnForward(180)

    bob.lineFollowing(1000, terminalTime=timeTillCenter+0.3)


def task10():
    task7()

    bob.lineFollowing(2)
    bob.turnForward(90)

    bob.lineFollowing(100, speed=bob.SLOWMODE,
                      terminalTime=timeTillCenter + 0.5)

    bob.turnForward(-95)

    bob.lineFollowing(1)  # in front of the waterbottles

    bob.adjustPickWater()
    bob.turnForward(80)

    bob.lineFollowing(1, speed=bob.SLOWMODE)

    bob.adjustForPickingUp()
    bob.pickUp()

    bob.lineFollowing(1, isForward=False)
    bob.turnForward(-90)
# ==============================================
    bob.lineFollowing(1)
    bob.turnForward(-90)

    bob.lineFollowing(1, speed=bob.SLOWMODE)
    bob.turnForward(90)
# ================================================
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
        bob.getOutofBB()

    print("out of function")
    bob.lineFollowing(1, speed=SLOWMODE)
    bob.adjustAfterLineFollow()

    bob.turnForward(-90 * tableDir)  # opposite of table dir
    # out of decision path

    # pull claw back up
    bob.armUp()

    bob.pickUpWithAdjust()

    bob.lineFollowing(1, isForward=False, speed=SLOWMODE)

    bob.turnBackward(-100 * tableDir)  # room dir is opposite of table dir
    bob.adjustAfterLineFollow()

    print(bob.lineFollowing(1000, lookForColor=True, colors=[
        Color.BLUE, Color.YELLOW], speed=2))

    bob.adjustToTable(tableDir)

    bob.clawOpen()  # placed the water bottle on the table

    bob.backFromTable()  # 1
    bob.turnForward(90 * tableDir)
    bob.clawClose()
    bob.outtaRoom()

    bob.lineFollowing(1, speed=bob.SLOWMODE)

    bob.leftWheel.run_angle(200, 360, wait=False)
    bob.rightWheel.run_angle(200, 360, wait=True)

    # -----------------------------------------
    bob.lineFollowing(100, speed=bob.SLOWMODE,
                      lookForColor=True, colors=[Color.YELLOW, Color.BLUE])
    bob.yaya()  # in the yellow room
    bob.turnForward(90 * tableDir)  # facing the laundry block, hopefully

    # don't need when doing the whole task
    bob.armDown()  # have to put it down to detect the green block

    bob.lineFollowing(100, speed=bob.SLOWMODE, lookForColor=True, colors=[
                      Color.BLACK], lookingSensor=objectDetector)

    # problem

    bob.armUp()
    bob.adjustToLaundry()
    bob.pickUp(extra1=True)

    bob.turnForward(80 * tableDir)
    bob.outtaRoom()
    bob.lineFollowing(1)  # out of the yellow room

    bob.adjustAfterLineFollow()
    bob.turnForward(-90 * tableDir)

    # rest is similar to task 5
    bob.lineFollowing(2)
    bob.turnForward(90)
    bob.lineFollowing(100, terminalTime=timeTillCenter)

    bob.turnForward(-100)

    bob.lineFollowing(1)

    bob.turnForward(90)

    bob.lineFollowing(1)

    bob.clawOpen()
    bob.clawClose()

    bob.leftWheel.run_angle(150, -250, wait=False)
    bob.rightWheel.run_angle(150, -250, wait=True)
    bob.turnForward(180)

    bob.lineFollowing(1000, terminalTime=timeTillCenter+0.3)


task10()
