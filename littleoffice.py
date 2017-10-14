import datetime

def whichHour():
	hour = ""
	now = datetime.datetime.now()

	if 4 <= now.hour < 9:
		hour += "morning"
	elif 9 <= now.hour < 17:
		hour += "daytime"
	elif 17 <= now.hour <= 21:
		hour += "evening"
	else:
		hour += "night"
	return hour

def whichDay():
	day = ""
	weekday = datetime.datetime.today().weekday()

	if weekday == 0:
		day += "monday"
	elif weekday == 1:
		day += "tuesday"
	elif weekday == 2:
		day += "wednesday"
	elif weekday == 3:
		day += "thursday"
	elif weekday == 4:
		day += "friday"
	elif weekday == 5:
		day += "saturday"
	else:
		day += "sunday"
	return day

day = whichDay()
hour = whichHour()

print("The current prayer for The Little Office of the Blessed Virgin Mary is " + day + " " + hour)

# Still need to insert actual hours

