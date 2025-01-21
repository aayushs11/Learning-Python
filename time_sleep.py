import datetime
import time

#Display date and time in the interval of 1 sec
while True:
    present= datetime.datetime.now()
    print(present)

    time.sleep(1)