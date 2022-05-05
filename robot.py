from pybricks.tools import wait, StopWatch, DataLog
from linefollowing import lineFollowingReflection


class Robot:
    def __init__(self, leftWheel, rightWheel, armLift, claw, objectDetector):
        self.leftWheel = leftWheel
        self.rightWheel = rightWheel
        self.armLift = armLift
        self.claw = claw
        self.objectDetector = objectDetector

        self.clawPower = 1700
        self.armPower = 500
        self.armDegree = 180

        self.SLOWMODE = 3
        self.DEFAULTMODE = 4

    def lineFollowing(self, countTarget, speed=4, isForward=True, lookForColor=False, lookingSensor=None, colors=None, terminalTime=1000):
        return lineFollowingReflection(self.leftWheel, self.rightWheel, countTarget, speed=speed, isForward=isForward,
                                       lookForColor=lookForColor, lookingSensor=lookingSensor, colors=colors, terminalTime=terminalTime)

    def clawOpen(self):
        self.claw.run(self.clawPower - 200)
        wait(1500)  # 1000 works for the laundry
        self.claw.stop()

    def clawClose(self):
        self.claw.run(-self.clawPower)
        wait(1500)
        self.claw.stop()

    def clawGrasp(self):
        self.claw.run(-self.clawPower)
        wait(1200)
        self.claw.stop()

    def armUp(self, degree=0):
        if degree == 0:
            degree = self.armDegree
        self.armLift.run_angle(self.armPower, +degree)

    def armDown(self, degree=0):
        if degree == 0:
            degree = self.armDegree
        self.armLift.run_angle(self.armPower, -degree)

    def turnForward(self, angle):
        if angle == 0:
            return None

        self.leftWheel.run(200 * angle / abs(angle))
        self.rightWheel.run(-200 * angle / abs(angle))

        wait(12 * abs(angle))

        self.leftWheel.stop()
        self.rightWheel.stop()

    def turnBackward(self, angle):
        angleAdjustment = 0.8

        if angle == 0:
            return None

        self.leftWheel.run((200 + angle * angleAdjustment)
                           * angle / abs(angle))
        self.rightWheel.run(-(200 - angle * angleAdjustment)
                            * angle / abs(angle))

        wait(12 * abs(angle))

        self.leftWheel.stop()
        self.rightWheel.stop()

    def adjustToLaundry(self):
        self.leftWheel.run_angle(200, 90, wait=False)
        self.rightWheel.run_angle(200, 90, wait=True)

    def adjustToWater(self):
        self.leftWheel.run_angle(100, -90, wait=False)
        self.rightWheel.run_angle(100, -90, wait=True)

    def adjustToTable(self, direction):  # right is +
        self.leftWheel.run_angle(300, 300, wait=False)
        self.rightWheel.run_angle(300, 300, wait=True)
        self.turnForward(90 * direction)
        self.leftWheel.run_angle(100, 100, wait=False)
        self.rightWheel.run_angle(100, 100, wait=True)

    def adjustForPickingUp(self):
        # push until it touches Bob
        # change 360 degress later
        self.leftWheel.run_angle(200, 270, wait=False)
        self.rightWheel.run_angle(200, 270, wait=True)

        # go back as needed
        self.leftWheel.run_angle(200,  -95, wait=False)
        self.rightWheel.run_angle(200, -95, wait=True)

    def backFromTable(self):
        self.leftWheel.run_angle(100, -150, wait=False)
        self.rightWheel.run_angle(100, -150, wait=True)

    def outtaRoom(self):
        self.leftWheel.run_angle(300, 300, wait=False)
        self.rightWheel.run_angle(300, 300, wait=True)

    def pickUp(self):
        self.clawOpen()
        self.armDown()
        self.clawClose()
        self.armUp()

    def pickUpWithAdjust(self):
        self.lineFollowing(1, speed=self.SLOWMODE)

        self.adjustForPickingUp()

        self.pickUp()

    def putDown(self):
        self.armDown()
        self.clawOpen()
        self.armUp()
        self.clawClose()

    # --------- Util Tools ------------"

    def downClose(self):
        self.armDown()
        self.clawClose()

    def testClaw(self):
        self.clawClose()
        self.clawOpen()

    def testArm(self):
        self.armDown()
        wait(5000)
        self.armUp()
