

from L1_ina import readVolts
import csv
import time
from L1_log import tmpFile

if __name__ == "__main__":
    while True:
        myBatt = round(readVolts(),2)       # collect a reading
        print("Battery Voltage: ",myBatt)   # print the reading
        tmpFile(myBatt, "VoltageTempFile")
        time.sleep(1)                       # pause