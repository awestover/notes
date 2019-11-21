
import time
import datetime
import os

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

data = {
    "Monday": [("11:12", "lunch")],
    "Tuesday": [("10:17", "psych"), ("12:10", "lunch")],
    "Wednesday": [("11:12", "lunch")], 
    "Thursday": [("3:00", "Functional Analysis")],
    "Friday": [("8:55", "psych"), ("11:40", "lunch")]
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


