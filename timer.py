
"""
adapted from:
https://stackoverflow.com/questions/25189554/countdown-clock-0105#
\r is a carriage return, it means 'write over my last line'
"""

import sys
import time

def countdown(totalTime):
  print("Starting timer for {} seconds".format(totalTime))
  while totalTime:  # until it hits 0
    mins, secs = divmod(totalTime, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)  # 2 digits
    print(timeformat, end='\r')  # overwrite last time
    time.sleep(1)
    totalTime -= 1
  print('The end\n\n\n')

# set the timer
try:
  secs = int(sys.argv[1])
  countdown(secs)
except:
  print("Invalid (or missing) argument to timer "+
          "(must be an ammount of seconds)")

