from L2_compass_heading import get_heading
import time
import csv
from L1_log import tmpFile
from L1_log import stringTmpFile


def Cardinal():
    Degrees = int(get_heading())
    directions = ['North', 'North West', 'West', 'South West', 'South', 'South East', 'East', 'North East', 'North']
    index = round(Degrees / 45) % 8  
    return directions[index]


if __name__ == "__main__":
    while True:
        CD = Cardinal()
        Heading = get_heading()
        stringTmpFile(CD, "CDTempFile")
        tmpFile(Heading, "HeadingTempFile")
        time.sleep(0.1)