

from L1_ina import readVolts
from L3_Compass import Cardinal
from L2_compass_heading import get_heading
import csv
import time
from L1_log import tmpFile
from L1_log import stringTmpFile


if __name__ == "__main__":
    while True:
        myBatt = round(readVolts(),2)       # collect a reading
        print("Battery Voltage: ",myBatt)   # print the reading
        tmpFile(myBatt, "VoltageTempFile")
        CD = Cardinal()
        Heading = get_heading()
        stringTmpFile(CD, "CDTempFile")
        tmpFile(Heading, "HeadingTempFile")
        time.sleep(1)                       # pause