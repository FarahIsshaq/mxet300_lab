from L2_kinematics import getPdCurrent
from L2_kinematics import getMotion
from L1_log import tmpFile
from L1_ina import readVolts
import time


if __name__ == "__main__":
    while True:
        myBatt = round(readVolts(),2)       # collect a reading
        print("Battery Voltage: ",myBatt)   # print the reading
        tmpFile(myBatt, "VoltageTempFile")
        B = getPdCurrent()
        tmpFile(B[0], "LeftMotorTempFile")
        tmpFile(B[1], "RightMotorTempFile")
        print("Left", B[0])
        print("Right", B[1])
        C = getMotion()
        print(C[0])
        tmpFile(C[0], "xdotTempFile")
        tmpFile(C[1], "thetadotTempFile")
        time.sleep(1)                       # pause