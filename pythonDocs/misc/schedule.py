
import time
import datetime
import os

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

data = {
    "Monday": [("11:40", "Psych"), ("4:00", "PRIMES"), ("6:00", "BEACON"), ("9:00", "READ")],
    "Tuesday": [("10:17", "psych"), ("12:35", "Chinese"), ("2:00", "PRIMES"), ("3:00", "READ")],
    "Wednesday": [("11:40", "Chinese"), ("3:00", "PRIMES"), ("5:00", "BEACON"), ("9:00", "READ")], 
    "Thursday": [("1:00", "PRIMESx2"), ("3:00", "BEACONx2"), ("9:00", "READ")],
    "Friday": [("8:55", "psych"), ("12:07", "Chem"), ("5:30", "GAME"), ("9:00", "READ")],
    "Saturday": [("12:00", "PRIMESx2"), ("2:00", "BEACONx2"), ("9:00", "READ")],
    "Sunday": [("12:00", "PRIMESx2"), ("2:00", "BEACONx2"), ("4:00", "BOM"), ("9:00", "READ")]
}

def send_alert(activity, mins_left, event_time):
    message = f"{activity} at {event_time} in {mins_left} minutes"
    title = f"GOTO {activity} NOW / SOON!"
    subtitle = "plz"
    sound = "Glass"
    os.system(f"osascript -e 'display notification \"{message}\" with title \"{title}\" subtitle \"{subtitle}\" sound name \"{sound}\"'")

while True:
    cur_time = datetime.datetime.today()
    day = weekdays[cur_time.weekday()]
    hour = cur_time.hour
    minute = cur_time.minute

    print(day)
    print(data[day])
    for datum in data[day]:
        datum_hr, datum_min = datum[0].split(":")
        datum_hr, datum_min = int(datum_hr), int(datum_min)
        time_left = (datum_hr - hour)*60 + datum_min - minute
        if time_left > 0:
            if time_left < 3:
                send_alert(datum[1], time_left, datum[0])
            print(f"{datum[1]} at {datum[0]} in {time_left} minutes")
            break

    time.sleep(60)


