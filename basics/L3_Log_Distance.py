from L2_vector import getNearest
from L2_vector import polar2cart
from L1_log import tmpFile
from L1_ina import readVolts
import time

if __name__ == "__main__":
    while True:
        myBatt = round(readVolts(),2)       # collect a reading
        print("Battery Voltage: ",myBatt)   # print the reading
        tmpFile(myBatt, "VoltageTempFile")
        B = getNearest()
        tmpFile(B[0], "DistanceTempFile")
        tmpFile(B[1], "AngleTempFile")
        print("Distance: ", B[0])
        print("Angle: ", B[1])
        C = polar2cart(B[0],B[1])
        tmpFile(C[0], "XcoorTempFile")
        tmpFile(C[1], "YcoorTempFile")
        print("X", C[0])
        print("Y", C[1])
        time.sleep(0.5)