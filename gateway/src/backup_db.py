#!/usr/bin/env python
import time
from datetime import datetime, timedelta
from time import sleep

SECONDS_PER_DAY = 24 * 60 * 60


def doFunc():
    print "do Function..."


def doFirst():
    curTime = datetime.now()
    print curTime
    desTime = curTime.replace(hour=20, minute=0, second=0, microsecond=0)
    print desTime
    delta = desTime-curTime
    sleeptime = delta.total_seconds()
    print "Now day must sleep %d seconds" %     sleeptime
    sleep(sleeptime)
    doFunc()


if __name__ == "__main__":
    doFirst()
